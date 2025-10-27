import streamlit as st
from google import genai

st.title("Syrah")
st.subheader("Made by Team Syrah (VBB 2025)! ace stands for AI coding Tutor")
user_input = st.chat_input(
    (f"You: {user_input}")
    client = genai.Client(api_key="AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw") 
    from google import genai
    client = genai.Client(api_key="AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw") 
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(user_input)
    bot_reply = response.text
    (f"Bot: {bot_reply}")
    print(bot_reply)
