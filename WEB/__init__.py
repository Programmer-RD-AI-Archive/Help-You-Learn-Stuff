"""
this has all of imports and other init configs and other main
"""
from flask import *
import pymongo
import stripe
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
import os
import random
from twilio.rest import Client
import requests

app = Flask(__name__)  # init flask app
app.debug = True  # debug
app.secret_key = "Help you Learn Stuff"  # secret key
app.config["SECURITY_PASSWORD_SALT"] = "Help you Learn Stuff"
from WEB.routes import *
