from platform import system

import streamlit as st
from helper import * #תביא את כל הפונקציות מהקובץ המשותף

st.set_page_config(
    page_title="בוט שיעורי בית",
    page_icon="🤓"
)

st.title("בוט שיעורי בית")

api_key = loadAPIKey() #מביא את הפונקציה מהקובץ

#הודעה ראשונה מהצ'אט
showMessage("AI","היי אני כאן כדאי לעזור לך")

#אם לא הגדרנו את הפרויקט - צור אותו בזיכרון
if "homework" not in st.session_state:
    newPage("homework")

system_prompt = """"

    #תפקיד
    אתה עוזר בשיעורי בית
    
    #משימה
    התפקיד שלך - להסביר לי את החומר
    אם אתה לא יודע - תגיד שאתה לא יודע או תחפש באינטרנט
    תסביר ברור
    
    #מגבלות
    **לא להמציא תשובה**
    תכתוב תשובה בצורה אנושית
    תכתוב תשובה מלאה
    ** אם השתמשת בכלי (tool) תכתוב את התוצאה **


"""

history = st.session_state["homework"]["history"]
for line in history:
    sender = line["role"]
    if sender == "model": #ג'מיני מצפה לקבל model
        sender = "ai" #streamlit מצפה לקבל AI

    text = line["parts"][0]["text"] #פשוט מוציאים את הטקסט מהמבנה של ג'מיני
    showMessage(sender,text)

#מקום להקליד
user = st.chat_input("ההודעה שלך...")

if user: #אם יש הודעה

    showMessage("user",user)
    #שולפים את ההיסטוריה

    save_to_history("homework","user",user)
    history = st.session_state["homework"]["history"]
    answer = sendMessage(user,system_prompt,history) #לשלוח לAI את ההודעה

    showMessage("ai",answer) #תראה את התשובה

    save_to_history("homework","model",answer)


