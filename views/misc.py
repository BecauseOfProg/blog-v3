from flask import render_template, send_from_directory
from utils.fill_informations import fill_informations
from pony.orm import db_session, select, desc
from db.models import Articles
from app import application
import os

'''Miscellaneous functions'''


@application.errorhandler(404)
def page_not_found(error):
    '''Returns the 404 error page'''
    erreur = "La page recherchée n'existe pas! (404)"
    return render_template('components/erreur.html',
                           erreur=erreur), 404


@application.route('/favicon.ico')
def favicon():
    '''Returns the favico file'''
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@application.route('/static/<path:path>')
def send_static(path):
    '''Returns the statics file (under subfolder statics/)'''
    return send_from_directory('static', path)


@application.route('/pwabuilder-sw.js')
def pwa():
    '''Returns the PWA JavaScript file (must be at the root to work'''
    return send_from_directory('static', 'pwabuilder-sw.js')


@application.route('/tout.rss')
@application.route('/blog.rss')
@db_session
def rss():
    '''Generates the RSS feed'''
    data = (
        select(
            (a.title, a.desc, a.banner, a.url, a.author, a.timestamp)
            for a in Articles).order_by(-6)[:4]
    )
    return render_template('components/flux.xml', data=data)


@application.route("/sitemap-articles.xml")
@db_session
def blog_sitemap():
    '''Returns a sitemap with all articles (WIP)'''
    data = select((a.url, a.timestamp) for a in Articles)
    return render_template('components/sitemap-articles.xml', data=data)
