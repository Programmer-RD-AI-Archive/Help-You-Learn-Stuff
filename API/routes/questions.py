from API import *

hp = Help_Funcs()
questions = reqparse.RequestParser()
questions.add_argument("html",
                       type=str,
                       help="html is required",
                       required=True)
questions.add_argument("name",
                       type=str,
                       help="name is required",
                       required=True)


class Questions(Resource):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def get(self) -> dict:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        asql = Azure_SQL()
        tables = asql.get_tables()
        if "Questions" not in tables:
            asql.create_new_table("""
                CREATE TABLE Questions
                (
                    [ID] int IDENTITY(1,1),
                    [html] varchar(max),
                    [name] varchar(max),
                )
                """)
        return {"message": asql.select_table("SELECT * FROM Questions")}

    def post(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        args = questions.parse_args()
        asql = Azure_SQL()
        tables = asql.get_tables()
        if "Questions" not in tables:
            asql.create_new_table()
        hp.table_exists_or_not(
            "Questions",
            """
            CREATE TABLE Questions
            (
                [ID] int IDENTITY(1,1),
                [html] varchar(max),
                [name] varchar(max),
            )
            """,
        )
        asql.insert_to_table(
            f"INSERT INTO Questions (html, name) VALUES ('{args['html']}','{args['name']}');"
        )
        return {"message": True}


api.add_resource(Questions, "/api/questions")
