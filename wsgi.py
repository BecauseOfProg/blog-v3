from core.database import db
from core.app import application

from config import routes
from config import bundler

if __name__ == '__main__':
    db.generate_mapping(create_tables=False)
    application.run()
