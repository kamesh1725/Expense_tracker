
import mysql.connector
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "expense_tracker")
    )

def verify_data():
    conn = get_connection()
    
    # Check total count
    query_count = "SELECT COUNT(*) FROM expenses"
    cursor = conn.cursor()
    cursor.execute(query_count)
    count = cursor.fetchone()[0]
    print(f"Total expenses: {count}")
    
    # Check categories
    query_cat = "SELECT category, count(*) FROM expenses GROUP BY category"
    df = pd.read_sql(query_cat, conn)
    print("\nExpenses by Category:")
    print(df)
    
    conn.close()

if __name__ == "__main__":
    verify_data()
