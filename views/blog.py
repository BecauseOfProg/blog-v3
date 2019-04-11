from utils.fill_informations import fill_informations
from pony.orm import db_session, select, desc
from db.models import Articles, User
from flask import render_template
from app import application


@application.route("/blog/<int:page>")
@application.route("/blog", defaults={'page': 0})
@application.route("/blog/", defaults={'page': 0})
@db_session
def show_blog(page):
    '''Displays list.html with the lasts articles'''
    data = select(a for a in Articles).order_by(desc(Articles.timestamp))[
        page * 10: page * 10 + 10
    ]
    if data == []:
        erreur = "La page recherchée n'existe pas! (404)"
        return render_template('components/erreur.html', erreur=erreur), 404
    data_dict = []
    for item in data:
        data_dict.append(fill_informations(item))
    return render_template('list.html', template="Blog",
                           type="Tous les articles", data=data_dict,
                           icon="description", page=page)
