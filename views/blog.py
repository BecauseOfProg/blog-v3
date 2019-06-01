from core.utils.fill_informations import fill_informations
from pony.orm import db_session, select, desc
from config.models import Articles, User
from flask import render_template
from flask import Markup
import requests
import markdown
import json


class BlogController:
  @staticmethod
  @db_session
  def show_home():
    '''Homepage of your blog-old'''
    last = (
      select(
        (a.title, a.description, a.banner, a.url, a.timestamp) for a in Articles)
        .order_by(-5)
        .first()
    )
    lasts_art = select(a for a in Articles).order_by(desc(Articles.timestamp))[1:4]
    list_of_dict = []
    for item in lasts_art:
      list_of_dict.append(fill_informations(item))

    r = requests.get('https://api.becauseofprog.fr/v1/posts/last')
    devblog = r.json()
    return render_template('blog/home.html', last=last, lasts=list_of_dict,
                           devblog=devblog)

  @staticmethod
  @db_session
  def show_blog(page):
    '''Displays list.html with the lasts articles'''
    data = select(a for a in Articles).order_by(desc(Articles.timestamp))[
           page * 10: page * 10 + 10
           ]
    if data == []:
      erreur = "La page recherchée n'existe pas! (404)"
      return render_template('components/erreur.html', erreur=erreur), 404
    data_dict = []
    for item in data:
      data_dict.append(fill_informations(item))
    return render_template('blog/list.html', template="Blog",
                           type="Tous les articles", data=data_dict,
                           icon="description", page=page)

  @staticmethod
  @db_session
  def show_category(category, page):
    '''Displays list.html with the lasts articles of a given category.
    Returns an error if the page is empty or if category does not exists.'''
    try:
      with open('static/data.json') as json_data:
        data = json.load(json_data)
        icon = data["categories"][category]
        json_data.close()
    except:
      return render_template('components/erreur.html',
                             erreur="La catégorie entrée est invalide !")

    data = select(a for a in Articles if category in a.category).order_by(
      desc(Articles.timestamp)
    )[page * 10: page * 10 + 10]

    if data == []:
      erreur = "La page recherchée n'existe pas! (404)"
      return render_template('components/erreur.html', erreur=erreur), 404
    data_dict = []
    for item in data:
      data_dict.append(fill_informations(item))

    return render_template('blog/list.html', template="Catégorie", type=category,
                           data=data_dict, icon=icon, page=page)

  @staticmethod
  @db_session
  def show_type(type, page):
    try:
      with open('static/data.json') as json_data:
        data = json.load(json_data)
        icon = data["types"][type]
        json_data.close()
    except:
      return render_template('components/erreur.html',
                             erreur="Le type entré est invalide !")

    data = select(
      a for a in Articles if type in a.art_type
    ).order_by(desc(Articles.timestamp))[page * 10:page * 10 + 10]
    if data == []:
      erreur = "La page recherchée n'existe pas! (404)"
      return render_template('components/erreur.html',
                             erreur=erreur), 404
    data_dict = []
    for item in data:
      data_dict.append(fill_informations(item))
    return render_template('blog/list.html', template="type", type=type,
                           data=data_dict, icon=icon, page=page)

  @staticmethod
  @db_session
  def show_article(url):
    '''Displays an article with a given url'''
    try:
      a = Articles.get(url=url)
      u = User.get(username=a.author)

      r = requests.get('https://api.becauseofprog.fr/v1/posts/last')
      devblog = r.json()

      if a.article_language == "markdown":
        htmlarticle = Markup(markdown.markdown(a.content,
                                               extensions=['extra']))
      return render_template('blog/article.html', **locals())
    except:
      erreur = "La page recherchée n'existe pas! (404)"
      return render_template('components/erreur.html',
                             erreur=erreur), 404
