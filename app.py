import streamlit as st

st.title("Hello AI/ML from mobile!")
name = st.text_input("Your name")
if st.button("Greet"):
    st.success(f"Hi {name}, welcome to your first mobile-built app!")
