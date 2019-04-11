from pony.orm import Database
import json

'''This files opens a connection to our MySQL database using Pony ORM.
The credentials are sored in config.json file. db is the database object,
required by Pony. See Pony docs at https://docs.ponyorm.org/

'''

with open('config.json') as json_data:
    data = json.load(json_data)
    config = data["db"]
    json_data.close()

db = Database()
db.bind(provider=config["provider"], host=config["host"],
        user=config["user"], passwd=config["password"], db=config["database"])
