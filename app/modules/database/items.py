import uuid

from modules.api import api
from modules.database import database


def add_item(label, description, attribution, logo):
    try:

        item_id = str(uuid.uuid4())
        database.server[database.DATA_DB_NAME][item_id] = {"_id": item_id,
                                                           "proto": "item",
                                                           "owner": "master",
                                                           "read": [],
                                                           "annotate": [],
                                                           "edit": [],
                                                           "images": [],
                                                           "meta": {
                                                               "attribution": attribution,
                                                               "logo": logo,
                                                               "label": label,
                                                               "description": description,
                                                           },
                                                           "metadata":[],
                                                           "thumbnail": ""
                                                           }
        print("Added item to database")

        # TODO create data-folder
        return database.server[database.DATA_DB_NAME][item_id]
    except Exception as e:
        print("Could not add item" + str(e))
        return None


def get_item(item_id):
    try:
        data = database.server[database.DATA_DB_NAME][item_id]
        if "proto" in data:
            if data["proto"] == "item":
                del data["_rev"]
                return data
        print("Could not get item " + item_id + ": Document type not item")
        return None

    except Exception as e:
        print("Could not get item " + item_id + ": " + str(e))
        return None


def get_items():
    # TODO replace with CouchDB view
    items = []
    for item in database.server[database.DATA_DB_NAME]:
        data = database.server[database.DATA_DB_NAME][item]
        if data["proto"] == "item":
            items.append(data)
    return items


def remove_item(item_id):
    try:
        data = database.server[database.DATA_DB_NAME][item_id]
        if data:
            if "proto" in data:
                if data["proto"] == "item":
                    #TODO delete images and files
                    del database.server[database.DATA_DB_NAME][item_id]
                    print("Removed item " + item_id + " from database")
                    return True
    except Exception as e:
        print("Could not remove item " + item_id + ": " + str(e))
        return False
    pass


def update_metadata(item_id, metadata):
    data = database.server[database.DATA_DB_NAME][item_id]
    if data:
        if "proto" in data:
            if data["proto"] == "item":
                data["meta"] = metadata
                database.server[database.DATA_DB_NAME][item_id] = data
                return database.server[database.DATA_DB_NAME][item_id]
    return None


def add_image_to_item(item_id, image_id):
    data = database.server[database.DATA_DB_NAME][item_id]
    if data:
        if "proto" in data:
            if data["proto"] == "item":
                if image_id not in data["images"]:
                    data["images"].append(image_id)
                    database.server[database.DATA_DB_NAME][item_id] = data
                    return database.server[database.DATA_DB_NAME][item_id]
                # TODO else:
    return None
