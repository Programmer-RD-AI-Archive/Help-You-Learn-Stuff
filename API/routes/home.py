from API import *
from API.help_funcs import send_email
from API.db.azure_sql import Azure_SQL

contact_us_request_parser = reqparse.RequestParser()
contact_us_request_parser.add_argument("email", type=str, help="email is required", required=True)
contact_us_request_parser.add_argument(
    "question", type=str, help="question is required", required=True
)


class Contact_Us(Resource):
    def post(self):
        try:
            args = contact_us_request_parser.parse_args()
            email = args["email"]
            question = args["question"]
            print(email, question)
            send_email(subject=question, message=f"Email - {email} \n Question {question}")
            print("Email Send")
            asql = Azure_SQL()
            tables = asql.get_tables()
            if "Contact_Us" not in tables:
                asql.create_new_table(
                    "CREATE TABLE Contact_Us (Email varchar(max),Question varchar(max))"
                )
            asql.insert_to_table(
                f"INSERT INTO [Contact_Us]( [Email], [Question] ) VALUES ( '{email}', '{question}')"
            )
            # Added DB
            return {"message": True}
        except:
            return {"message": False}


api.add_resource(Contact_Us, "/api/Contact_Us")
accounts_request_parser = reqparse.RequestParser()
accounts_request_parser.add_argument("email", type=str, help="email is required", required=True)
accounts_request_parser.add_argument(
    "password", type=str, help="Password is required", required=True
)
accounts_request_parser.add_argument(
    "user name", type=str, help="user name is required", required=True
)


class Accounts(Resource):
    def get(self):
        asql = Azure_SQL()
        tables = asql.get_tables()
        if "Accounts" not in tables:
            asql.create_new_table(
                "CREATE TABLE Accounts (ID Email varchar(max),User_Name varchar(max), Password varchar(max))"
            )
        accounts = asql.select_table("SELECT * FROM Accounts")
        return {"message": accounts}

    def post(self):
        args = accounts_request_parser.parse_args()
        asql = Azure_SQL()
        tables = asql.get_tables()
        if "Accounts" not in tables:
            asql.create_new_table(
                "CREATE TABLE Accounts (Email varchar(max),User_Name varchar(max), Password varchar(max))"
            )
        asql.insert_to_table(
            f"INSERT INTO [Accounts]( [Email], [User_Name], [Password] ) VALUES ( '{args['email']}', '{args['user name']}', '{args['password']}')"
        )
