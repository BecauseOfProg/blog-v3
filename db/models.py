from pony.orm import Required, PrimaryKey, Json
from db.db import db


class Articles(db.Entity):
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
