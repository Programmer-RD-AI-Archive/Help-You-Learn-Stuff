from API import *
from API.help_funcs import send_email
from API.db.azure_sql import Azure_SQL

contact_us_request_parser = reqparse.RequestParser()
contact_us_request_parser.add_argument(
    "email", type=str, help="Password is required", required=True
)
contact_us_request_parser.add_argument(
    "question", type=str, help="Password is required", required=True
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
            asql.insert_to_table(
                f"INSERT INTO [Contact_Us]( [Email], [Question] ) VALUES ( '{email}', '{question}')"
            )
            # Added DB
            return {"message": True}
        except:
            return {"message": False}


api.add_resource(Contact_Us, "/api/Contact_Us")


class Sign_Up(Resource):
    def get(self):
        pass

    def post(self):
        pass
