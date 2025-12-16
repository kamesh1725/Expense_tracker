# 💸 Expense Tracker (Streamlit + MySQL)

A multipage expense tracking web app built with **Streamlit** and **MySQL**.  
Easily track your expenses, analyze spending patterns, and visualize data with interactive charts.

## 🚀 Features
- ✅ Add, search, and view expenses
- ✅ Interactive charts (Pie, Bar, Line)
- ✅ Expense statistics & metrics
- ✅ MySQL database backend
- ✅ Streamlit multipage UI

## 📂 Project Structure
ExpenseTracker/

├── Home.py # Main dashboard

├── Pages/

│ ├── 1_Add_Expense.py # Add expense

│ ├── 2_View_Expense.py # View expenses based on category

│ ├── 3_View_All_Expenses.py # View all expenses

│ ├── 4_Charts.py # Charts

│ └── 5_Stats.py # Statistics

├── db_utils.py # Query handling

├── dbconnect.py # MySQL connection

├── requirements.txt

└── README.md

## 🛠️ Tech Stack
- **Frontend/UI:** Streamlit
- **Database:** MySQL
- **Data Analysis:** Pandas, Plotly

## 🔗 Database Setup
1. Create database:

CREATE DATABASE expense_tracker;

2. Create table:

CREATE TABLE expenses (

    id INT AUTO_INCREMENT PRIMARY KEY,
    
    title VARCHAR(255),
    
    category VARCHAR(100),
    
    amount DECIMAL(10,2),
    
    eDate DATE
    
);

## 🔐 Environment Variables
Create a `.env` file in the root folder:

DB_HOST=localhost

DB_USER=root

DB_PASSWORD=yourpassword

DB_NAME=dbexpense

## ▶️ Running Locally

pip install -r requirements.txt

streamlit run Home.py

## 📸 Screenshots

### 🏠 Home Page
![Home](screenshots/Home.png)

### ➕ Add Expense Page
![Add Expense 1](screenshots/AddExpense1.png)
![Add Expense 2](screenshots/AddExpense2.png)

### 📂 View Expenses by category Page
![View Expense](screenshots/ViewExpense.png)

### 📂 View All Expenses Page
![View All Expense](screenshots/ViewAllExpense.png)

### 📊 Charts Page
![Charts 1](screenshots/Charts1.png)
![Charts 2](screenshots/Charts2.png)
![Charts 3](screenshots/Charts3.png)

### 📈 Stats Page
![Stats 1](screenshots/Stats1.png)
![Stats 2](screenshots/Stats2.png)
![Stats 3](screenshots/Stats3.png)
![Stats 4](screenshots/Stats4.png)
![Stats 5](screenshots/Stats5.png)

👤 Developer

Built by kamesh p
🔗 [Linkedin](https://www.linkedin.com/in/kamesh001/)

🔗 [GitHub](https://github.com/kamesh1725)
