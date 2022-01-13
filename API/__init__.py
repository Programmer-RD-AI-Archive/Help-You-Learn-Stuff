import binascii
import json
import os
import smtplib
import ssl
import textwrap
import uuid

import pyodbc
from azure.storage.blob import (
    BlobClient,
    BlobServiceClient,
    ContainerClient,
    __version__,
)
from flask import Flask
from flask_restful import Api, Resource, abort, fields, marshal_with, reqparse

from API.db import *
from API.help_funcs import *
from API.routes import *

password = "01x2253x6871"
app = Flask(__name__)
app.debug = True  # debug
app.secret_key = "Help you Learn Stuff"  # secret key
app.config["SECURITY_PASSWORD_SALT"] = "Help you Learn Stuff"
api = Api(app)
