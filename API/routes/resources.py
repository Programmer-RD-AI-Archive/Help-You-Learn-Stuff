from API import *

resources_request_parser_delete = reqparse.RequestParser()
resources_request_parser_delete.add_argument("id",
                                             type=int,
                                             help="id is required",
                                             required=True)
resources_request_parser = reqparse.RequestParser()
resources_request_parser.add_argument("method_of_resource",
                                      type=str,
                                      help="method_of_resource is required",
                                      required=True)
resources_request_parser.add_argument("link_of_resource",
                                      type=str,
                                      help="link_of_resource is required",
                                      required=True)
resources_request_parser.add_argument("title",
                                      type=str,
                                      help="title is required",
                                      required=True)
resources_request_parser.add_argument("description",
                                      type=str,
                                      help="description is required",
                                      required=True)


class Resources(Resource):
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
        asql = Azure_SQL()
        return {"message": asql.select_table("SELECT * FROM [Resources]")}

    def post(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        args = resources_request_parser_delete.parse_args()
        asql = Azure_SQL()
        return {
            "message":
            asql.insert_to_table(
                f"DELETE FROM Resources WHERE ID={args['id']}")
        }  # TODO

    def put(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        args = resources_request_parser.parse_args()
        asql = Azure_SQL()
        asql.insert_to_table(
            f"INSERT INTO [Resources]( [method_of_resource], [link_of_resource], [title], [description] ) VALUES ( '{args['method_of_resource']}', '{args['link_of_resource']}','{args['title']}','{args['description']}')"
        )


api.add_resource(Resources, "/api/resources")
