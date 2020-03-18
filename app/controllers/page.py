from pony.orm import db_session, desc
from flask import render_template, request, jsonify
from core.exceptions import NoArticlesFound
from core.utils.fill_informations import fill_informations
from core.utils.links import links_list
from app.models.article import Articles
from app.models.user import User
from app.controllers.blog import BlogController
import json

import feedparser

BLOGROLL = json.loads(open('resources/data/blogroll.json', 'r').read())
PROJECTS = json.loads(open('resources/data/projects.json', 'r', encoding='utf-8').read())

TYPES = json.loads(open('resources/data/types.json', 'r').read())
CATEGORIES = json.loads(open('resources/data/categories.json', 'r', encoding="utf-8").read())

EMBED_PARAMS = json.loads(open('resources/data/embeds.json', 'r', encoding='utf-8').read())


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
  def rss_embed(source):
    '''Returns a small HTML file, inserted into the home page with some JS. Source parameter can be links, twitter, mastodon, instagram'''
    params = EMBED_PARAMS[source]
    feed = links_list(params["source"], 8, "false")
    len_l = len(feed['entries'])

    return render_template('page/links_embed.html', links=feed, len_l=len_l, params=params)

  @staticmethod
  def js_embed():
    '''Returns json data'''
    RSS_URLS = []
    for source in EMBED_PARAMS:
      RSS_URLS.append(EMBED_PARAMS[source]["source"])

    posts = []
    for url in RSS_URLS:
      posts.extend(feedparser.parse(url).entries)

    return jsonify(sorted(posts, key = lambda i: i.published_parsed, reverse = True))

  @staticmethod
  def links():
    '''Displays links from an RSS feed (see function links_list(). )'''
    links = links_list("links", 20, "true")
    len_links = len(links['entries'])
    return render_template('page/liens.html', links=links, len_links=len_links, blogroll=BLOGROLL)

  @staticmethod
  def projects():
    '''Returns a static file'''
    return render_template('page/projects.html', projects=PROJECTS)

  @staticmethod
  @db_session
  def show_search(keyword, page):
    '''Search into articles'''
    if keyword is None:
      keyword = request.args.get('q', default="", type=str)
    if page == 0:
      page = request.args.get('page', default=0, type=int)
    if keyword != "":
      return PageController.process_search(keyword, page)
    else:
      lasts = Articles.get_articles_in_range(0, 3)
      return render_template('page/search.html', categories=CATEGORIES, types=TYPES, lasts=lasts)

  @staticmethod
  def process_search(keyword, page):
    '''Process the search when a keyword is given'''
    try:
      articles = Articles.search_articles(keyword, page)
    except NoArticlesFound:
      erreur = "Votre recherche n'a donné aucun résultat. Vous pouvez entrer un autre mot clé :"
      lasts = Articles.get_articles_in_range(0, 3)
      return render_template('page/search.html', error=erreur, categories=CATEGORIES, types=TYPES, lasts=lasts)
    return render_template('blog/list.html', articles=articles, template="site",
                           type="Recherche", name="Recherche", icon="magnify", keyword=keyword, page=page,
                           types=TYPES, categories=CATEGORIES, devblog=BlogController.get_devblog())
