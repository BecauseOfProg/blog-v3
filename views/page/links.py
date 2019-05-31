from utils.links import links_list
from flask import render_template
from app import application


@application.route("/page/links")
def links():
    '''Displays links from an RSS feed (see function links_list(). )'''
    links = links_list(20, "true")
    len_links = len(links['entries'])
    return render_template('page/liens.html', links=links, len_links=len_links)


@application.route("/page/links-embed")
def links_embed():
    '''Returns a small HTML file, inserted into the home page with some JS'''
    links = links_list(5, "false")
    len_l = len(links['entries'])
    return render_template('page/links_embed.html', links=links, len_l=len_l)
