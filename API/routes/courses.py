from API import *

hp = Help_Funcs()
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


class Courses(Resource):
    def put(self) -> dict:
        args = courses.parse_args()
        asql = Azure_SQL()
        hp.table_exists_or_not(
            "Contact_Us",
            """
            CREATE TABLE Courses
            (
                [ID] int IDENTITY(1,1),
                [Whole_Content] varchar(max),
                [Info] varchar(max),
                [Image] varchar(max),
                [Name] varchar(max),
                [Marks] varchar(max)
            )
            """,
        )
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
        astorage.create_file(file_name_in_the_cloud=f"{id_new}-info.txt",
                             file_rb=info)
        hp.table_exists_or_not(
            "Contact_Us",
            """
            CREATE TABLE Courses
            (
                [ID] int IDENTITY(1,1),
                [Whole_Content] varchar(max),
                [Info] varchar(max),
                [Image] varchar(max),
                [Name] varchar(max),
                [Marks] varchar(max)
            )
            """,
        )
        asql.insert_to_table(f"""
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
            """)
        return {"message": True}


api.add_resource(Courses, "/api/courses")
