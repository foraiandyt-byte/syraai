import streamlit as st
from google import genai

st.title("Syrah")
st.subheader("Made by Team Syrah (VBB 2025)! ace stands for AI coding Tutor")
user_input = st.chat_input(
    "Say something and/or attach an image",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
)
if user_input and user_input.text:
    st.markdown(user_input.text)
if user_input and user_input["files"]:
    st.image(user_input["files"][0])
    (f"You: {user_input}")
    client = genai.Client(api_key="AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw") 
try:
    from google import genai
    client = genai.Client(api_key="AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw") 
    model="gemini-2.5-flash"
    response=client.generate_content(
      model="gemini-2.5-flash",
      contents=user_input
        )
    bot_reply = response.text
except:
    (f"Bot: {bot_reply}")
    print(bot_reply)
