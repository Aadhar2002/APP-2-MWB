import streamlit as st
from contact_email import contact_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Enter your email address")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        contact_email(message)
        st.info("Your message was sent successfully")