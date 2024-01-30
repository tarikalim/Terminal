import mysql.connector
from mysql.connector import Error

def connect_to_database(host_name, user_name, database_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            database=database_name
        )
        print("Connected.")
    except Error as e:
        print(f"Connection fail")

    return connection

host = "34.141.227.97"
user = "thinkpad"
database = "hepsiburada_db"

# Bağlantıyı dene
connection = connect_to_database(host, user, database)

# Bağlantıyı kapat
if connection:
    connection.close()
