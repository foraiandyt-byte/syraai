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
    
def ai_code_fix(code_str):
    client = genai.Client(api_key="AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw")  
    fixed_code = "# AI fixed code\n" + code_str
    return fixed_code
    uploaded_file = st.file_uploader("Upload Python code", type=["py"])

if uploaded_file:
    # Read file content
    code = uploaded_file.getvalue().decode()
    
    st.subheader("Original Code")
    st.code(code, language="python")
    
    # AI processes the uploaded code
    fixed_code = ai_fix_code(code)
    
    st.subheader("AI Fixed Code")
    st.code(fixed_code, language="python", "java", "C", "C++")

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
