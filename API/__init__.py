import json
import warnings

from flask import *
from flask_restful import *
from flask_restful import reqparse

config = json.load(open("./API/config.json"))
password = config["Configs"]["API Key"]
app = Flask(__name__)
app.debug = True  # debug
app.secret_key = config["Configs"]["Secret Key"]  # secret key
app.config["SECURITY_PASSWORD_SALT"] = config["Configs"]["Secret Key"]
api = Api(app)
from API.db import *
from API.help_funcs import *
from API.routes import *
