import streamlit as st
from google import genai

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Syrah.ace")
st.subheader("AI coding expert")

user_input = st.text_input("Type your doubt about coding:")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if user_input := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)
        
    bot_reply = f"Echo: {user_input}"

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.write(bot_reply)
    
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

with st.chat_message("Syrah"):
    st.markdown(
        f"<div style='background:#222;color:#fff;padding:10px;border-radius:10px'>"
        f"{bot_reply}</div>",
        unsafe_allow_html=True
