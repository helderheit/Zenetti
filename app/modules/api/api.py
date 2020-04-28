# -*- coding: utf-8 -*-
"""core functionality an methods of the REST-Api"""
from flask import Blueprint, jsonify, request, g, Response, json
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                          BadSignature, SignatureExpired)

from modules.database import users

from modules import config

api_blueprint = Blueprint("api", __name__)

auth = HTTPBasicAuth()

secret_key = "".join(random.choice(string.ascii_uppercase + string.digits)
                     for x in range(32))


@api_blueprint.route("info/", methods=["GET"])
def get_api_info():
    """
        return information about the api and the server
    """
    res = {"zenetti": "api", "version": "1.0"}
    return jsonify(res)


@api_blueprint.route("token", methods=["GET"])
@auth.login_required
def get_auth_token():
    """returns a token"""
    token = g.user.generate_auth_token()
    return jsonify({"token": token.decode("utf-8"), "host":config.host})


@auth.verify_password
def verify_password(username_or_token, password):
    # handles api login with username or token
    username = User.verify_auth_token(username_or_token)
    if username:
        user = users.get_user(username)
    else:
        user = users.get_user(username_or_token)
        if user is None:
            return False
        elif user.verify_password(password):
            pass
        else:
            return False
    g.user = user
    return True


class User:
    # class representing a user of the RESTfull-API
    username = None
    name = None
    password_hash = None

    def __init__(self, username=None, name=None, password_hash=None, admin=False, master=False, change_password=False):
        self.username = username
        self.name = name
        self.password_hash = password_hash
        self.admin = admin
        self.master = master
        self.change_password = change_password

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        serializer = Serializer(secret_key, expires_in=expiration)
        return serializer.dumps({"username": self.username})

    def to_dict(self):
        return {"username": self.username, "name": self.name, "change_password": self.change_password,
                "admin": self.admin, "master": self.master}

    def debug(self):
        print(self.username, self.name, self.password_hash, self.admin, self.master, self.change_password)

    @staticmethod
    def verify_auth_token(token):
        serializer = Serializer(secret_key)
        try:
            data = serializer.loads(token)
        except SignatureExpired:
            # Valid token but expired
            return None
        except BadSignature:
            # Invalid Token
            return None
        username = data["username"]
        return username


def check_attributes(data, attributes):
    for attribute in attributes:
        if attribute not in data:
            return {"error": "Missing field " + attribute}
    return None
