from flask import request, jsonify
from modules.api import api

from modules.database import collections

from modules.api.api import check_attributes


@api.api_blueprint.route("item/<item_id>", methods=["GET"])
def get_item(item_id):
    #TODO
    pass

@api.api_blueprint.route("item", methods=["POST"])
def add_item():
    #TODO
    pass


@api.api_blueprint.route("collection", methods=["POST"])
def add_collection():
    """adds a project to the database"""
    data = request.json
    attributes = ["label", "description", "attribution", "logo"]
    attribute_missing = check_attributes(data, attributes)
    if attribute_missing:
        return jsonify(attribute_missing), 422

    success = collections.add_collection(data["label"],
                                   data["description"],
                                   data["attribution"],
                                   data["logo"])
    if success:
        return jsonify(success), 200
    else:
        return jsonify({"error": "Could not add collection"}), 409

@api.api_blueprint.route("collection", methods=["GET"])
def get_projects():
    """get a list of collections from the database"""
    data = collections.get_collections()
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Could get projects"}), 409

