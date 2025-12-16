import db_utils as db
import streamlit as st
import pandas as pd

def show_data():
    query="Select * from expenses order by eDate desc"
    return db.fetch_data(query)

st.title("View Expense History")
df=show_data()
if df.empty:
    st.info("No matching expenses found.")
else:
    st.dataframe(df)
