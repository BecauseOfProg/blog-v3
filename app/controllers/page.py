from pony.orm import db_session
from flask import render_template, request
from app.models.user import User
from app.controllers.blog import BlogController
from core.utils.links import links_list
import json

BLOGROLL = json.loads(open('resources/data/blogroll.json', 'r').read())
PROJECTS = json.loads(open('resources/data/projects.json', 'r', encoding='utf-8').read())


class PageController:
  @staticmethod
  @db_session
  def about():
    '''Displays the 'about' page with a list of the staff'''
    roles = {
      "POST_WRITE": "Membre",
      "BLOG_WRITE": "Rédacteur",
      "USER_WRITE": "Modérateur"
    }
    staff = User.select(lambda u: str(u.permissions) != '[]')[:]
    return render_template('page/about.html', staff=staff, roles=roles)

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
    return render_template('page/liens.html', links=links, len_links=len_links, blogroll=BLOGROLL)

  @staticmethod
  def projects():
    '''Returns a static file'''
    return render_template('page/projects.html', projects=PROJECTS)

  @staticmethod
  @db_session
  def search(keyword, page):
    '''Search into articles'''
    if keyword is None:
      keyword = request.args.get('s', default="", type=str)
    if page == 0:
      page = request.args.get('page', default=0, type=int)
    if keyword != "":
      return BlogController.show_search(keyword, page)
    else:
      return render_template('page/search.html')
