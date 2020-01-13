# -*- coding: utf-8 -*-
"""adapter for CouchDB"""
import time
import traceback
from datetime import datetime
import json
import uuid

from couchdb import Server
from modules.database import database, users
from modules.api import api
from modules import config

server = None
USER_DB_NAME = "zenetti_users"
DATA_DB_NAME = "zenetti_data"

database_names = [USER_DB_NAME]

database_url = "http://127.0.0.1:5984"

def initialize():
    """connect to couchDB"""
    try:
        database.server = Server(
            database_url)
        server.version_info()
        print("Connected to database-server " + str(database.server))
        for database_name in database_names:
            try:
                server[database_name]
            except Exception as e:
                try:
                    server.create(database_name)
                except Exception as e:
                    print( "Could not create database " + database_name + ": " + str(e))
        # check if master_user exists, else create document
        try:
            server[USER_DB_NAME][config.get_config()["master_username"]]
        except Exception as e:
            setup(config.get_config()["master_username"], config.get_config()["master_password"])

    except Exception as e:
        print("Could not connect to database-server: " + str(e))

def setup(master_username, master_password):
    """create master-user in database
        Args:
            master_username (string): username of system master-administrator
            master_password (string): password for the account
        Returns:
            bool: True on success
    """
    try:
        user = api.User(master_username, "", None)
        user.hash_password(master_password)
        server[USER_DB_NAME][master_username] = {"username": master_username, "password": user.password_hash, "name": "",
                                            "admin": True, "master": True, "change_password": False}
        print("Created master-user")
        return True

    except Exception as e:
        print("Could not create master-user" + str(e))
        return False

