from flask import render_template, send_from_directory, make_response
from pony.orm import db_session, desc
from app.models.article import Articles


class MiscController:
    @staticmethod
    def get_pwa():
        """
            Returns the PWA JavaScript file (must be at the root to work)
        """
        return send_from_directory('../resources/static', 'pwabuilder-sw.js')

    @staticmethod
    @db_session
    def get_rss():
        """
            Generates the RSS feed
        """
        articles = Articles.select().order_by(desc(Articles.timestamp))
        rss_xml = render_template('components/flux.xml', articles=articles)
        response = make_response(rss_xml)
        response.headers['Content-Type'] = 'application/xml'
        return response

    @staticmethod
    @db_session
    def get_sitemap():
        """
            Returns a sitemap with all articles (WIP)
        """
        articles = Articles.select()
        return render_template(
            'components/sitemap-articles.xml', articles=articles)
