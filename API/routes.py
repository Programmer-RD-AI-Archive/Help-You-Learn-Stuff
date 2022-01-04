from API import *

get_config_request_parser = reqparse.RequestParser()
get_config_request_parser.add_argument(
    "password", type=str, help="Password is required", required=True
)
contact_us_request_parser = reqparse.RequestParser()
contact_us_request_parser.add_argument("email", type=str, help="email is required", required=True)
contact_us_request_parser.add_argument(
    "question", type=str, help="question is required", required=True
)

accounts_request_parser = reqparse.RequestParser()
accounts_request_parser.add_argument("email", type=str, help="email is required", required=True)
accounts_request_parser.add_argument(
    "password", type=str, help="Password is required", required=True
)
accounts_request_parser.add_argument(
    "user_name", type=str, help="user name is required", required=True
)
cources = reqparse.RequestParser()
cources.add_argument("label", type=str, help="label is required", required=True)
cources.add_argument("content", type=str, help="content is required", required=True)
cources.add_argument("html", type=str, help="html is required", required=True)


class Get_Config(Resource):
    def get(self):
        args = get_config_request_parser.parse_args()
        if args["password"] == password:
            config = open("./API/config.json")
            config = json.load(config)
            return {"config": config}
        else:
            abort(401, message="Wrong password")


class Contact_Us(Resource):
    def post(self):
        try:
            args = contact_us_request_parser.parse_args()
            email = args["email"]
            question = args["question"]
            send_email(subject=question, message=f"Email - {email} \n Question {question}")
            asql = Azure_SQL()
            tables = asql.get_tables()
            if "Contact_Us" not in tables:
                asql.create_new_table(
                    "CREATE TABLE Contact_Us (ID int IDENTITY(1,1),  Email varchar(max),Question varchar(max))"
                )
            asql.insert_to_table(
                f"INSERT INTO [Contact_Us]( [Email], [Question] ) VALUES ( '{email}', '{question}')"
            )
            # Added DB
            return {"message": True}
        except Exception as e:
            return {"message": False}


class Accounts(Resource):
    def get(self):
        asql = Azure_SQL()
        tables = asql.get_tables()
        if "Accounts" not in tables:
            asql.create_new_table(
                "CREATE TABLE Accounts (ID int IDENTITY(1,1), Rank INT(max), Email varchar(max),User_Name varchar(max), Password varchar(max))"
            )
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
            asql.create_new_table(
                "CREATE TABLE Accounts (ID int IDENTITY(1,1), Rank INT(max), Email varchar(max),User_Name varchar(max), Password varchar(max))"
            )
        asql.insert_to_table(
            f"INSERT INTO [Accounts]( [Rank],[Email], [User_Name], [Password] ) VALUES ( 1,'{args['email']}', '{args['user_name']}', '{args['password']}')"
        )
        newaccounts = []
        accounts = asql.select_table("SELECT * FROM [Accounts]")
        for account in accounts:
            newaccounts.append(list(account))
        return {"message": newaccounts}


class Cources(Resource):
    def post(self):
        args = cources.parse_args()
        asql = Azure_SQL()
        tables = asql.get_tables()
        if "Questions" not in tables:
            asql.create_new_table(
                """
                CREATE TABLE Questions
                (
                    label varchar(max),
                    content varchar(max),
                    html varchar(max)
                )
                """
            )
        asql.insert_to_table(
            f"INSERT INTO [Questions]( [label], [content], [html] ) VALUES ( '{args['label']}', '{args['content']}', '{args['html']}')"
        )

api.add_resource(Contact_Us, "/api/Contact_Us")
api.add_resource(Accounts, "/api/Accounts")
api.add_resource(Get_Config, "/api/get_config")
