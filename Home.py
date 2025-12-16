import streamlit as st
from datetime import datetime
import db_utils as db
import pandas as pd

st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="centered")

# --- Title & Intro ---
st.title("💸 Personal Expense Tracker")
st.subheader("Welcome!")
st.markdown("Track your expenses effortlessly and stay financially aware.")

# --- Stats Section ---
query = "SELECT COUNT(*) as count, SUM(amount) as total FROM expenses"
df_stats = db.fetch_data(query)

query_cat = """
    SELECT category, COUNT(*) as entries 
    FROM expenses 
    GROUP BY category 
    ORDER BY entries DESC 
    LIMIT 1
"""
df_cat = db.fetch_data(query_cat)

col1, col2, col3 = st.columns(3)
col1.metric("🧾 Transactions", int(df_stats['count'][0]) if not df_stats.empty else 0)
col2.metric("💰 Total Spent", f"₹{float(df_stats['total'][0]):,.2f}" if pd.notna(df_stats['total'][0]) else "₹0.00")
col3.metric("🔥 Most Used Category", df_cat['category'][0] if not df_cat.empty else "N/A")

st.info(f"📅 Today is **{datetime.now().strftime('%A, %d %B %Y')}**")

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 13px;'>
        Built with ❤️ using Streamlit © 2025 | Developed by <b>Harini Neon</b> | 
        <a href='https://www.linkedin.com/in/shree-harini-k-m-a35a42250/' target='_blank'>LinkedIn</a> | 
        <a href='https://github.com/Harinineon' target='_blank'>GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
