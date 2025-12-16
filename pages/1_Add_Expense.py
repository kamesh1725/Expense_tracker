import db_utils as db
import streamlit as st
import pandas as pd

def save_expense(_title,_category,_amount,_edate):
    query="Insert into expenses(title,category,amount,edate) values(%s,%s,%s,%s)"
    params=(_title,_category,_amount,_edate)
    db.execute_query(query,params)
    st.success("Expense Added")

def show_data():
    query="Select * from expenses order by eDate desc"
    return db.fetch_data(query)

st.title("Add Expense")
st.subheader("Maintain Daily Expense")

with st.form("Expenseform"):
    title=st.text_input("Expense Title","",placeholder="Enter Expense")
    category=st.selectbox("Expense Category",["Food","Travel","Rent","Shopping","Others"])
    amount=st.number_input("Expense Amount",min_value=0,max_value=10000000)
    edate=st.date_input("Expense Date")
    submit=st.form_submit_button("Save")
    
    if submit:
        if not title.strip():
            st.error("Expense title is required!")
        elif amount == 0:
            st.error("Amount should be greater than 0.")
        else:
            save_expense(title,category,amount,edate)
            st.rerun()

df=show_data()
st.subheader("Last 5 Expenses Added")
st.dataframe(df.head(5))