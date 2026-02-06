import streamlit as st
from  ollama import thefun
import requests
import json

# Set the page configuration
st.set_page_config(
    page_title="chatbot"
)


if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(
        {
            "role" : "assistant",
            "content" : "hello, I am a chatbot How can i help you"
        }
    )

if 'is_typing' not in st.session_state:
    st.session_state.is_typing = False

st.title("my own chatbot")
st.markdown("This is a simple chatbot application built with Streamlit.")

st.caption("cahtbot is ready to answer your questions   ")

for message in st.session_state.messages:
    if message["role"] == "user":
        st.info(message["content"])
    else:
        st.success(message["content"])


if st.session_state.is_typing:
    st.markdown("bot is typing...")
    st.warning("typing...")

st.markdown("---")
st.subheader("your message  ")

with st.form(key = "chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here:")
    submit_button = st.form_submit_button(label="send message")

if submit_button and user_input.split():
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
  )
    st.session_state.is_typing = True
    st.rerun()
if st.session_state.is_typing:
    user_message = st.session_state.messages[-1]["content"]
    bot_response = thefun(user_message)
    st.session_state.messages.append(
        {
            "role" : "assistant",
            "content" : bot_response
        }
    )
    st.session_state.is_typing = False
    st.rerun()
