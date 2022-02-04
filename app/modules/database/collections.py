import uuid

from modules.api import api
from modules.database import database


def get_collections():
    collections = []
    for item in database.get_index(database.COLLECTIONS_DB_NAME):
        data = database.load_item(database.COLLECTIONS_DB_NAME, item)

        collections.append(data)
    return collections


def get_collection(collection_id):
    data = database.load_item(database.COLLECTIONS_DB_NAME, collection_id)
    if "proto" in data:
        if data["proto"] == "collection":
            return data
    return None


def add_collection(label, description, attribution, logo, username):
    data_id = str(uuid.uuid4())
    data = {
        "_id": data_id,
        "proto": "collection",
        "owner": username,
        "items": [],
        "meta": {
            "attribution": attribution,
            "logo": logo,
            "label": label,
            "description": description
        }
    }
    database.store_item(database.COLLECTIONS_DB_NAME, data_id, data)
    return database.load_item(database.COLLECTIONS_DB_NAME, data_id)


def remove_collection(collection_id):
    """remove a collection from the database,return True on success"""
    try:
        data = database.load_item(database.COLLECTIONS_DB_NAME, collection_id)
        if data:
            if "proto" in data:
                if data["proto"] == "collection":
                    database.remove_item(database.COLLECTIONS_DB_NAME, collection_id)
                    print("Removed collection " + collection_id + " from database")
                    return True
        print("Could not remove collection " + collection_id + " from database")
        return False
    except Exception as e:
        print("Could not remove collection " + collection_id + ": " + str(e))
        return False


def update_collection(collection_id, label, description, attribution, logo):
    data = database.load_item(database.COLLECTIONS_DB_NAME, collection_id)
    if data:
        if "proto" in data:
            if data["proto"] == "collection":
                data["meta"]["label"] = label
                data["meta"]["description"] = description
                data["meta"]["attribution"] = attribution
                data["meta"]["logo"] = logo

                database.update_item(database.COLLECTIONS_DB_NAME, collection_id, data)

                return database.load_item(database.COLLECTIONS_DB_NAME, collection_id)
    return None


def add_item_to_collection(collection_id, item_id):
    data = database.load_item(database.COLLECTIONS_DB_NAME, collection_id)
    if data:
        if "proto" in data:
            if data["proto"] == "collection":
                data["items"].append(item_id)
                database.update_item(database.COLLECTIONS_DB_NAME, collection_id, data)
                return True
    return False


def remove_item_from_collection(collection_id, item_id):
    data = database.load_item(database.COLLECTIONS_DB_NAME, collection_id)
    if data:
        if "proto" in data:
            if data["proto"] == "collection":
                del data["items"][data["items"].index(item_id)]
                database.update_item(database.COLLECTIONS_DB_NAME, collection_id, data)
                return True
    return False
