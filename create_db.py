import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
load_dotenv()

def create_connection(host_name, user_name, user_password):
  connection = None

  try:
    connection = mysql.connector.connect(
      host = host_name,
      user = user_name,
      password = user_password
    )

    print("Connection to MySQL DB successful.")
  except Error as e:
    print(f"Error: {e} occurred")

  return connection

# Can be done manually, doing for learning purposes
def create_db(connection, query):
  cursor = connection.cursor()

  try:
    cursor.execute(query)
    print("Database created successfully")
  except Error as e:
    print(f"Error: {e} occurred")
  finally:
    cursor.close()

def main():
  
  MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
  conn = create_connection('localhost', 'root', MYSQL_ROOT_PASSWORD)

  if conn:
    create_db_query = "CREATE DATABASE coding2025"
    create_db(conn, create_db_query)
    conn.close()
    print("MySQL connection is closed.")

if __name__ == "__main__":
  main()