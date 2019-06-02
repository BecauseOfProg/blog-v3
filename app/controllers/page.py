from core.utils.fill_informations import fill_informations
from pony.orm import db_session, select, desc
from flask import render_template, request
from app.models.article import Articles
from app.models.user import User
from core.utils.links import links_list

class PageController:
  @staticmethod
  @db_session
  def about():
    '''Displays the 'about' page with a list of the staff'''
    stafflist = []
    roles = {
      "POST_WRITE": "Membre",
      "BLOG_WRITE": "Rédacteur",
      "USER_WRITE": "Modérateur"
    }
    staff = select(u for u in User if str(u.permissions) != '[]')[:]
    for user in staff:
      stafflist.append({
        'username': user.username,
        'displayname': user.displayname,
        'description': user.description,
        'avatar': user.avatar,
        'permissions': user.permissions
      })
    return render_template('page/about.html', staff=stafflist, roles=roles)

  @staticmethod
  def app():
    '''Returns a static file'''
    return render_template('page/app.html')

  @staticmethod
  def links_embed():
    '''Returns a small HTML file, inserted into the home page with some JS'''
    links = links_list(5, "false")
    len_l = len(links['entries'])
    return render_template('page/links_embed.html', links=links, len_l=len_l)

  @staticmethod
  def links():
    '''Displays links from an RSS feed (see function links_list(). )'''
    links = links_list(20, "true")
    len_links = len(links['entries'])
    return render_template('page/liens.html', links=links, len_links=len_links)

  @staticmethod
  def projects():
    '''Returns a static file'''
    return render_template('page/projects.html')

  @staticmethod
  @db_session
  def search(keyword, page):
    '''Search into articles'''
    if keyword is None:
      keyword = request.args.get('s', default="", type=str)
    if page == 0:
      page = request.args.get('page', default=0, type=int)

    if keyword != "":
      data = select(
        a for a in Articles if keyword in a.title
      ).order_by(desc(Articles.timestamp))[page * 10:page * 10 + 10]
      if data == []:
        erreur = "Votre recherche n'a donné aucun résultat. Vous pouvez entrer un autre mot clé :"
        return render_template('page/search.html', error=erreur)
      data_dict = []
      for item in data:
        data_dict.append(fill_informations(item))
      return render_template('blog/list.html', data=data_dict, template="search",
                             type="Recherche", keyword=keyword, page=page)

    else:
      return render_template('page/search.html')