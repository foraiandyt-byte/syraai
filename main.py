import streamlit as st
from google import genai

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Syrah.ace")
st.subheader("AI coding expert")

user_input = st.text_input("Type your doubt about coding:")
prompt = st.chat_input(
 accept_file=True, 
 file_type=[".txt", ".py", ".html"]
)
if prompt and prompt.text:
    st.markdown(prompt.text)


if st.button("Send") and user_input:
    
    st.session_state.chat_history.append(f"You: {user_input}")
    
    client = genai.Client(api_key="AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw")  
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"Error: {e}"
 
    st.session_state.chat_history.append(f"Syrah: {bot_reply}")

for msg in st.session_state.chat_history:
    st.write(msg)
