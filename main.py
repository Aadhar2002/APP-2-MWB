import streamlit as st

#st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/me.jpg")

with col2:
    st.title("Aadhar Kaushik")
    content = """Hi, I am Aadhar! I am an AI/ML engineer. I have a masters degree in the specialisation of Artificial 
    Intelligence/Machine Learning. I am also a mentor at Mentors Without Borders where I teach python programming 
    language to underprivileged students on a global level."""
    st.info(content)