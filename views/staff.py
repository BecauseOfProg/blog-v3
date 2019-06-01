from flask import render_template, request, redirect
from pony.orm import db_session, commit
from core.utils.checklogin import checklogin
from config.models import Articles
import time

class StaffController:
  @staticmethod
  @db_session
  def new_post():
    '''Checks if user is allowed to access the new post page'''
    u = checklogin()
    if u is not False:
      return StaffController.create_post(u)
    else:
      return redirect('/login')

  @staticmethod
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
          description=request.form['description'],
          url=request.form['url'],
          banner=request.form['banner'],
          timestamp=time.time(),
          author=username,
          content=request.form['md-editor'],
          article_language="markdown"
        )
        commit()
        return redirect('/article/' + request.form['url'])
      return render_template('members/new-article.html')

    erreur = "Vous n'avez pas la permission de visiter cette page (403)"
    return render_template('components/erreur.html', erreur=erreur), 403