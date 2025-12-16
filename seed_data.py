
import mysql.connector
import os
from dotenv import load_dotenv
from faker import Faker
import random
from datetime import datetime, timedelta

load_dotenv()
fake = Faker()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "expense_tracker")
    )

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    categories = ["Food", "Travel", "Rent", "Shopping", "Entertainment", "Utilities", "Health", "Education"]
    
    # Generate 50 sample expenses
    expenses = []
    print("Generating 50 professional sample expenses...")
    
    for _ in range(50):
        category = random.choice(categories)
        
        # Smart titles based on category
        if category == "Food":
            title = fake.random_element(elements=("Groceries at Wallmart", "Dinner at McD", "Lunch Cafe", "Starbucks Coffee", "Pizza Night"))
        elif category == "Travel":
            title = fake.random_element(elements=("Uber Ride", "Flight Ticket", "Gas Station", "Train Ticket", "Bus Pass"))
        elif category == "Rent":
            title = "Monthly Rent"
        elif category == "Shopping":
            title = fake.random_element(elements=("Amazon Purchase", "Nike Shoes", "New Jeans", "Electronics", "Gift for Mom"))
        elif category == "Entertainment":
            title = fake.random_element(elements=("Netflix Subscription", "Movie Night", "Concert Tickets", "Spotify Premium"))
        elif category == "Utilities":
            title = fake.random_element(elements=("Electricity Bill", "Water Bill", "Internet Bill", "Phone Recharge"))
        else:
            title = fake.sentence(nb_words=3).replace(".", "")

        amount = round(random.uniform(10, 5000), 2)
        
        # Random date in the last 60 days
        days_ago = random.randint(0, 60)
        edate = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')
        
        expenses.append((title, category, amount, edate))

    query = "INSERT INTO expenses (title, category, amount, edate) VALUES (%s, %s, %s, %s)"
    
    try:
        # Clear old data (optional, but good for clean slate)
        # cursor.execute("TRUNCATE TABLE expenses") 
        # print("Cleared existing data.")
        
        cursor.executemany(query, expenses)
        conn.commit()
        print(f"Successfully added {len(expenses)} professional sample expenses.")
    except Exception as e:
        print(f"Error seeding data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    seed_data()
