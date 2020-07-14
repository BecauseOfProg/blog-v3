from flask import render_template, request, jsonify
from pony.orm import db_session, desc
import json
import feedparser

from core.exceptions import NoArticlesFound
from core.utils.fill_informations import fill_informations
from core.utils.links import links_list

from core.data.blogroll import blogroll
from core.data.projects import projects
from core.data.embeds import embeds

from app.models.article import Articles
from app.models.user import User
from app.controllers.blog import BlogController


class PageController:
    @staticmethod
    @db_session
    def about():
        """
            Displays the "about" page with a list of the staff
        """
        roles = {
            "POST_WRITE": "Membre",
            "BLOG_WRITE": "Rédacteur",
            "USER_WRITE": "Modérateur"
        }
        staff = User.select(lambda u: str(u.permissions) != '[]')[:]
        return render_template('page/about.html', staff=staff, roles=roles)

    @staticmethod
    def app():
        """
            Returns a static file
        """
        return render_template('page/app.html')

    @staticmethod
    def rss_embed(source):
        """
            Returns a small HTML file, inserted into the home page with some JS. Source parameter can be links,
            Twitter, Mastodon, Instagram
        """
        params = embeds[source]
        feed = links_list(params["source"], 8, "false")

        return render_template('page/links_embed.html',
                               links=feed, params=params)

    @staticmethod
    def js_embed():
        """
            Returns json data
        """
        rss_urls = []
        for source in embeds:
            rss_urls.append(embeds[source]["source"])

        posts = []
        for url in rss_urls:
            posts.extend(feedparser.parse(url).entries)

        return jsonify(
            sorted(posts, key=lambda i: i.published_parsed, reverse=True))

    @staticmethod
    def links():
        """
            Displays links from an RSS feed (see function links_list())
        """
        links = links_list("links", 20, "true")
        links_number = len(links['entries'])
        return render_template(
            'page/liens.html', links=links, links_number=links_number, blogroll=blogroll)

    @staticmethod
    def projects():
        """
            Returns a static file
        """
        return render_template('page/projects.html', projects=projects)

    @staticmethod
    @db_session
    def show_search(keyword, page):
        """
            Search into articles
        """
        if keyword is None:
            keyword = request.args.get('q', default="", type=str)
        if page == 0:
            page = request.args.get('page', default=0, type=int)
        if keyword != "":
            return PageController.process_search(keyword, page)
        else:
            lasts = Articles.get_articles_in_range(0, 3)
            return render_template(
                'page/search.html',
                lasts=lasts
            )

    @staticmethod
    def process_search(keyword, page):
        """
            Process the search when a keyword is given
        """
        try:
            articles, total_articles = Articles.search_articles(keyword, page)
        except NoArticlesFound:
            error = "Votre recherche n'a donné aucun résultat. Vous pouvez entrer un autre mot clé :"
            lasts = Articles.get_articles_in_range(0, 3)
            return render_template(
                'page/search.html', error=error, lasts=lasts)
        return render_template('blog/list.html',
                               articles=articles,
                               total_articles=total_articles,
                               template="site",
                               type="Recherche",
                               name="Recherche",
                               icon="magnify",
                               keyword=keyword,
                               page=page)
