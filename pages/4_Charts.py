import db_utils as db
import pandas as pd
import streamlit as st
import plotly.express as px

st.title("📊 Expense Charts Dashboard")
st.write("Visualize your spending with interactive charts.")

# --- Pie Chart: Category-wise Distribution ---
category_query = """
    SELECT category, SUM(amount) as total
    FROM expenses GROUP BY category
"""
category_df = db.fetch_data(category_query)

if not category_df.empty:
    st.subheader("🧾 Category-wise Expense Distribution (Pie Chart)")
    fig_pie = px.pie(category_df, names='category', values='total', title="Expense Share by Category")
    st.plotly_chart(fig_pie, use_container_width=True)
else:
    st.info("No category data available for the pie chart.")

st.markdown("---")

# --- Bar Chart: Category-wise Comparison ---
bar_query = """
    SELECT category, SUM(amount) as amount
    FROM expenses GROUP BY category
"""
bar_df = db.fetch_data(bar_query)

if not bar_df.empty:
    st.subheader("📉 Category-wise Expense Comparison (Bar Chart)")
    st.bar_chart(bar_df, x="category", y="amount")
    
    st.subheader("📋 Category-wise Expense Table")
    st.dataframe(bar_df)
else:
    st.info("No data available for the bar chart.")
