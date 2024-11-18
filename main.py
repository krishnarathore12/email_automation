import streamlit as st
import pandas as pd

from utils import get_placeholders
from send_mail import process_and_send_emails




# api_key = st.sidebar.text_input("OPENAI_API_KEY", )
sender_email = st.sidebar.text_input("Sender's E-mail")
password = st.sidebar.text_input("Password")
dataframe = pd.DataFrame()
smtp_server = "smtp.office365.com"
port = 587

placeholders = []

st.header("Email-Automation")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    dataframe.to_csv('data.csv', index=False)
    st.write(dataframe)
    placeholders = get_placeholders(dataframe)
    st.write("Placeholders in the CSV")
    st.write(placeholders)

# default_prompt = get_default_prompt(placeholders)

default_prompt = "You are a expert in writing emails, you are given following placeholders in the email:"
for i in placeholders:
    default_prompt += i + " "

prompt = st.text_input("System Prompt", default_prompt)

if st.button("Send Mails", type = 'primary'):
    process_and_send_emails( sender_email, password, dataframe, smtp_server, port )
    st.write("Emails successfully send!")




