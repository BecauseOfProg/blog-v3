from flask import render_template, request, redirect
from pony.orm import db_session, commit
from core.utils.checklogin import checklogin
from app.models.article import Articles
import time
import json

TYPES = json.loads(open('resources/data/types.json', 'r').read())
CATEGORIES = json.loads(
    open(
        'resources/data/categories.json',
        'r',
        encoding="utf-8").read())


class StaffController:
    @staticmethod
    @db_session
    def new_post():
        """
            Checks if user is allowed to access the new post page
        """
        user = checklogin()
        if user is not False:
            return StaffController.create_post(user)
        else:
            return redirect('/login')

    @staticmethod
    def create_post(user):
        permissions = str(user.permissions)
        username = str(user.username)
        if permissions.find("BLOG_WRITE") != -1:
            if request.method == 'POST':
                # An authorized user wants to submit a new article.
                # Send the data to MySQL
                article = Articles(
                    title=request.form['title'],
                    type=request.form['type'],
                    category=request.form['category'],
                    description=request.form['description'],
                    url=request.form['url'],
                    banner=request.form['banner'],
                    timestamp=time.time(),
                    author=username,
                    content=request.form['md-editor'],
                    labels=request.form['labels'].split(','),
                    article_language="markdown"
                )
                commit()
                return redirect('/article/' + request.form['url'])
            return render_template(
                'members/new-article.html', types=TYPES, categories=CATEGORIES)

        error = "Vous n'avez pas la permission de visiter cette page (403)"
        return render_template('components/erreur.html', erreur=error), 403
