import streamlit as st
from google import genai

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Syrah.ace")
st.subheader("AI coding expert")

uploaded_file = st.file_uploader(
    "Upload a code file",
    type=["py", "js", "html", "css", "cpp", "java", "cs", "php", "txt"]
)
if uploaded_file:
    code = uploaded_file.getvalue().decode()
    st.code(code, language="python")

    if st.button("Fix Code"):
        # send 'code' to your AI fixer
        fixed_code = ai_fix_code(code)  # <-- your AI function
        st.code(fixed_code, language="python")

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
