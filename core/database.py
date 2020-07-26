from pony.orm import Database
from config.database import database_config

"""
    This core part opens a connection to the MySQL database using Pony ORM.
    The connection information is stored in the config/database.py file.

    For more technical information, see Pony docs at https://docs.ponyorm.org/.
"""

db = Database()
db.bind(provider='mysql', host=database_config['host'], port=database_config['port'],
        user=database_config['user'], passwd=database_config['password'], db=database_config['database'])
