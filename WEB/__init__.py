"""this has all of imports and other init configs and other main"""
import warnings

from flask import *

from WEB.help_funcs import *
from WEB.routes import *

app = Flask(__name__)  # init flask app
app.debug = True  # debug
app.secret_key = "Help you Learn Stuff"  # secret key
app.config["SECURITY_PASSWORD_SALT"] = "Help you Learn Stuff"
password = "01x2253x6871"
