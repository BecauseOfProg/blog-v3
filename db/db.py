from pony.orm import Database
import json

with open('config.json') as json_data:
    data = json.load(json_data)
    config = data["db"]
    json_data.close()

db = Database()
db.bind(provider=config["provider"], host=config["host"],
        user=config["user"], passwd=config["password"], db=config["database"])
