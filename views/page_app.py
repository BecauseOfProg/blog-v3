from flask import render_template
from app import application


@application.route("/page/app")
def app():
    return render_template('page/app.html')
