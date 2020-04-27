# -*- coding: utf-8 -*-

import json
from modules import config

CONFIG_PATH = "config/app.conf"

master_username = ""
master_password = ""


def get_config():
    """get the local node configurations
    Returns:
        dict: a dict containing node_id, connection, master_username and master_password
    """
    global res
    try:
        with open(CONFIG_PATH) as config_file:
            node_json = json.load(config_file)
            res = node_json
            config.master_username = res["master_username"]
            config.master_password = res["master_password"]
    except Exception as e:
        print("Could not load config: " + str(e))
    return res
