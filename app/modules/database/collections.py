import uuid

from modules.api import api
from modules.database import database


def add_item(owner, label, description, attribution, logo):
    try:

        item_id = str(uuid.uuid4())
        database.server[database.DATA_DB_NAME][item_id] = {"_id": item_id,
                                                           "proto": "item",
                                                           "owner": owner,
                                                           "read": [],
                                                           "annotate": [],
                                                           "edit": [],
                                                           "images": {},
                                                           "metadata": {
                                                               "attribution": attribution,
                                                               "logo": logo,
                                                               "label": label,
                                                               "description": description,
                                                           },
                                                           "thumbnail": ""
                                                           }
        print("Added item to database")
        return get_item(item_id)
    except Exception as e:
        print("Could not add item" + str(e))
        return None


def get_item(item_id):
    try:
        data = database.server[database.DATA_DB_NAME][item_id]
        if "proto" in data:
            if data["proto"] == "item":
                del data["rev"]
                return data
        print("Could not get item " + item_id + ": Document type not item")
        return None

    except Exception as e:
        print("Could not get item " + item_id + ": " + str(e))
        return None


def remove_item(item_id):
    try:
        del database.server[database.DATA_DB_NAME][item_id]
        print("Removed item " + item_id + " from database")
        return True
    except Exception as e:
        print("Could not remove item " + item_id + ": " + str(e))
        return False
    pass


def update_metadata(item_id, metadata):
    pass


def get_collections():
    # TODO replace with CouchDB view
    collections = []
    for item in database.server[database.DATA_DB_NAME]:
        data = database.server[database.DATA_DB_NAME][item]
        if data["proto"] == "collection":
            collections.append(data)
    return collections


def get_collection(collection_id):
    data = database.server[database.DATA_DB_NAME][collection_id]
    if "proto" in data:
        if data["proto"] == "collection":
            return data
    return None


def add_collection(label, description, attribution, logo):
    data_id = str(uuid.uuid4())
    data = {
        "_id": data_id,
        "proto": "collection",
        "owner": "master",
        "items": [],
        "meta": {
            "attribution": attribution,
            "logo": logo,
            "label": label,
            "description": description
        }
    }
    database.server[database.DATA_DB_NAME][data_id] = data
    return database.server[database.DATA_DB_NAME][data_id]


def remove_collection(collection_id):
    """remove a collection from the database,return True on success"""
    try:
        data = database.server[database.DATA_DB_NAME][collection_id]
        if data:
            if "proto" in data:
                if data["proto"] == "collection":
                    del database.server[database.DATA_DB_NAME][collection_id]
                    print("Removed collection " + collection_id + " from database")
                    return True
        print("Could not remove collection " + collection_id + " from database")
        return False
    except Exception as e:
        print("Could not remove collection " + collection_id + ": " + str(e))
        return False


def update_collection(collection_id, label, description, attribution, logo):
    data = database.server[database.DATA_DB_NAME][collection_id]
    if data:
        if "proto" in data:
            if data["proto"] == "collection":
                data["meta"]["label"] = label
                data["meta"]["description"] = description
                data["meta"]["attribution"] = attribution
                data["meta"]["logo"] = logo

                database.server[database.DATA_DB_NAME][collection_id] = data

                return database.server[database.DATA_DB_NAME][collection_id]
    return None
