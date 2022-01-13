from API import *

hp = Help_Funcs()
accounts_request_parser = reqparse.RequestParser()
accounts_request_parser.add_argument("email", type=str, help="email is required", required=True)
accounts_request_parser.add_argument(
    "password", type=str, help="Password is required", required=True
)
accounts_request_parser.add_argument(
    "user_name", type=str, help="user name is required", required=True
)
accounts_request_parser.add_argument("password_hash", type=str, required=True)


class Accounts(Resource):
    def get(self) -> dict:
        if args["password_hash"] == password:
            asql = Azure_SQL()
            hp.table_exists_or_not(
                "Accounts",
                "CREATE TABLE Accounts (ID int IDENTITY(1,1), Rank INT(max), Email varchar(max),User_Name varchar(max), Password varchar(max))",
            )
            newaccounts = []
            accounts = asql.select_table("SELECT * FROM [Accounts]")
            for account in accounts:
                newaccounts.append(list(account))
            return {"message": newaccounts}

    def post(self) -> dict:
        
        args = accounts_request_parser.parse_args()
        asql = Azure_SQL()
        hp.table_exists_or_not(
            "Accounts",
            "CREATE TABLE Accounts (ID int IDENTITY(1,1), Rank INT(max), Email varchar(max),User_Name varchar(max), Password varchar(max))",
        )
        asql.insert_to_table(
            f"INSERT INTO [Accounts]( [Rank],[Email], [User_Name], [Password] ) VALUES ( 1,'{args['email']}', '{args['user_name']}', '{args['password']}')"
        )
        newaccounts = []
        accounts = asql.select_table("SELECT * FROM [Accounts]")
        for account in accounts:
            newaccounts.append(list(account))
        return {"message": newaccounts}


api.add_resource(Accounts, "/api/Accounts")
