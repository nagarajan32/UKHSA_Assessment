import pyodbc
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_connection():
    try:
        # Build connection string
        connection_string = (
            f"DRIVER={os.getenv('DRIVER')};"
            f"SERVER={os.getenv('SERVER_NAME')};"
            f"DATABASE={os.getenv('DATABASE')};"
            f"UID={os.getenv('USER')};"
            f"PWD={os.getenv('PASSWORD')}"
        )

        # Establish connection
        connection = pyodbc.connect(connection_string)

        # Test the connection
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()

        # If the above query succeeds, the connection is successful
        print("Connection to SQL Server is successful.")

        # Close the connection
        cursor.close()
        connection.close()

    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server: {e}")

if __name__ == "__main__":
    test_connection()
