from os import getenv
from flask import Flask
from flask_restful import Api as ApiRest
from resources.translator import Translator
from resources.ping import Ping
from config_params import init_cfg

prefix_url = getenv("PREFIX_URL", "")
static_url_path = getenv("STATIC_URL", None)
app = Flask(__name__)
api = ApiRest(app)

init_cfg(app)

api.add_resource(Translator, "/traductor")
api.add_resource(Ping, "/ping")                  
                

if __name__ == "__main__":
    host = app.config["HOST"]
    port = app.config["PORT"]
    app.run(host=host, port=port, debug=False, use_reloader=False)