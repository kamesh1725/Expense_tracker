from dotenv import load_dotenv
load_dotenv()

import mysql.connector
import os

def test_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "expense_tracker")
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Database connection failed: {e}")
        return None
