from flask import render_template, send_from_directory
from utils.fill_informations import fill_informations
from pony.orm import db_session, select, desc
from db.models import Articles
from app import application
import os


@application.errorhandler(404)
def page_not_found(error):
    return render_template('components/erreur.html',
                           erreur="La page recherchée n'existe pas! (404)"), 404


@application.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@application.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@application.route('/pwabuilder-sw.js')
def ynh():
    return send_from_directory('static', 'pwabuilder-sw.js')


@application.route('/tout.rss')
@application.route('/blog.rss')
@db_session
def rss():
    data = select((a.title, a.desc, a.banner, a.url, a.author, a.timestamp) for a in Articles).order_by(-6)[:4]
    return render_template('components/flux.xml', data=data)


@application.route("/sitemap-articles.xml")
@db_session
def blog_sitemap():
    data = select((a.url, a.timestamp) for a in Articles)
    return render_template('components/sitemap-articles.xml', data=data)
