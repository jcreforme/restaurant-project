import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "restaurant")
    )

def init_db():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT 1")
    cursor.close()
    connection.close()

# Test the database connection
def test_connection():
    try:
        connection = get_connection()
        print("Database connection successful!")
        connection.close()
    except mysql.connector.Error as err:
        print(f"Database connection failed: {err}")

# Run the test if this file is executed directly
if __name__ == "__main__":
    test_connection()