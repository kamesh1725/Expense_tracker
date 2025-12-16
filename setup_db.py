
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def setup_database():
    try:
        # Connect to MySQL Server (without database)
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "")
        )
        cursor = conn.cursor()

        # Create Database
        db_name = os.getenv("DB_NAME", "expense_tracker")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database '{db_name}' ready.")

        # Connect to the database
        conn.database = db_name

        # Create Table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            category VARCHAR(100) NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            edate DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_table_query)
        print("Table 'expenses' ready.")

        conn.close()
        print("Setup completed successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    setup_database()
