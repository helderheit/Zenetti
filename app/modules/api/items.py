from flask import request, jsonify
from modules.api import api

from modules.database import items
from modules.database import collections
from modules.database import images

from modules.api.api import check_attributes


@api.api_blueprint.route("items", methods=["GET"])
@api.auth.login_required
def get_items():
    """get a list of collections from the database"""
    data = items.get_items()
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Could get items"}), 409


@api.api_blueprint.route("items/<item_id>", methods=["GET"])
@api.auth.login_required
def get_item(item_id):
    """get a item from the database"""
    data = items.get_item(item_id)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Could get item " + item_id}), 409
    pass


def extract_metadata(data):
    metadata = []
    for key in data:
        if key not in ["label", "description", "attribution", "logo"]:
            metadata.append({"label": key, "value": data[key]})
    return metadata


@api.api_blueprint.route("items/<collection_id>", methods=["POST"])
@api.auth.login_required
def add_item(collection_id):
    """add a item to the database"""
    data = request.json
    attributes = ["label", "description", "attribution", "logo"]
    attribute_missing = check_attributes(data, attributes)
    if attribute_missing:
        return jsonify(attribute_missing), 422
    metadata = extract_metadata(data)
    success = items.add_item(data["label"],
                             data["description"],
                             data["attribution"],
                             data["logo"], metadata)
    if success:
        collections.add_item_to_collection(collection_id, success["_id"])
        return jsonify(success), 200
    else:
        return jsonify({"error": "Could not add item"}), 409


@api.api_blueprint.route("items/<collection_id>/<item_id>", methods=["DELETE"])
@api.auth.login_required
def remove_item(collection_id, item_id):
    """remove a item from the database"""
    success = items.remove_item(item_id)
    collections.remove_item_from_collection(collection_id, item_id)
    if success:
        return jsonify({"ok": "Removed item " + item_id}), 200
    else:
        return jsonify({"error": "Could not remove item " + item_id}), 409


@api.api_blueprint.route("items/<item_id>", methods=["PUT"])
@api.auth.login_required
def update_item(item_id):
    """update an item"""

    data = request.json
    attributes = ["label", "description", "attribution", "logo"]
    attribute_missing = check_attributes(data, attributes)
    if attribute_missing:
        return jsonify(attribute_missing), 422
    metadata = extract_metadata(data)
    success = items.update_metadata(item_id, {
        "label": data["label"],
        "description": data["description"],
        "attribution": data["attribution"],
        "logo": data["logo"]
    }, metadata)
    if success:
        return jsonify(success), 200
    else:
        return jsonify({"error": "Could not update item " + item_id}), 409


@api.api_blueprint.route("/<collection_id>/<item_id>/annotations.json")
@api.auth.login_required
def get_annotations(collection_id, item_id):
    annotations_json = {}
    item = items.get_item(item_id)
    first_image_id = ""
    for image_id in item["images"]:
        if first_image_id == "":
            first_image_id = image_id
            image = images.get_image(image_id)
            annotations_json["http://localhost:4000/data/" + collection_id + "/" +
                             item_id + "/" + image_id + ".json"] = image["annotations"]
    return jsonify(annotations_json), 200
