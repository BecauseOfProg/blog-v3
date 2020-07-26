import subprocess
import shutil
import os
import platform

js_dir = "resources/static/js/"

with open(os.path.join("resources", "static", "build", "bundle.js"), "w+") as outfile:
    for file in os.listdir(js_dir):
        if file.endswith(".js"):
            with open(os.path.join(js_dir, file), "r") as fd:
                shutil.copyfileobj(fd, outfile)

stylus_exe = "stylus.cmd" if platform.system() == "Windows" else "stylus"
stylus_bin = os.path.join("node_modules", ".bin", stylus_exe)

subprocess.call([stylus_bin,
                 "resources/static/css/index.styl", "-o",
                 "resources/static/build/bundle.css", "-c"])
