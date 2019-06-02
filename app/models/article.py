from pony.orm import Required, PrimaryKey, Json
from core.database import db

'''This is the model of a blog article. It matches the `articles` table in the database.'''

class Articles(db.Entity):
  url = PrimaryKey(str)
  title = Required(str)
  timestamp = Required(float)
  author = Required(str)
  art_type = Required(str, column="type")
  category = Required(str)
  description = Required(str, column="desc")
  labels = Required(Json)
  banner = Required(str)
  content = Required(str, max_len=50000)
  article_language = Required(str)

  _table_ = "articles"