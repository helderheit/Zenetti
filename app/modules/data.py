# -*- coding: utf-8 -*-
"""methods serving webapp"""
from flask import Blueprint, send_from_directory, send_file
from flask_iiif.api import IIIFImageAPIWrapper

data_blueprint = Blueprint("data", __name__)


@data_blueprint.route("/data/<collection>/<item>/<uuid>/<region>/<size>/<rotation>/<quality>", methods=["GET"])

def get_image(collection, item, uuid, region, size, rotation, quality):

    quality = quality.replace(".jpg","")
    quality = quality.replace(".tif", "")
    quality = quality.replace(".png", "")
    image = IIIFImageAPIWrapper.from_file("webapp/data/"+collection+"/"+item+"/"+ uuid+ ".tif")
    image.apply_api(
        region=region,
        size=size,
        rotation=rotation,
        quality=quality
    )

    return send_file(image.serve(), mimetype='image/jpeg')