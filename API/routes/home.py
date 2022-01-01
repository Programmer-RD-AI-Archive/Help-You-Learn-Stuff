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
    def get(self):
        args = contact_us_request_parser.parse_args()
        email = args["email"]
        question = args["question"]
        send_email(subject=question, message=f"Email - {email} \n Question {question}")
        asql = Azure_SQL()
        asql.insert_one(f"INSERT INTO [TEST]( [Email], [Question] ) VALUES ( {email}, {question})")
        
        return {"message": "Success"}


api.add_resource(Contact_Us, "/api/Contact_Us")
