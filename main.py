import streamlit as st
import google.generativeai as genai
import os

API_KEY = "AIzaSyCPSoTZUvlXRkKq0kK1snpO6Mpl-hKqcmo" 

try:
    genai.configure(api_key="AIzaSyCPSoTZUvlXRkKq0kK1snpO6Mpl-hKqcmo")
except Exception as e:
    st.error(f"Error configuring the Gemini API: {e}")
    st.stop()

try:
    model = genai.GenerativeModel('gemini-2.5-flash')
except Exception as e:
    st.error(f"Error initializing the generative model: {e}")
    st.stop()

st.set_page_config(
    page_title="Maverick.ace",
    page_icon="🇮🇳",
    layout="centered"
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Maverick.ace")
st.subheader("ace stands for AI coding expert")
st.caption("Powered by team Maverick VBB 25")

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
      
prompt = st.chat_input("What would you like to ask about coding?")

if prompt:
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    try:
        with st.chat_message("assistant"):
            # Show a "thinking" spinner while generating
            with st.spinner("Thinking..."):
                response = model.generate_content(prompt)
                
                if response and response.text:
                    ai_response = response.text
                    st.markdown(ai_response)
                    # Add AI response to chat history
                    st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                else:
                    st.error("The model did not return a valid response.")
    
    except Exception as e:
        st.error(f"An error occurred while generating the response: {e}")
