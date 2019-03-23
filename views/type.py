from utils.fill_informations import fill_informations
from pony.orm import db_session, select, desc
from db.models import Articles, User
from flask import render_template
from app import application
import json


@application.route("/type/<article_type>/<int:page>")
@application.route("/type/<article_type>", defaults={'page': 0})
@application.route("/type/<article_type>/", defaults={'page': 0})
@db_session
def show_type(article_type, page):
    try:
        with open('static/data.json') as json_data:
            data = json.load(json_data)
            icon = data["types"][article_type]
            json_data.close()
    except:
        return render_template('components/erreur.html',
                               erreur="Le type entré est invalide !")

    data = select(a for a in Articles if article_type in a.art_type).order_by(desc(Articles.timestamp))[page*10:page*10+10]
    if data == []:
        return render_template('components/erreur.html',
                               erreur="La page recherchée n'existe pas! (404)"), 404
    data_dict = []
    for item in data:
        data_dict.append(fill_informations(item))
    return render_template('list.html', template="type", type=article_type,
                           data=data_dict, icon=icon, page=page)
