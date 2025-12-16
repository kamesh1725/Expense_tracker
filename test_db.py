
import dbconnect as dc

print("Testing database connection...")
conn = dc.test_connection()
if conn:
    print("Connection Successful!")
    conn.close()
else:
    print("Connection Failed.")
