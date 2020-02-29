# -*- coding: utf-8 -*-
"""methods serving the IIIF api"""
import os

from flask import Blueprint, send_from_directory, send_file, request, jsonify
from flask_iiif.api import IIIFImageAPIWrapper
from werkzeug.utils import secure_filename

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


# @data_blueprint.route("/data/<collection>/<item>/<uuid>/info.json")
# def get_image_info(collection, item, uuid):
#    pass

