import streamlit as st

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 My Sales Dashboard")

st.write("Welcome to my first Sales Dashboard!")

st.subheader("Sales Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", "Rs. 50,000")

with col2:
    st.metric("Total Orders", "120")

with col3:
    st.metric("Customers", "85")

st.success("My first Streamlit dashboard is ready!")