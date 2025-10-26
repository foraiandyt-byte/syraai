import streamlit as st
from google import genai

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Syrah.ace")
st.subheader("AI coding expert")

user_input = st.text_input("Type your doubt about coding:")

if st.button("Send") and user_input:
    # Add user message to chat history
    st.session_state.chat_history.append(f"You: {user_input}")

     with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = random.choice(
    

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
