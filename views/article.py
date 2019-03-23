from db.models import Articles, User
from flask import render_template
from pony.orm import db_session
from app import application
from flask import Markup
import requests
import markdown


@application.route("/article/<url>")
@db_session
def article(url):
    '''Displays an article'''
    try:
        a = Articles.get(url=url)
        u = User.get(username=a.author)

        r = requests.get('https://api.becauseofprog.fr/v1/posts/last')
        devblog = r.json()

        if a.article_language == "markdown":
            htmlarticle = Markup(markdown.markdown(a.content,
                                                   extensions=['extra']))
        return render_template('article.html', **locals())
    except:
        return render_template('components/erreur.html',
                               erreur="La page recherchée n'existe pas! (404)"), 404
