import streamlit as st
from helper import *

st.set_page_config(
    page_title="בוט שיעורי בית"
)

st.title("בוט שיעורי בית")

api_key = loadAPIKey()


showMessage("AI","היי אני כאן כדי לעזור לך")

user = st.chat_input("ההודעה שלך...")

if user:
    showMessage("user",user)