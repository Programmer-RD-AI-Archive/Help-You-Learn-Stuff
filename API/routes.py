from API import *

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
get_config_request_parser = reqparse.RequestParser()
get_config_request_parser.add_argument("password",
                                       type=str,
                                       help="Password is required",
                                       required=True)
contact_us_request_parser = reqparse.RequestParser()
contact_us_request_parser.add_argument("email",
                                       type=str,
                                       help="email is required",
                                       required=True)
contact_us_request_parser.add_argument("question",
                                       type=str,
                                       help="question is required",
                                       required=True)
azure_sql_request_parser = reqparse.RequestParser()
azure_sql_request_parser.add_argument("Type",
                                      type=str,
                                      help="Type is required",
                                      required=True)
azure_sql_request_parser.add_argument("Query",
                                      type=str,
                                      help="Query is required",
                                      required=False)
azure_storage_request_parser = reqparse.RequestParser()
azure_storage_request_parser.add_argument("Container Name",
                                          type=str,
                                          help="Container Name is required",
                                          required=True)
azure_storage_request_parser.add_argument("blob_name",
                                          type=str,
                                          help="blob_name is required",
                                          required=False)
azure_storage_request_parser.add_argument("file_rb",
                                          type=str,
                                          help="file_rb is required",
                                          required=False)
azure_storage_request_parser.add_argument("file_name",
                                          type=str,
                                          help="file_name is required",
                                          required=False)
azure_storage_request_parser.add_argument("Type",
                                          type=str,
                                          help="Type is required",
                                          required=False)
accounts_request_parser = reqparse.RequestParser()
accounts_request_parser.add_argument("email",
                                     type=str,
                                     help="email is required",
                                     required=True)
accounts_request_parser.add_argument("password",
                                     type=str,
                                     help="Password is required",
                                     required=True)
accounts_request_parser.add_argument("user_name",
                                     type=str,
                                     help="user name is required",
                                     required=True)
cources = reqparse.RequestParser()
cources.add_argument("html", type=str, help="html is required", required=True)
cources.add_argument("name", type=str, help="name is required", required=True)
resources_request_parser_delete = reqparse.RequestParser()
resources_request_parser_delete.add_argument("id",
                                             type=int,
                                             help="id is required",
                                             required=True)
courses = reqparse.RequestParser()
courses.add_argument("whole_content",
                     type=str,
                     help="whole_content is required",
                     required=True)
courses.add_argument("info", help="info is required", required=True, type=str)
courses.add_argument("image",
                     type=str,
                     help="image is required",
                     required=True)
courses.add_argument("name", type=str, help="name is required", required=True)
courses.add_argument("marks",
                     type=str,
                     help="marks is required",
                     required=True)


class Get_Config(Resource):
    def get(self):
        args = get_config_request_parser.parse_args()
        if args["password"] == password:
            config = open("./API/config.json")
            config = json.load(config)
            return {"config": config}
        abort(401, message="Wrong password")


class Contact_Us(Resource):
    def post(self):
        try:
            args = contact_us_request_parser.parse_args()
            email = args["email"]
            question = args["question"]
            send_email(subject=question,
                       message=f"Email - {email} \n Question {question}")
            asql = Azure_SQL()
            tables = asql.get_tables()
            if "Contact_Us" not in tables:
                result = asql.create_new_table(
                    "CREATE TABLE Contact_Us (ID int IDENTITY(1,1),  Email varchar(max),Question varchar(max))"
                )
                if result[0] is False:
                    return {"message": False}
            result = asql.insert_to_table(
                f"INSERT INTO [Contact_Us]( [Email], [Question] ) VALUES ( '{email}', '{question}')"
            )
            if result[0] is False:
                return {"message": False}
            # Added DB
            return {"message": True}
        except Exception as e:
            return {"message": False}


class Accounts(Resource):
    def get(self):
        asql = Azure_SQL()
        tables = asql.get_tables()
        if "Accounts" not in tables:
            result = asql.create_new_table(
                "CREATE TABLE Accounts (ID int IDENTITY(1,1), Rank INT(max), Email varchar(max),User_Name varchar(max), Password varchar(max))"
            )
            if result[0] is False:
                return {"message": False}
        newaccounts = []
        accounts = asql.select_table("SELECT * FROM [Accounts]")
        for account in accounts:
            newaccounts.append(list(account))
        return {"message": newaccounts}

    def post(self):
        args = accounts_request_parser.parse_args()
        asql = Azure_SQL()
        tables = asql.get_tables()
        if "Accounts" not in tables:
            result = asql.create_new_table(
                "CREATE TABLE Accounts (ID int IDENTITY(1,1), Rank INT(max), Email varchar(max),User_Name varchar(max), Password varchar(max))"
            )
            if result[0] is False:
                return {"message": False}
        result = asql.insert_to_table(
            f"INSERT INTO [Accounts]( [Rank],[Email], [User_Name], [Password] ) VALUES ( 1,'{args['email']}', '{args['user_name']}', '{args['password']}')"
        )
        if result[0] is False:
            return {"message": False}
        newaccounts = []
        accounts = asql.select_table("SELECT * FROM [Accounts]")
        for account in accounts:
            newaccounts.append(list(account))
        return {"message": newaccounts}


class Questions(Resource):
    def get(self):
        asql = Azure_SQL()
        tables = asql.get_tables()
        if "Questions" not in tables:
<<<<<<< Updated upstream
            asql.create_new_table("""
=======
            result = asql.create_new_table(
                """
>>>>>>> Stashed changes
                CREATE TABLE Questions
                (
                    [ID] int IDENTITY(1,1),
                    [html] varchar(max),
                    [name] varchar(max),
                )
<<<<<<< Updated upstream
                """)
=======
                """
            )
            if result[0] is False:
                return {"message": False}
>>>>>>> Stashed changes
        return {"message": asql.select_table(f"SELECT * FROM Questions")}

    def post(self):
        args = cources.parse_args()
        asql = Azure_SQL()
        tables = asql.get_tables()
        if "Questions" not in tables:
<<<<<<< Updated upstream
            asql.create_new_table("""
=======
            result = asql.create_new_table(
                """
>>>>>>> Stashed changes
                CREATE TABLE Questions
                (
                    [ID] int IDENTITY(1,1),
                    [html] varchar(max),
                    [name] varchar(max),
                )
<<<<<<< Updated upstream
                """)
        asql.insert_to_table(
=======
                """
            )
            if result[0] is False:
                return {"message": False}
        result = asql.insert_to_table(
>>>>>>> Stashed changes
            f"INSERT INTO Questions (html, name) VALUES ('{args['html']}','{args['name']}');"
        )
        if result[0] is False:
            return {"message": False}
        return {"message": True}


class Resources(Resource):
    def get(self):
        asql = Azure_SQL()
        return {"message": asql.select_table(f"SELECT * FROM [Resources]")}

    def post(self):
        args = resources_request_parser_delete.parse_args()
        asql = Azure_SQL()
        return {
            "message":
            asql.insert_to_table(
                f"DELETE FROM Resources WHERE ID={args['id']}")
        }  # TODO

    def put(self):
        args = resources_request_parser.parse_args()
        asql = Azure_SQL()
        result = asql.insert_to_table(
            f"INSERT INTO [Resources]( [method_of_resource], [link_of_resource], [title], [description] ) VALUES ( '{args['method_of_resource']}', '{args['link_of_resource']}','{args['title']}','{args['description']}')"
        )
        if result[0] is False:
            return {"message": False}


class Courses(Resource):
    def put(self):
        args = courses.parse_args()
        asql = Azure_SQL()
        astorage = Azure_Storage("cource")
        cources = asql.select_table("SELECT * FROM Courses")
        ids_of_cources = []
        for cource in cources:
            ids_of_cources.append(cource)
        if ids_of_cources == []:
            ids_of_cources = [[0]]
        id_new = ids_of_cources[-1][0]
        id_new += 1

        info = str(args["info"])
        info = bytes(info, encoding="utf-8")
<<<<<<< Updated upstream
        astorage.create_file(file_name_in_the_cloud=f"{id_new}-info.txt",
                             file_rb=info)

        tables = asql.get_tables()
        if "Questions" not in tables:
            asql.create_new_table("""
=======
        result = astorage.create_file(file_name_in_the_cloud=f"{id_new}-info.txt", file_rb=info)
        if result[0] is False:
            return {"message": False}
        tables = asql.get_tables()
        if "Questions" not in tables:
            result = asql.create_new_table(
                """
>>>>>>> Stashed changes
                CREATE TABLE Courses
                (
                    [ID] int IDENTITY(1,1),
                    [Whole Content] varchar(max),
                    [Info] varchar(max),
                    [Image] varchar(max),
                    [Name] varchar(max),
                    [Marks] varchar(max)
                )
<<<<<<< Updated upstream
                """)
        asql.insert_to_table(f"""
=======
                """
            )
            if result[0] is False:
                return {"message": False}
        result = asql.insert_to_table(
            f"""
>>>>>>> Stashed changes
            INSERT INTO [Courses]
            (   
                [Whole_Content],
                [Info],
                [Image],
                [Name],
                [Marks]
            ) 
            VALUES 
            ( 
                '{args['whole_content']}',
                '{id_new}-info.txt',
                '{args['image']}',
                '{args['name']}',
                '{args['marks']}'
            )
<<<<<<< Updated upstream
            """)
=======
            """
        )
        if result[0] is False:
            return {"message": False}
>>>>>>> Stashed changes
        return {"message": True}

    def get(self):
        asql = Azure_SQL()
        tables = asql.get_tables()
        if "Questions" not in tables:
            result = asql.create_new_table(
                """
                CREATE TABLE Courses
                (
                    [ID] int IDENTITY(1,1),
                    [Whole Content] varchar(max),
                    [Info] varchar(max),
                    [Image] varchar(max),
                    [Name] varchar(max)
                )
                """
            )
            if result[0] is False:
                return {"message": False}
        return {"message": asql.select_table(f"SELECT * FROM Courses;")}


class Azure_SQL_API(Resource):
    def get(self):
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


class Azure_Storage_API(Resource):
    def get(self):
        args = azure_storage_request_parser.parse_args()
        astorage = Azure_Storage(args["Container Name"])
        if args["Type"] == "Create File":
            return {
                "message":
                astorage.create_file(blob_name=args["blob_name"],
                                     file_rb=args["file_rb"])
            }
        if args["Type"] == "Find File":
            return {"message": astorage.find_file()}
<<<<<<< Updated upstream
        if args["Type"] == "Download File":
            return {
                "message":
                astorage.download_file(
                    file_name_in_the_cloud=args["file_name"]).decode("utf-8")
            }
        if args["Type"] == "Delete Container":
=======
        elif args["Type"] == "Download File":
            return {"message": astorage.download_file(file_name_in_the_cloud=args["file_name"])}
        elif args["Type"] == "Delete Container":
>>>>>>> Stashed changes
            return {"message": astorage.delete_blob()}
        return {"message": "Not correct type"}


api.add_resource(Resources, "/api/resources")
api.add_resource(Azure_Storage_API, "/api/azure/storage")
api.add_resource(Azure_SQL_API, "/api/azure/sql")
api.add_resource(Questions, "/api/questions")
api.add_resource(Contact_Us, "/api/Contact_Us")
api.add_resource(Accounts, "/api/Accounts")
api.add_resource(Get_Config, "/api/get_config")
api.add_resource(Courses, "/api/courses")
