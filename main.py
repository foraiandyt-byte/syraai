import streamlit as st
from google.genai import genai
st.title=("Syrah")
st.subheader=("Made by Team 21 VBB 2025")
genai.configure(api_key="AIzaSyArI5AG69nKu8eIhUiPWsCORf-JKJcLyXA")
model=genai.GenerativeModel("gemini-2.5-flash")
prompt = st.chat_input("What would you like to ask?")

if prompt:
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = model.generate_content(prompt)
                
                if response and response.text:
                    ai_response = response.text
                    st.markdown(ai_response)
                    st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                else:
                    st.error("The model did not return a valid response.")
    
    except Exception as e:
        st.error(f"An error occurred while generating the response: {e}")

                            
