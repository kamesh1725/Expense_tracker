import db_utils as db
import pandas as pd
import streamlit as st
import plotly.express as px

st.title("📈 Expense Statistics & Insights")
st.write("Track key metrics and analyze your spending trends.")

# Fetch all expense data
query = "SELECT * FROM expenses"
df = db.fetch_data(query)

if df.empty:
    st.warning("No expense data available. Please add some records.")
    st.stop()

# Convert date column
df["edate"] = pd.to_datetime(df["edate"])

# --- Basic KPIs ---
total_expense = df["amount"].sum()
avg_daily_expense = df.groupby("edate")["amount"].sum().mean()
category_sum = df.groupby("category")["amount"].sum()
top_category = category_sum.idxmax()
expensive_day = df.groupby("edate")["amount"].sum().idxmax()

st.metric("💰 Total Expense", f"₹{total_expense:.2f}")
st.metric("📆 Average Daily Expense", f"₹{avg_daily_expense:.2f}")
st.metric("🏆 Most Spent Category", top_category)
st.metric("📅 Most Expensive Day", expensive_day.strftime("%Y-%m-%d"))

st.markdown("---")

# --- Daily Expense Trend ---
st.subheader("📊 Daily Expenses Over Time")
daily_expenses = df.groupby("edate")["amount"].sum().reset_index()
fig_line = px.line(daily_expenses, x="edate", y="amount", markers=True, title="Daily Expense Trend")
st.plotly_chart(fig_line, use_container_width=True)

# --- Category-wise Bar Chart (for stats) ---
st.subheader("📌 Total Spending by Category")
category_df = category_sum.reset_index().rename(columns={"amount": "total"})
st.bar_chart(category_df, x="category", y="total")

# --- Weekday Spending (Pie Chart) ---
st.subheader("📅 Spending Distribution by Weekday")
df["weekday"] = df["edate"].dt.day_name()
weekday_df = df.groupby("weekday")["amount"].sum().reset_index()
fig_pie = px.pie(weekday_df, names="weekday", values="amount", title="Spending by Day of the Week")
st.plotly_chart(fig_pie, use_container_width=True)

# --- Cumulative Spending ---
st.subheader("📈 Cumulative Spending Over Time")
daily_expenses["running_total"] = daily_expenses["amount"].cumsum()
fig_cumulative = px.line(daily_expenses, x="edate", y="running_total", markers=True, title="Cumulative Expense Growth")
st.plotly_chart(fig_cumulative, use_container_width=True)

# --- Savings Suggestion ---
top_percent = (category_sum.max() / total_expense) * 100
if top_percent > 50:
    st.warning(f"⚠️ More than {top_percent:.1f}% of your expenses are in **{top_category}**. Try to control spending here.")
else:
    st.success("✅ Your expenses are relatively balanced across categories.")
