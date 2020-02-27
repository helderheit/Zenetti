from flask import request, jsonify
from modules.api import api

from modules.database import images

from modules.api.api import check_attributes


@api.api_blueprint.route("images/<image_id>", methods=["GET"])
def get_image(image_id):
    data = images.get_collection(image_id)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Could get image " + image_id}), 409
    return None


@api.api_blueprint.route("images/", methods=["POST"])
def add_image():
    """adds a image to the database"""
    data = request.json
    attributes = ["file-name", "file-extension", "path", "width","height"]
    attribute_missing = check_attributes(data, attributes)
    if attribute_missing:
        return jsonify(attribute_missing), 422

    success = images.add_image(data["file-name"],
                                         data["file-extension"],
                                         data["path"],
                                         data["width"],
                                         data["height"]
                               )
    if success:
        return jsonify(success), 200
    else:
        return jsonify({"error": "Could not add image"}), 409


@api.api_blueprint.route("images/<image_id>", methods=["PUT"])
def update_image(image_id):
    # TODO
    return None


@api.api_blueprint.route("images/<image_id>", methods=["DELETE"])
def remove_image(image_id):
    # TODO
    return None
