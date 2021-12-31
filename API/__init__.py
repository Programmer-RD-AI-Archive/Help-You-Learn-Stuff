import json
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

password = "01x2253x6871"
app = Flask(__name__)
api = Api(app)
get_config_request_parser = reqparse.RequestParser()
get_config_request_parser.add_argument(
    "password", type=str, help="Password is required", required=True
)


class Get_Config(Resource):
    def get(self):
        args = get_config_request_parser.parse_args()
        if args["password"] == password:
            config = open("./API/config.json")
            config = json.load(config)
            return {"config": config}
        else:
            abort(401, message="Wrong password")


api.add_resource(Get_Config, "/api/get_config")
from API.routes import *
