from utils.fill_informations import fill_informations
from pony.orm import db_session, select, desc
from flask import render_template, request
from db.models import Articles, User
from app import application


@application.route("/page/search", defaults={'keyword': None, 'page': 0})
@application.route("/page/search/", defaults={'keyword': None, 'page': 0})
@application.route("/page/search/<keyword>", defaults={'page': 0})
@application.route("/page/search/<keyword>/", defaults={'page': 0})
@application.route("/page/search/<keyword>/<int:page>")
@db_session
def search(keyword, page):
    '''Search into articles'''
    if keyword is None:
        keyword = request.args.get('s', default="", type=str)
    if page == 0:
        page = request.args.get('page', default=0, type=int)

    if keyword != "":
        data = select(
            a for a in Articles if keyword in a.title
        ).order_by(desc(Articles.timestamp))[page*10:page*10+10]
        if data == []:
            erreur = "Votre recherche n'a donné aucun résultat. Vous pouvez entrer un autre mot clé :"
            return render_template('page/search.html', error=erreur)
        data_dict = []
        for item in data:
            data_dict.append(fill_informations(item))
        return render_template('blog/list.html', data=data_dict, template="search",
                               type="Recherche", keyword=keyword, page=page)

    else:
        return render_template('page/search.html')
