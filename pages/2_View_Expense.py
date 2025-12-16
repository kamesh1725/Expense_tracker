import db_utils as db
import streamlit as st
import pandas as pd

def show_data(_category):
    query="Select * from expenses where category like %s order by eDate desc"
    params=(f"{_category}%",)
    return db.fetch_data(query,params)

st.title("View Category wise Expense History")
with st.form("ViewExpenses"):
    searchval=st.text_input("Category",placeholder="Search by category name")
    searchButton=st.form_submit_button("Search")

    if searchButton:
        if not searchval.strip():
            st.warning("Please enter a category to search.")
        else:
            df=show_data(searchval)
            if df.empty:
                st.info("No matching expenses found.")
            else:
                st.dataframe(df)
    