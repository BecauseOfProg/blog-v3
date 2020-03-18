import subprocess
import shutil
import os

dir = "resources/static/js/"

with open(os.path.join("resources", "static", "build", "bundle.js"), "w+") as outfile:
  for file in os.listdir(dir):
    if file.endswith( ".js" ):
      with open( os.path.join( dir, file ) ,"r") as fd:
        shutil.copyfileobj(fd, outfile)

subprocess.call(["node_modules/stylus/bin/stylus",
                 "resources/static/css/index.styl", "-o",
                 "resources/static/build/bundle.css", "-c"])
