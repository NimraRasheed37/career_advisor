# streamlit version is not ready yet, still needs fixing


import streamlit as st
from agents import Runner
from advisor.career_agent import career_agent
from config import gemini_config
import asyncio

st.set_page_config(page_title="Career Mentor", page_icon="🎓")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🎓 Career Mentor")
st.caption("Hi! I'm your Career Mentor. Let's explore your interests and skills!")

# 🟦 Display chat history above the input
for chat in st.session_state.history:
    with st.chat_message("user" if chat["role"] == "user" else "assistant"):
        st.markdown(chat["content"])

# 🟨 Input section at the bottom
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Your message", placeholder="e.g. I like computers and writing", label_visibility="collapsed")
    submitted = st.form_submit_button("Send")

# 🟩 Handle input after form submission
if submitted and user_input:
    # Add user's message
    st.session_state.history.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("💭 Thinking..."):
            try:
                result = asyncio.run(Runner.run(
                    career_agent,
                    st.session_state.history,
                    run_config=gemini_config
                ))

                output = result.final_output
                st.markdown(output)
                st.session_state.history.append({"role": "assistant", "content": output})
            except Exception as e:
                error_message = f"❌ Error: {e}"
                st.markdown(error_message)
                st.session_state.history.append({"role": "assistant", "content": error_message})
