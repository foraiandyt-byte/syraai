import streamlit as st
from google import genai
from PIL import Image
# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Syrah.ace")
st.subheader("AI coding expert")
prompt = st.chat_input(
    "Say something and/or attach an image",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
)
if prompt and prompt.text:
    st.markdown(prompt.text)
st.session_state.chat_history.append(f"You: {prompt}")
    
client = genai.Client(api_key="AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw")  
try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=st.chat_input
        )
        bot_reply = response.text
except Exception as e:
        bot_reply = f"Error: {e}"
        st.session_state.chat_history.append(f"Bot: {bot_reply}")


for msg in st.session_state.chat_history:
    st.write(msg)
