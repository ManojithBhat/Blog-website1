import mysql.connector
import os

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='sql2manojithblore',
    auth_plugin='mysql_native_password'
)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE post")

# my_cursor.execute("DROP DATABASE post")

my_cursor.execute("SHOW DATABASES")

print(os.environ.get('DB_USER_1'))

for db in my_cursor:
    print(db)