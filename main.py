import streamlit as st
from google import genai

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Syrah.ace")
url = "https://chatgpt.com/backend-api/estuary/content?id=file_00000000b1d461fa84b416f85600914d&ts=489301&p=fs&cid=1&sig=beda5c837fe0acd1b9407346bf90ff37c5108b1b3cb39a463d2f6cf8ab71d3e5&v=0"
st.subheader("AI coding expert")

user_input = st.text_input("Type your doubt about coding:")

if st.button("Send") and user_input:
    # Add user message to chat history
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
