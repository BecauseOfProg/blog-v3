from core.database import db
from core.app import application

from config import routes
from config import bundler

if __name__ == '__main__':
  application.run(host='localhost', port=5001, debug=True)
