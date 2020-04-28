from flask import jsonify, g, request
from modules.api import api

from modules.database import users

from modules import config


@api.api_blueprint.route("users", methods=["POST"])
@api.auth.login_required
def add_user():
    """adds a user to the database"""
    if g.user.admin:

        data = request.json
        if "username" not in data:
            return jsonify({"error": "Missing field username"}), 422
        if "name" not in data:
            return jsonify({"error": "Missing field name"}), 422
        if "password" not in data:
            return jsonify({"error": "Missing field password"}), 422
        if "admin" not in data:
            return jsonify({"error": "Missing field admin"}), 422
        if "change_password" not in data:
            return jsonify({"error": "Missing field change_password"}), 422
        if not g.user.master:
            # only the master-user is allowed to create admins
            data["admin"] = False
        success = users.add_user(data["username"], data["name"], data["password"], data["admin"],
                                 data["change_password"])
        if success:
            return jsonify({"ok": "Added user " + data["username"]}), 200
        else:
            return jsonify({"error": "Could not add user " + data["username"]}), 409
    else:
        return jsonify({"error": "Access denied"}), 401


@api.api_blueprint.route("users", methods=["PUT"])
@api.auth.login_required
def update_user():
    """updates a user in the database"""
    data = request.json
    access = False
    if g.user.admin:
        access = True
        print(data)
    if "username" in data:
        if data["username"] == g.user.username:
            access = True
    if access:
        if "username" not in data:
            return jsonify({"error": "Missing field username"}), 422
        if "name" not in data:
            return jsonify({"error": "Missing field name"}), 422
        if "password" not in data:
            return jsonify({"error": "Missing field password"}), 422
        if "admin" not in data:
            return jsonify({"error": "Missing field admin"}), 422
        if "change_password" not in data:
            return jsonify({"error": "Missing field change_password"}), 422
        if not g.user.master:
            # only the master-user is allowed to create admins
            data["admin"] = False

        success = users.update_user(data["username"], data["name"], data["password"], data["admin"],
                                    data["change_password"])
        if success:
            return jsonify({"ok": "Updated user " + data["username"]}), 200
        else:
            return jsonify({"error": "Could not update user " + data["username"]}), 409
    else:
        return jsonify({"error": "Access denied"}), 401


@api.api_blueprint.route("users/<username>", methods=["DELETE"])
@api.auth.login_required
def remove_user(username):
    """remove a user from the database"""
    if g.user.admin:
        success = users.remove_user(username)
        if success:
            return jsonify({"ok": "Removed user " + username}), 200
        else:
            return jsonify({"error": "Could not remove user" + username}), 409
    else:
        return jsonify({"error": "Access denied"}), 401


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


@api.api_blueprint.route("users/<username>", methods=["GET"])
@api.auth.login_required
def get_user(username):
    """get a user from the database"""
    if g.user.admin or g.user.username == username:
        user = users.get_user(username)
        if user:
            user = user.to_dict()
            user["host"]= config.host
            return jsonify(user), 200
        else:
            return jsonify({"error": "Could get user"}), 409
    else:
        return jsonify({"error": "Access denied"}), 401
