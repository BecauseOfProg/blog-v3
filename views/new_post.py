from flask import render_template, request, session, redirect, url_for
from pony.orm import db_session, commit
from utils.checklogin import checklogin
from db.models import Articles, User
from app import application
import time


@application.route('/new-post', methods=['GET', 'POST'])
@db_session
def new_post():
    u = checklogin()
    if u is not False:
        return create_post(u)
    else:
        return redirect('/login')


def create_post(u):
    perms = str(u.permissions)
    username = str(u.username)
    if perms.find("BLOG_WRITE") != -1:
        if request.method == 'POST':
            # Un utilisateur autorisé souhaite poster un article
            # On envoie les données à MySQL
            a = Articles(
                title=request.form['title'],
                art_type=request.form['type'],
                category=request.form['category'],
                desc=request.form['desc'],
                url=request.form['url'],
                banner=request.form['banner'],
                timestamp=time.time(),
                author=username,
                content=request.form['md-editor'],
                article_language="markdown"
            )
            commit()
            return redirect('/article/'+request.form['url'])
        return render_template('members/new-article.html')
    return render_template('components/erreur.html', erreur="Vous n'avez pas la permission de visiter cette page (403)"), 403
