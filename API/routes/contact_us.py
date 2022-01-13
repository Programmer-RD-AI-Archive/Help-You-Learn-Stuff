from API import *

hp = Help_Funcs()
contact_us_request_parser = reqparse.RequestParser()
contact_us_request_parser.add_argument("email", type=str, help="email is required", required=True)
contact_us_request_parser.add_argument(
    "question", type=str, help="question is required", required=True
)


class Contact_Us(Resource):
    def post(self) -> dict:
        try:
            args = contact_us_request_parser.parse_args()
            email = args["email"]
            question = args["question"]
            send_email(subject=question, message=f"Email - {email} \n Question {question}")
            asql = Azure_SQL()
            hp.table_exists_or_not(
                "Contact_Us",
                "CREATE TABLE Contact_Us (ID int IDENTITY(1,1),  Email varchar(max),Question varchar(max))",
            )
            asql.insert_to_table(
                f"INSERT INTO [Contact_Us]( [Email], [Question] ) VALUES ( '{email}', '{question}')"
            )
            # Added DB
            return {"message": True}
        except Exception as e:
            return {"message": False}


api.add_resource(Contact_Us, "/api/Contact_Us")
