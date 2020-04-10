from flask import request, jsonify
from modules.api import api
from modules.database import collections
from modules.api.api import check_attributes


@api.api_blueprint.route("collections", methods=["GET"])
@api.auth.login_required
def get_collections():
    """get a list of collections from the database"""
    # TODO for development purpose only
    data = collections.get_collections()
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Could get collections"}), 409


@api.api_blueprint.route("collections/<collection_id>", methods=["GET"])
@api.auth.login_required
def get_collection(collection_id):
    """get a collection from the database"""
    data = collections.get_collection(collection_id)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Could get collection " + collection_id}), 409


@api.api_blueprint.route("collections", methods=["POST"])
@api.auth.login_required
def add_collection():
    """adds a collection to the database"""
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


@api.api_blueprint.route("collections/<collection_id>", methods=["PUT"])
@api.auth.login_required
def update_collection(collection_id):
    """update a collection"""

    data = request.json
    attributes = ["label", "description", "attribution", "logo"]
    attribute_missing = check_attributes(data, attributes)
    if attribute_missing:
        return jsonify(attribute_missing), 422

    success = collections.update_collection(collection_id,
                                            data["label"],
                                            data["description"],
                                            data["attribution"],
                                            data["logo"],
                                            )
    if success:
        return jsonify(success), 200
    else:
        return jsonify({"error": "Could not update collection " + collection_id}), 409


@api.api_blueprint.route("collections/<collection_id>", methods=["DELETE"])
@api.auth.login_required
def remove_collection(collection_id):
    """remove a collection from the database"""
    success = collections.remove_collection(collection_id)
    if success:
        return jsonify({"ok": "Removed collection " + collection_id}), 200
    else:
        return jsonify({"error": "Could not remove collection " + collection_id}), 409
