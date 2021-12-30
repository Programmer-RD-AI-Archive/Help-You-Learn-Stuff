import pyodbc
import textwrap
import binascii

# Specify the Driver.

driver = "{ODBC Driver 17 for SQL Server}"  # or driver 17
# Specify the Server name and the DB name

server_name = "help-you-learn-stuff"
database_name = "Help-You-Learn-Stuff"


# Password - Programmer-RD-AI
# Server admin login = ranuga2008
server = f"{server_name}.database.windows.net,1433"

# Define User Name
username = "help-you-learn-stuff"
password = "ranuga-2008"

# Create the full connection str

connection_str = textwrap.dedent(
    f"""
                                 Driver={driver};
                                 Server={server};
                                 Database={database_name};
                                 Uid={username};
                                 Pwd={password};
                                 Encrypt=yes;
                                 TrustServerCertificate=no;
                                 Connection Timeout=30;
                                 """
)

print(connection_str)

# Create a new PYOCDC connection object

cnxn: pyodbc.Connection = pyodbc.connect(connection_str)

# Create a new Cursor from the connection

crsr: pyodbc.Cursor = cnxn.cursor()
f = open(
    f"./azure_sql.py",
    "rb",
)
f = '0x' + binascii.hexlify(f.read()).decode('utf-8')
print(f)
# Dine a select query
select_sql = "CREATE TABLE TEST (A varbinary(max),B varchar(50))"
result = crsr.execute(select_sql)
select_sql = f"""
INSERT INTO
    [TEST](
        [A],
        [B]
    )
VALUES
    (
        {f},
        'Jane'
    )
"""
result = crsr.execute(select_sql)
select_sql = "SELECT * FROM TEST"
result = crsr.execute(select_sql)
print(crsr.fetchall())

cnxn.close()
