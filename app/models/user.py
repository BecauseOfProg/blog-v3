from pony.orm import Required, Optional, PrimaryKey, Json
from core.database import db

'''This is the model of a registered user, with all its informations. It matches the `users` table in the database.'''

class User(db.Entity):
  username = PrimaryKey(str)
  displayname = Required(str)
  email = Required(str)
  hashed = Required(str, column="password")
  password_type = Required(str)
  permissions = Required(Json)
  token = Required(str)
  timestamp = Required(float)
  avatar = Required(str, column='picture')
  description = Optional(str)
  biography = Optional(str)
  location = Optional(str)
  socials = Required(Json)
  is_email_public = Required(bool)

  _table_ = "users"