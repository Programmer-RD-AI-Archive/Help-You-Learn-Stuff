import binascii
import textwrap

import pyodbc


class Azure_SQL:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    try:
        f = open(
            "./azure_sql.py",
            "rb",
        )
        f = "0x" + binascii.hexlify(f.read()).decode("utf-8")
    except Exception as e:
        warnings.filterwarnings(e)
        f = "0x123456987"

    def __init__(
        self,
        driver: str = """{ODBC Driver 17 for SQL Server}""",
        server_name: str = """help-you-learn-stuff""",
        database_name: str = """Help-You-Learn-Stuff""",
        username: str = """help-you-learn-stuff""",
        password: str = """ranuga-2008""",
        connection_timeout: int = 30,
    ) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.driver = driver
        self.server_name = server_name
        self.database_name = database_name
        self.server = f"""{self.server_name}.database.windows.net,1433"""
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
        self.cnxn: pyodbc.Connection = pyodbc.connect(self.connection_str)
        self.crsr: pyodbc.Cursor = self.cnxn.cursor()

    def create_new_table(
        self,
        table_query: str = """CREATE TABLE TEST (A varbinary(max),B varchar(50))""",
    ) -> bool:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        try:
            self.crsr.execute(table_query)
            self.crsr.commit()
            return True
        except Exception as e:
            warnings.filterwarnings(e)
            return False

    def insert_to_table(
        self,
        insert_query: str = f"""INSERT INTO [TEST]( [A], [B] ) VALUES ( {f}, 'Jane')""",
    ) -> bool:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        try:
            self.crsr.execute(insert_query)
            self.crsr.commit()
            return True
        except Exception as e:
            warnings.filterwarnings(e)
            return False

    def select_table(self, select_query: str = """SELECT * FROM TEST""") -> list:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        try:
            self.crsr.execute(select_query)
            results = []
            for result in self.crsr.fetchall():
                results.append(list(result))
            return results
        except Exception as e:
            warnings.filterwarnings(e)
            return []  # TODO

    def close_connection(self) -> bool:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        try:
            self.cnxn.close()
            return True
        except Exception as e:
            warnings.filterwarnings(e)
            return False

    def reconnect_connection(self) -> bool:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        try:
            self.cnxn: pyodbc.Connection = pyodbc.connect(self.connection_str)
            return True
        except Exception as e:
            warnings.filterwarnings(e)
            return False

    def reconnect_cursor(self) -> bool:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        try:
            self.crsr: pyodbc.Cursor = self.cnxn.cursor()
            return True
        except Exception as e:
            warnings.filterwarnings(e)
            return False

    def get_tables(self) -> list:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        try:
            new_tables = []
            tables = self.select_table("""SELECT table_name FROM information_schema.tables""")
            for table in tables:
                new_tables.append(table[0])
            return new_tables
        except Exception as e:
            warnings.filterwarnings(e)
            return []
