import streamlit as st
from google import genai

st.title("Neuro")
st.subheader("Made by Team Syrah (VBB 2025)! ace stands for AI coding Tutor")
user_input = st.chat_input(
    "Say something and/or attach an image",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
)
if prompt and prompt.text:
    st.markdown(prompt.text)
if prompt and prompt["files"]:
    st.image(prompt["files"][0])
(f"You: {user_input}")
client = genai.Client(api_key="AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw")  # ⬅️ Replace with your real Gemini API key   
response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=user_input
        )
bot_reply = response.text
(f"Bot: {bot_reply}")
print(bot_reply)
