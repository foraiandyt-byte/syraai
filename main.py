import streamlit as st
from google import genai

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Neuro")
st.subheader("Made by Team Syrah (VBB 2025)! ace stands for AI coding Tutor")
user_input = st.chat_input("Type your message:")
if st.button("Send") and chat_input:
    st.session_state.chat_history.append(f"You: {user_input}")
    client = genai.Client(api_key="AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw")  # ⬅️ Replace with your real Gemini API key   
try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )
        bot_reply = response.text
except Exception as e:
        bot_reply = f"Error: {e}"
    st.session_state.chat_history.append(f"Bot: {bot_reply}")
for msg in st.session_state.chat_history:
    st.write(msg)
