import json
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import pyodbc
import textwrap
import binascii
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import smtplib, ssl

password = "01x2253x6871"
app = Flask(__name__)
app.debug = True  # debug
app.secret_key = "Help you Learn Stuff"  # secret key
app.config["SECURITY_PASSWORD_SALT"] = "Help you Learn Stuff"
api = Api(app)
from API.help_funcs import *
from API.db import *
from API.routes import *
