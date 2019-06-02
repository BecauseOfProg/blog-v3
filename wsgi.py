from core.app import application
from core.database import db

from config import routes

if __name__ == '__main__':
  db.generate_mapping(create_tables=False)
  application.run()
