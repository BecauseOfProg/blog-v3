from core.database import db
from core.app import application

from config import routes
import shutil

import os
dir = "resources/static/js/"

with open(os.path.join("resources", "static", "build", "bundle.js"), "w") as outfile:
  for file in os.listdir(dir):
    if file.endswith( ".js" ):
      with open( os.path.join( dir, file ) ,"r") as fd:
        shutil.copyfileobj(fd, outfile)



if __name__ == '__main__':
  application.run(host='localhost', port=5001, debug=True)
