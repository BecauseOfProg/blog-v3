from datetime import datetime
from db.models import User

'''This file contains the function fill_informations'''


def fill_informations(post):
    '''Returns a dictionnary with all the usefull info about a given article'''
    response = {
        "timestamp": datetime.fromtimestamp(post.timestamp),
        "title": post.title,
        "url": post.url,
        "type": post.art_type,
        "category": post.category,
        "author": post.author,
        "displayname": User[post.author].displayname,
        "avatar": User[post.author].avatar,
        "banner": post.banner,
        "desc": post.desc
    }
    return response
