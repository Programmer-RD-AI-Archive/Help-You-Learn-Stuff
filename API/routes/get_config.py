from API import *

get_config_request_parser = reqparse.RequestParser()
get_config_request_parser.add_argument("password",
                                       type=str,
                                       help="Password is required",
                                       required=True)


class Get_Config(Resource):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def get(self) -> dict:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        args = get_config_request_parser.parse_args()
        if args["password"] == password:
            config = open("./API/config.json")
            config = json.load(config)
            return {"config": config}
        abort(401, message="Wrong password")


api.add_resource(Get_Config, "/api/get_config")
