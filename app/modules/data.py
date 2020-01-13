# -*- coding: utf-8 -*-
"""methods serving webapp"""
from flask import Blueprint, send_from_directory, send_file

data_blueprint = Blueprint("data", __name__)


@data_blueprint.route("/<path:path>", methods=["GET"])
def get_path(path):
    """serving static file for the webapp"""
    return send_from_directory("data", path)