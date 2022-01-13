
from azure.storage.blob import (
    __version__)
from flask import Flask
from flask_restful import Api

from API.db import *
from API.help_funcs import *
from API.routes import *

password = "01x2253x6871"
app = Flask(__name__)
app.debug = True  # debug
app.secret_key = "Help you Learn Stuff"  # secret key
app.config["SECURITY_PASSWORD_SALT"] = "Help you Learn Stuff"
api = Api(app)
