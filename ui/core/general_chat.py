import streamlit as st
from llms.router import ask_model


def general_chat_page(model):

    st.title("💬 General Chat")

    st.write("Chat with Gemini or Claude.")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display previous messages
    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(message)

    # Chat input
    prompt = st.chat_input("Type your message...")

    if prompt:

        # Show user message
        st.session_state.chat_history.append(("user", prompt))

        with st.chat_message("user"):
            st.markdown(prompt)

        # Get AI response
        with st.spinner("Thinking..."):
            response = ask_model(model, prompt)

        # Show AI response
        st.session_state.chat_history.append(("assistant", response))

        with st.chat_message("assistant"):
            st.markdown(response)

    # Clear chat button
    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()