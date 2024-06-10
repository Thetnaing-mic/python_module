import os
import pyodbc
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

db_server = os.getenv('SERVER')
db_database = os.getenv('DATABASE')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')


connection_string = (
    f'DRIVER={{SQL Server}};'
    f'SERVER={db_server};'
    f'DATABASE={db_database};'
    f'UID={db_user};'
    f'PWD={db_password};'
)

conn = pyodbc.connect(connection_string)

cursor = conn.cursor()
print(conn)
# cursor.execute("SELECT * FROM mic_company")

# for row in cursor:
#     print(row)

# df = pd.read_sql("SELECT * FROM mic_company", conn)
# print(df)



# # # cursor.execute("DELETE FROM mic_company WHERE id = 7")

# Define the SQL query to create the user table
# create_table_query = '''
# CREATE TABLE Users (
#     ID INT PRIMARY KEY IDENTITY,
#     名前 VARCHAR(255),
#     年齢 INT
# )
# '''

# cursor.execute(create_table_query)

# cursor.execute("INSERT INTO Users(name, age) VALUES ('Thetnaing', 29)")

# cursor.execute("UPDATE Users SET 年齢 = 39 WHERE id = 2")

df = pd.read_sql("SELECT * FROM Users", conn)

print(df)


# conn.commit()
cursor.close()
conn.close()
