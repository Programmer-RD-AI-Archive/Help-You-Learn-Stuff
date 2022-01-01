from API import *



class Azure_SQL:
    try:
        f = open(
            f"./azure_sql.py",
            "rb",
        )
        f = "0x" + binascii.hexlify(f.read()).decode("utf-8")
    except:
        f = "0x123456987"

    def __init__(
        self,
        driver: str = "{ODBC Driver 17 for SQL Server}",
        server_name: str = "help-you-learn-stuff",
        database_name: str = "Help-You-Learn-Stuff",
        username: str = "help-you-learn-stuff",
        password: str = "ranuga-2008",
        connection_timeout: int = 30,
    ) -> None:
        self.driver = driver
        self.server_name = server_name
        self.database_name = database_name
        self.server = f"{self.server_name}.database.windows.net,1433"
        self.username = username
        self.password = password
        self.connection_timeout = connection_timeout
        self.connection_str = textwrap.dedent(
            f"""
                                 Driver={self.driver};
                                 Server={self.server};
                                 Database={self.database_name};
                                 Uid={self.username};
                                 Pwd={self.password};
                                 Encrypt=yes;
                                 TrustServerCertificate=no;
                                 Connection Timeout={30};
                                 """
        )
        print(self.connection_str)
        self.cnxn: pyodbc.Connection = pyodbc.connect(self.connection_str)
        self.crsr: pyodbc.Cursor = self.cnxn.cursor()

    def create_new_table(
        self, table_query: str = "CREATE TABLE TEST (A varbinary(max),B varchar(50))"
    ):
        print("Creating New Table")
        result = self.crsr.execute(table_query)
        self.crsr.commit()
        return result

    def insert_to_table(
        self, insert_query: str = f"INSERT INTO [TEST]( [A], [B] ) VALUES ( {f}, 'Jane')"
    ):
        print("Insert to Table")
        result = self.crsr.execute(insert_query)
        self.crsr.commit()
        return result

    def select_table(self, select_query: str = "SELECT * FROM TEST"):
        print("Select Table")
        result = self.crsr.execute(select_query)
        return self.crsr.fetchall()

    def close_connection(self) -> bool:
        print("Closing Connection")
        try:
            self.cnxn.close()
            return True
        except:
            return False

    def reconnect_connection(self) -> bool:
        print("Reconnecting Connection")
        try:
            self.cnxn: pyodbc.Connection = pyodbc.connect(self.connection_str)
            return True
        except:
            return False

    def reconnect_cursor(self) -> bool:
        print("Reconnecting Cursor")
        try:
            self.crsr: pyodbc.Cursor = self.cnxn.cursor()
            return True
        except:
            return False

    def get_tables(self):
        new_tables = []
        tables = self.select_table("SELECT table_name FROM information_schema.tables")
        for table in tables:
            new_tables.append(table[0])
        return new_tables
