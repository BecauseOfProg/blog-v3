"""
    This is the file where the MySQL database credentials are defined.
    They are all stored in this `database` dict.
"""

database_config = {
    # This is the host of your database : it can be a URL or a IP address
    'host': 'localhost',

    # The port to connect to
    'port': 3306,

    # Select the database on which all the data will be saved
    'database': 'bop',

    # Authentication credentials : username and password
    'user': '',
    'password': ''
}
