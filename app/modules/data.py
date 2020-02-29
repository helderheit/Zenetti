# -*- coding: utf-8 -*-
"""methods serving the IIIF api"""
import os

from flask import Blueprint, send_from_directory, send_file, request, jsonify
from flask_iiif.api import IIIFImageAPIWrapper
from werkzeug.utils import secure_filename
from modules.database import images

data_blueprint = Blueprint("data", __name__)


@data_blueprint.route("/data/<collection>/<item>/<uuid>/<region>/<size>/<rotation>/<quality>", methods=["GET"])
def get_image(collection, item, uuid, region, size, rotation, quality):
    quality = quality.replace(".jpg", "")
    quality = quality.replace(".tif", "")
    quality = quality.replace(".png", "")
    image = IIIFImageAPIWrapper.from_file("webapp/data/" + collection + "/" + item + "/" + uuid + ".tif")
    image.apply_api(
        region=region,
        size=size,
        rotation=rotation,
        quality=quality
    )

    return send_file(image.serve(), mimetype='image/jpeg')


@data_blueprint.route("/data/<collection>/<item>/<uuid>/info.json")
def get_image_info(collection, item, uuid):
    image = images.get_image(uuid)


    data = {
        "@context": "http://iiif.io/api/image/2/context.json",
        "@id": "http://localhost:4000/data/"+collection + "/"+item+"/"+uuid,
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

