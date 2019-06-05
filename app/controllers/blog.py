from core.utils.fill_informations import fill_informations
from pony.orm import db_session, select, desc
from app.models.article import Articles
from app.models.user import User
from flask import render_template
from flask import Markup
import requests
import markdown
import json

TYPES = json.loads(open('resources/data/types.json', 'r').read())
CATEGORIES = json.loads(open('resources/data/categories.json', 'r', encoding="utf-8").read())


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

    devblog = requests.get('https://api.becauseofprog.fr/v1/posts/last').json()
    return render_template('blog/home.html', last=last, lasts=list_of_dict, types=TYPES, categories=CATEGORIES,
                           devblog=devblog)

  @staticmethod
  @db_session
  def show_blog(page):
    '''Displays list.html with the lasts articles'''
    devblog = requests.get('https://api.becauseofprog.fr/v1/posts/last').json()['post']

    data = select(a for a in Articles).order_by(desc(Articles.timestamp))[
           page * 10: page * 10 + 10
           ]
    if data == []:
      erreur = "La page recherchée n'existe pas! (404)"
      return render_template('components/erreur.html', erreur=erreur), 404
    articles = []
    for item in data:
      articles.append(fill_informations(item))
    return render_template('blog/list.html', template="Blog", type='Tous les articles', name='Tous les articles',
                           articles=articles, icon="description", page=page, types=TYPES, categories=CATEGORIES,
                           devblog=devblog)

  @staticmethod
  @db_session
  def show_category(category, page):
    '''Displays list.html with the lasts articles of a given category.
    Returns an error if the page is empty or if category does not exists.'''
    if category not in CATEGORIES:
      return render_template('components/erreur.html',
                             erreur="La catégorie souhaitée est invalide !")

    category_data = CATEGORIES[category]

    devblog = requests.get('https://api.becauseofprog.fr/v1/posts/last').json()['post']

    data = Articles.select(lambda a: a.category == category).order_by(desc(Articles.timestamp))[
           page * 10: page * 10 + 10]

    articles = []
    for item in data:
      articles.append(fill_informations(item))

    return render_template('blog/list.html', template="Catégorie", type=category, name=category_data['name'],
                           icon=category_data['icon'], articles=articles, page=page, types=TYPES,
                           categories=CATEGORIES, devblog=devblog)

  @staticmethod
  @db_session
  def show_type(type, page):
    '''Displays list.html with the lasts articles of a given type.
        Returns an error if the page is empty or if type does not exists.'''
    if type not in TYPES:
      return render_template('components/erreur.html',
                             erreur="Le type souhaité est invalide !")

    type_data = TYPES[type]

    devblog = requests.get('https://api.becauseofprog.fr/v1/posts/last').json()['post']

    data = Articles.select(lambda a: a.type == type).order_by(desc(Articles.timestamp))[page * 10:page * 10 + 10]

    articles = []
    for item in data:
      articles.append(fill_informations(item))
    return render_template('blog/list.html', template="type", type=type, icon=type_data['icon'], name=type_data['name'],
                           articles=articles, page=page, types=TYPES, categories=CATEGORIES, devblog=devblog)

  @staticmethod
  @db_session
  def show_article(url):
    '''Displays an article with a given url'''
    try:
      article = Articles.get(url=url)
      author = User.get(username=article.author)

      devblog = requests.get('https://api.becauseofprog.fr/v1/posts/last').json()['post']

      if article.article_language == "markdown":
        htmlarticle = Markup(markdown.markdown(article.content, extensions=['extra']))
      else:
        htmlarticle = ''
      return render_template('blog/article.html', devblog=devblog, article=article, author=author,
                             htmlarticle=htmlarticle, categories=CATEGORIES, types=TYPES)
    except Exception as e:
      print(e)
      erreur = "La page recherchée n'existe pas! (404)"
      return render_template('components/erreur.html',
                             erreur=erreur), 404
