from flask import jsonify, g
from modules.api import api

from modules.database import users


@api.api_blueprint.route("users", methods=["GET"])
@api.auth.login_required
def get_users():
    """get a list of users from the database"""
    if g.user.admin:
        data = users.get_users()
        if data:
            return jsonify(data), 200
        else:
            return jsonify({"error": "Could get users"}), 409
    else:
        return jsonify({"error": "Access denied"}), 401
