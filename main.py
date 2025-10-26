import streamlit as st
import google.genai as genai

client = genai.Client(api_key="AIzaSyALEjQpQpIEtZcEHCYrGOizaVITtD0Atxw")  
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye! 👋")
        break

    try:
        # Generate response using Gemini model
        response = client.models.generate_content(
            model="gemini-2.5-flash",   # You can change to "gemini-1.5-pro" for deeper answers
            contents=user_input
        )

        print("Chatbot:", response.output_text)

    except Exception as e:
        print(f"⚠️ Error: {e}")

st.set_page_config(page_title="Syrah AI", page_icon="")
st.title("🤖 Syrah.ace")
st.write("AI coding expert (ace)!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_message = st.chat_input("Ask anything about coding...")

if user_message:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_message})
    st.chat_message("user").write(user_message)

    response = model.generate_content(user_message)
    bot_reply = response.text


    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.chat_message("assistant").write(bot_reply)
