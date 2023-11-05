import streamlit as st
import pandas as pd
#st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/me.jpg")

with col2:
    st.title("Aadhar Kaushik")
    content = """Hi, I am Aadhar! I am an AI/ML engineer. I graduated in 2020 from SRM University Delhi-NCR in the 
    field of Computer Science and Engineering. I have a masters degree in the specialisation of Artificial 
    Intelligence/Machine Learning. I am also a mentor at Mentors Without Borders where I teach python programming 
    language to underprivileged students on a global level."""
    st.info(content)

content2 = """
In this website you can find the applications I have built in Python. For any query feel free to contact me.
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code] ({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code] ({row['url']})")
