from API import *
from API.help_funcs import send_email
from example.azure_sql import Azure_SQL

contact_us_request_parser = reqparse.RequestParser()
contact_us_request_parser.add_argument(
    "email", type=str, help="Password is required", required=True
)
contact_us_request_parser.add_argument(
    "question", type=str, help="Password is required", required=True
)


class Get_Config(Resource):
    def get(self):
        args = contact_us_request_parser.parse_args()
        email = args["email"]
        question = args["question"]
        send_email(subject=question, message=f"Email - {email} \n Question {question}")
        asql = Azure_SQL()
        asql.create_new_table("CREATE TABLE Contact_Us_Questions (Email varchar(50), Question varchar(50))")
        


api.add_resource(Get_Config, "/api/get_config")
