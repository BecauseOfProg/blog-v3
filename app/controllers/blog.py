from flask import render_template
from flask import Markup
from pony.orm import db_session, select, desc, count
import requests
import markdown
import json

from core.utils.fill_informations import fill_informations
from core.data.categories import categories
from core.data.types import types
from core.data.socials import socials

from app.models.article import Articles
from app.models.user import User


class BlogController:
    @staticmethod
    @db_session
    def show_home():
        """
          Homepage of the blog
        """
        last = Articles.select().order_by(desc(Articles.timestamp)).first()
        lasts_art = Articles.select().order_by(desc(Articles.timestamp))[1:4]
        list_of_dict = []
        for item in lasts_art:
            list_of_dict.append(fill_informations(item))
        return render_template('blog/home.html',
                               last=last,
                               lasts=list_of_dict,
                               socials=socials)

    @staticmethod
    @db_session
    def show_blog(page):
        """
          Displays the list page with lasts articles
        """
        data = select(a for a in Articles).order_by(desc(Articles.timestamp))[
            page * 10: page * 10 + 10
        ]
        if not data:
            error = "La page recherchée n'existe pas! (404)"
            return render_template(
                'components/erreur.html', erreur=error), 404
        articles = []
        for item in data:
            articles.append(fill_informations(item))
        return render_template('blog/list.html',
                               template="Blog",
                               type='Tous les articles',
                               name='Tous les articles',
                               articles=articles,
                               total_articles=count(a for a in Articles),
                               icon="file-document-box-multiple-outline",
                               page=page)

    @staticmethod
    @db_session
    def show_category(category, page):
        """
          Displays the list page with the lasts articles of a given category.
          Returns an error if the page is empty or if category doesn't exists.
        """
        if category not in categories:
            return render_template(
                'components/erreur.html',
                erreur="La catégorie souhaitée est invalide !")

        category_data = categories[category]
        data = Articles.select(
            lambda a: a.category == category).order_by(
            desc(
                Articles.timestamp))[
                page *
                10: page *
                10 +
            10]

        articles = []
        for item in data:
            articles.append(fill_informations(item))

        return render_template('blog/list.html',
                               template="Catégorie",
                               type=category,
                               name=category_data['name'],
                               icon=category_data['icon'],
                               articles=articles,
                               total_articles=count(
                                   a for a in Articles if a.category == category),
                               page=page)

    @staticmethod
    @db_session
    def show_type(type, page):
        """
          Displays list.html with the lasts articles of a given type.
          Returns an error if the page is empty or if type doesn't exists.
        """
        if type not in types:
            return render_template('components/erreur.html',
                                   erreur="Le type souhaité est invalide !")

        type_data = types[type]

        data = Articles.select(
            lambda a: a.type == type).order_by(
            desc(
                Articles.timestamp))[
                page *
                10:page *
                10 +
            10]

        articles = []
        for item in data:
            articles.append(fill_informations(item))
        return render_template('blog/list.html',
                               template="type",
                               type=type,
                               icon=type_data['icon'],
                               name=type_data['name'],
                               articles=articles,
                               total_articles=count(
                                   a for a in Articles if a.type == type),
                               page=page)

    @staticmethod
    @db_session
    def show_article(url):
        """
          Displays an article using a given URL
        """
        try:
            article = Articles.get(url=url)
            author = User.get(username=article.author)

            if article.article_language == "markdown":
                htmlarticle = Markup(
                    markdown.markdown(
                        article.content,
                        extensions=['extra']))
            else:
                htmlarticle = ''
            return render_template('blog/article.html',
                                   article=article,
                                   author=author,
                                   htmlarticle=htmlarticle)
        except Exception as e:
            print(e)
            error = "La page recherchée n'existe pas! (404)"
            return render_template('components/erreur.html',
                                   erreur=error), 404
