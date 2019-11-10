from flask import render_template, send_from_directory
from pony.orm import db_session, desc
from app.models.article import Articles


class MiscController:
  @staticmethod
  def get_pwa():
    '''Returns the PWA JavaScript file (must be at the root to work)'''
    print("hey")
    return send_from_directory('../resources/static', 'pwabuilder-sw.js')

  @staticmethod
  @db_session
  def get_rss():
    '''Generates the RSS feed'''
    articles = Articles.select().order_by(desc(Articles.timestamp))
    return render_template('components/flux.xml', articles=articles)

  @staticmethod
  @db_session
  def get_sitemap():
    '''Returns a sitemap with all articles (WIP)'''
    articles = Articles.select()
    return render_template('components/sitemap-articles.xml', articles=articles)
