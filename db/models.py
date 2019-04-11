from pony.orm import Required, PrimaryKey, Json
from db.db import db

'''This files contains classes entities derived from the Database.
Entity attribute of the Database object. It means that they are not ordinary
classes, but entities. The entity instances are stored in the database,
which is bound to the db variable.
'''


class Articles(db.Entity):
    '''This is the entity Articles, matching table "articles" of the database.
    It contains all the attributes related to MySQL columns.'''
    title = Required(str)
    art_type = Required(str, column="type")
    category = Required(str)
    desc = Required(str)
    url = PrimaryKey(str)
    banner = Required(str)
    timestamp = Required(float)
    author = Required(str)
    content = Required(str, max_len=50000)
    article_language = Required(str)

    _table_ = "articles"


class User(db.Entity):
    '''This is the entity User, matching table "users" of the database.
    It contains all the attributes related to MySQL columns.'''
    username = PrimaryKey(str)
    displayname = Required(str)
    avatar = Required(str, column='picture')
    socials = Required(Json)
    permissions = Required(Json)
    token = Required(str)
    validate = Required(int)
    description = Required(str)
    grade = Required(str)
    email = Required(str)
    password_type = Required(str)
    hashed = Required(str, column="password")

    _table_ = "users"

db.generate_mapping(create_tables=False)
