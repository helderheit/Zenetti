# -*- coding: utf-8 -*-
"""methods serving the IIIF api"""
from os import path
from flask import Blueprint, send_from_directory, send_file, request, jsonify
from flask_iiif.api import IIIFImageAPIWrapper
from werkzeug.utils import secure_filename
from modules.database import images, collections
from modules.api import api
from modules.database import items

from modules import config

data_blueprint = Blueprint("data", __name__)


@data_blueprint.route("/data/<collection>/<item>/<uuid>/<region>/<size>/<rotation>/<quality>", methods=["GET"])
@api.auth.login_required
def get_image(collection, item, uuid, region, size, rotation, quality):

    quality = quality.replace(".jpg", "")
    quality = quality.replace(".tif", "")
    quality = quality.replace(".png", "")
    file_extension = images.get_image(uuid)["file-extension"]

    image_path = "webapp/data/" + collection + "/" + item + "/" + uuid + "."+file_extension
    # check if file exists
    if path.exists(image_path):
        print("image file found")
    else:
        print("image file not found")
    image = IIIFImageAPIWrapper.open_image(image_path)
    image.apply_api(
        region=region,
        size=size,
        rotation=rotation,
        quality=quality
    )

    return send_file(image.serve(), mimetype='image/jpeg')


@data_blueprint.route("/data/<collection>/<item>/<uuid>/info.json")
@api.auth.login_required
def get_image_info(collection, item, uuid):
    image = images.get_image(uuid)

    data = {
        "@context": "http://iiif.io/api/image/2/context.json",
        "@id": config.host + "/data/" + collection + "/" + item + "/" + uuid,
        "protocol": "http://iiif.io/api/image",
        "width": image["meta"]["width"],
        "height": image["meta"]["height"],
        "sizes": [
            {"width": 206, "height": 152},
            {"width": 309, "height": 238}
        ],
        "tiles": [
            {"width": 256, "height": 256, "scaleFactors": [1, 2, 4, 8, 16, 32]}
        ],
        "profile": [
            "http://iiif.io/api/image/2/level1.json",
            {"formats": ["jpg"],
             "qualities": ["native", "color", "gray", "bitonal"],
             "supports": ["regionByPct", "regionSquare", "sizeByForcedWh", "sizeByWh", "sizeAboveFull", "rotationBy90s",
                          "mirroring"],
             "maxWidth": 1000,
             "maxHeight": 1000
             }
        ]
    }
    return jsonify(data), 200


def generate_image_in_manifest(collection_id, item_id, image_object):
    image_json = {
        "@id": config.host + "/data/" + collection_id + "/" + item_id + "/" + image_object["_id"] + ".json",
        "@type": "sc:Canvas",
        "label": "",
        "width": image_object["meta"]["width"],
        "height": image_object["meta"]["height"],
        "images": [
            {"@id": config.host + "/data/" + collection_id + "/" + item_id + "/" + image_object["_id"] + ".json",
             "@type": "oa:Annotation",
             "motivation": "sc:painting",
             "on": config.host + "/data/" + collection_id + "/" + item_id + "/" + image_object["_id"] + ".json",
             "resource": {
                 "@id": config.host + "/data/" + collection_id + "/" + item_id + "/" + image_object["_id"],
                 "@type": "dctypes:Image",
                 "format": "image/jpeg",
                 "width": image_object["meta"]["width"],
                 "height": image_object["meta"]["height"],
                 "service": {"@context": "http://iiif.io/api/image/2/context.json",
                             "profile": "http://iiif.io/api/image/2/level1.json",
                             "@id": config.host + "/data/" + collection_id + "/" + item_id + "/" + image_object[
                                 "_id"]}}}]
    }

    return image_json


@data_blueprint.route("/data/<collection_id>/<item_id>")
@api.auth.login_required
def get_manifest(collection_id, item_id):
    item = items.get_item(item_id)
    # generate json for images
    image_json = []
    first_image_id = ""
    for image_id in item["images"]:
        if first_image_id == "":
            first_image_id = image_id
        image_json.append(generate_image_in_manifest(collection_id, item_id, images.get_image(image_id)))

    manifest = {
        "@context": "http://iiif.io/api/presentation/2/context.json",
        "@id": config.host + "/" + collection_id + "/" + item_id,
        "@type": "sc:Manifest",
        "attribution": item["meta"]["attribution"],
        "metadata": item["metadata"],
        "label": item["meta"]["label"],
        "logo": item["meta"]["logo"],
        "service": {
            "@context": "http://iiif.io/api/search/1/context.json",
            "@id": "http://exist.scta.info/exist/apps/scta/iiif/pg-lon/search",
            "profile": "http://iiif.io/api/search/1/search",
            "label": "Search within this manifest"
        },
        "rendering": {
            "@id": config.host + "/",
            "format": "text/html",
            "label": "Full record view"
        },
        "sequences": [
            {"@id": config.host + "/" + collection_id + "/" + item_id + "/" + first_image_id + ".json",
             "@type": "sc:Sequence",
             "label": "Default",
             "canvases": image_json}],
        "thumbnail": {
            "@id": config.host + "/data" + collection_id + "/" + item_id + "/" + first_image_id + "/full/,200/0/default",
            "service": {"@context": "http://iiif.io/api/image/2/context.json",
                        "@id": config.host + "/data/" + collection_id + "/" + item_id + "/" + first_image_id,
                        "profile": "http://iiif.io/api/image/2/level2.json"}},
        "within": config.host + "/"
    }

    return jsonify(manifest), 200
