import streamlit as st
from google import genai

genai.configure(api_key="AIzaSyArI5AG69nKu8eIhUiPWsCORf-JKJcLyXA")
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="Syrah AI", page_icon="")
st.title("🤖 Syrah.ace")
st.write("AI coding expert (ace)!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_message = st.chat_input("Ask anything about coding...")

if user_message:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_message})
    st.chat_message("user").write(user_message)

    response = model.generate_content(user_message)
    bot_reply = response.text


    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.chat_message("assistant").write(bot_reply)
