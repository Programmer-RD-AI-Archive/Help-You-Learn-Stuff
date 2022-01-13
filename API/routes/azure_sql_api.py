from API import *

hp = Help_Funcs()
azure_sql_request_parser = reqparse.RequestParser()
azure_sql_request_parser.add_argument("Type",
                                      type=str,
                                      help="Type is required",
                                      required=True)
azure_sql_request_parser.add_argument("Query",
                                      type=str,
                                      help="Query is required",
                                      required=False)


class Azure_SQL_API(Resource):
    def get(self) -> dict:
        args = azure_sql_request_parser.parse_args()
        asql = Azure_SQL()
        if args["Type"] == "Table":
            return {"message": asql.create_new_table(args["Query"])}
        if args["Type"] == "Insert":
            return {"message": asql.insert_to_table(args["Query"])}
        if args["Type"] == "Select":
            return {"message": asql.select_table(args["Query"])}
        if args["Type"] == "Get Tables":
            return {"message": asql.create_new_table()}
        return {"message": "Not correct type"}


api.add_resource(Azure_SQL_API, "/api/azure/sql")
