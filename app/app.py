from flask import Flask
from flask_iiif import IIIF
from flask_restful import Api

from modules.web import web_blueprint
from modules.api.api import api_blueprint
from modules.data import data_blueprint
from modules.api import administration
from modules.api import collections

from modules.database import database

app = Flask(__name__)

api_url_prefix = "/api/1.0/"

#load api functins
app.register_blueprint(api_blueprint, url_prefix=api_url_prefix)

#load functions serving the webapp
app.register_blueprint(web_blueprint)

##IIIF API
ext = IIIF(app=app)
api = Api(app=app)
ext.init_restful(api)

#load functions serving the images
app.register_blueprint(data_blueprint)

if __name__ == "__main__":
    port = 4000
    host = "0.0.0.0"
    database.initialize()
    app.run(port=port, host=host, debug=False, threaded=True)