import copy
import os
from io import BytesIO

from PIL import Image
from flask import request, jsonify
from modules.api import api

from modules.database import images, items

from modules.api.api import check_attributes
from werkzeug.utils import secure_filename


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
    attributes = ["file-name", "file-extension", "path", "width", "height"]
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


@api.api_blueprint.route('images/<collection_id>/<item_id>', methods=['POST'])
def upload_images(collection_id, item_id):
    files = request.files.getlist("files")
    # create directories
    if not os.path.exists("webapp/data/" + collection_id + "/" + item_id):
        os.makedirs("webapp/data/" + collection_id + "/" + item_id)

    for file in files:
        print(file.filename)
        filename = secure_filename(file.filename)
        extension = filename.split('.')[-1]
        path = collection_id + "/" + item_id

        image_bytes = BytesIO(file.stream.read())
        file.stream.seek(0)
        # get Image size
        img = Image.open(image_bytes)
        size = img.size

        #create image object in database
        image = images.add_image(extension, path, size[0], size[1])
        # add image to item
        items.add_image_to_item(item_id, image["_id"])

        file.save(os.path.join("webapp/data/" + collection_id + "/" + item_id, image["_id"] +"."+extension))
    resp = jsonify({'message': 'File successfully uploaded'})
    resp.status_code = 201
    return resp
