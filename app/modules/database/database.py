# -*- coding: utf-8 -*-
"""adapter for CouchDB"""
import os
import time
import traceback
from datetime import datetime
import json
import uuid

from couchdb import Server
from modules.database import database, users
from modules.api import api
from modules import config

#server = None
USER_DB_NAME = "zenetti_users"
COLLECTIONS_DB_NAME = "zenetti_collections"
ITEMS_DB_NAME = "zenetti_items"
IMAGES_DB_NAME = "zenetti_images"


database_names = [USER_DB_NAME, COLLECTIONS_DB_NAME,ITEMS_DB_NAME, IMAGES_DB_NAME]

#database_url = "http://127.0.0.1:5984"

#DATA_PATH = ""


def initialize():
    """connect to couchDB"""
    try:
        #database.server = Server(
        #    database_url)
        #server.version_info()
        #print("Connected to database-server " + str(database.server))

        for database_name in database_names:
            if os.path.isdir(os.path.join("webapp/data/database/" + database_name)):
                pass
            else:
                try:
                    os.mkdir(os.path.join("webapp/data/database/" + database_name))
                except Exception as e:
                    print("Could not create database " + database_name + ": " + str(e))
        # check if master_user exists, else create document
        try:
            load_item(USER_DB_NAME, config.get_config(), "master_username")
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

        store_item(USER_DB_NAME, master_username, {"username": master_username, "password": user.password_hash,
                                                   "name": "",
                                                   "admin": True, "master": True, "change_password": False})
        print("Created master-user")
        return True

    except Exception as e:
        print("Could not create master-user" + str(e))
        return False


def store_item(database, item_id, data):
    if os.path.isfile(os.path.join("webapp/data/database/" + database + "/" + item_id + ".json")):
        raise Exception("Item exists")
    else:
        with open(os.path.join("webapp/data/database/" + database + "/" + item_id + ".json"), "w",
                  encoding="utf8") as json_file:
            json.dump(data, json_file)


def load_item(database, item_id):
    with open(os.path.join("webapp/data/database/" + database + "/" + item_id + ".json"), "r",
              encoding="utf8") as json_file:
        data = json.load(json_file)
        return data


def update_item(database, item_id, data):
    if os.path.isfile(os.path.join("webapp/data/database/" + database + "/" + item_id + ".json")):
        with open(os.path.join("webapp/data/database/" + database + "/" + item_id + ".json"), "w",
                  encoding="utf8") as json_file:
            json.dump(data, json_file)
    else:
        raise Exception("Item does not exist")


def remove_item(database, item_id):
    os.remove(os.path.join("webapp/data/database/" + database + "/" + item_id + ".json"))


def get_index(database):
    file_list = os.scandir(os.path.join("webapp/data/database/" + database))
    items = []
    for f in file_list:
        filename = f.name
        if filename != ".." and filename != ".":
            items.append(filename.replace(".json", ""))
    return items
