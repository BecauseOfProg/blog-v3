from pony.orm import db_session, select
from db.models import User
from flask import render_template
from app import application


@application.route("/page/about")
@db_session
def about():
    '''Displays the 'about' page with a list of the staff'''
    stafflist = []
    roles = {
      "POST_WRITE": "Membre",
      "BLOG_WRITE": "Rédacteur",
      "USER_WRITE": "Modérateur"
    }
    staff = select(u for u in User if str(u.permissions) != '[]')[:]
    for user in staff:
        stafflist.append({
          'username': user.username,
          'displayname': user.displayname,
          'description': user.description,
          'avatar': user.avatar,
          'permissions': user.permissions
        })
    return render_template('page/about.html', staff=stafflist, roles=roles)
