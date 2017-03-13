from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from config import DATABASE_NAME, MONGO_SERVER, MONGO_PORT


def connect_database(server=MONGO_SERVER, port=MONGO_PORT, database_name=DATABASE_NAME):
    """ Create a bound connection with mongo database. """
    db_connection = None
    try:
        connectivity = MongoClient(server, port)
        db_connection = connectivity[database_name]

        # test connectivity
        connectivity.server_info()
    except ServerSelectionTimeoutError as exp:
        print "Server timeout, no connection on specify location: %r" % exp
    return db_connection


def add_message(db_connection, message):
    """ Insert new message in database. """

    if not db_connection:
        db_connection = connect_database()
    ack = False
    try:
        if message:
            db_connection.items.insert_many(message)
            ack = True
    except AttributeError as exp:
        print "We could not insert the message: %r" % exp
    return ack
