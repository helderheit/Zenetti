import os
import uuid

from modules.api import api
from modules.database import database


def add_item(label, description, attribution, logo, metadata, username):
    try:

        item_id = str(uuid.uuid4())
        database.store_item(database.ITEMS_DB_NAME, item_id, {"_id": item_id,
                                                           "proto": "item",
                                                           "owner": username,
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
                                                           "metadata":metadata,
                                                           "thumbnail": ""
                                                           })
        print("Added item to database")

        return database.load_item(database.ITEMS_DB_NAME, item_id)
    except Exception as e:
        print("Could not add item" + str(e))
        return None


def get_item(item_id):
    try:
        data = database.load_item(database.ITEMS_DB_NAME, item_id)
        if "proto" in data:
            if data["proto"] == "item":
                return data
        print("Could not get item " + item_id + ": Document type not item")
        return None

    except Exception as e:
        print("Could not get item " + item_id + ": " + str(e))
        return None


def get_items():
    items = []
    for item in database.get_index(database.ITEMS_DB_NAME):
        data = database.load_item(database.ITEMS_DB_NAME, item)
        if data["proto"] == "item":
            items.append(data)
    return items


def remove_item(item_id):
    try:
        data = database.load_item(database.ITEMS_DB_NAME, item_id)
        if data:
            if "proto" in data:
                if data["proto"] == "item":

                    database.remove_item(database.ITEMS_DB_NAME, item_id)

                    print("Removed item " + item_id + " from database")
                    return True
    except Exception as e:
        print("Could not remove item " + item_id + ": " + str(e))
        return False
    pass


def update_metadata(item_id, attributes, metadata):
    data = database.load_item(database.ITEMS_DB_NAME, item_id)
    if data:
        if "proto" in data:
            if data["proto"] == "item":
                data["meta"] = attributes
                data["metadata"] = metadata
                database.update_item(database.ITEMS_DB_NAME, item_id, data)
                return database.load_item(database.ITEMS_DB_NAME, item_id)
    return None


def add_image_to_item(item_id, image_id):
    data = database.load_item(database.ITEMS_DB_NAME, item_id)
    if data:
        if "proto" in data:
            if data["proto"] == "item":
                if image_id not in data["images"]:
                    data["images"].append(image_id)
                    database.update_item(database.ITEMS_DB_NAME, item_id, data)
                    return database.load_item(database.ITEMS_DB_NAME, item_id)
                # TODO else:
    return None


def update_collaborators(item_id, collaborators):
    data = database.load_item(database.ITEMS_DB_NAME, item_id)
    if data:
        if "proto" in data:
            if data["proto"] == "item":
                data["read"] = collaborators
                database.update_item(database.ITEMS_DB_NAME, item_id, data)
                return database.load_item(database.ITEMS_DB_NAME, item_id)
    return None


def update_images(item_id, images):
    data = database.load_item(database.ITEMS_DB_NAME, item_id)
    if data:
        if "proto" in data:
            if data["proto"] == "item":
                data["images"] = images
                database.update_item(database.ITEMS_DB_NAME, item_id, data)
                return database.load_item(database.ITEMS_DB_NAME, item_id)
    return None