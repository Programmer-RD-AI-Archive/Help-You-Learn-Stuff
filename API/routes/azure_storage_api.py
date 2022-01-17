from API import *

azure_storage_request_parser = reqparse.RequestParser()
azure_storage_request_parser.add_argument(
    "Container Name", type=str, help="Container Name is required", required=True
)
azure_storage_request_parser.add_argument(
    "blob_name", type=str, help="blob_name is required", required=False
)
azure_storage_request_parser.add_argument(
    "file_rb", type=str, help="file_rb is required", required=False
)
azure_storage_request_parser.add_argument(
    "file_name", type=str, help="file_name is required", required=False
)
azure_storage_request_parser.add_argument("Type", type=str, help="Type is required", required=False)


class Azure_Storage_API(Resource):
    def get(self) -> dict:
        args = azure_storage_request_parser.parse_args()
        astorage = Azure_Storage(args["Container Name"])
        if args["Type"] == "Create File":
            return {
                "message": astorage.create_file(
                    blob_name=args["blob_name"], file_rb=args["file_rb"]
                )
            }
        if args["Type"] == "Find File":
            return {"message": astorage.find_file()}
        if args["Type"] == "Download File":
            return {
                "message": astorage.download_file(file_name_in_the_cloud=args["file_name"]).decode(
                    "utf-8"
                )
            }
        if args["Type"] == "Delete Container":
            return {"message": astorage.delete_blob()}
        return {"message": "Not correct type"}


api.add_resource(Azure_Storage_API, "/api/azure/storage")
