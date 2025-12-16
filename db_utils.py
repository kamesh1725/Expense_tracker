import pandas as pd
import dbconnect as dc

def execute_query(query, params=None):
    try:
        conn = dc.test_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error executing query:", e)

def fetch_data(query, params=None):
    try:
        conn = dc.test_connection()
        df = pd.read_sql(query, conn, params=params)
        conn.close()
        return df
    except Exception as e:
        print("Error fetching data:", e)
        return pd.DataFrame()
