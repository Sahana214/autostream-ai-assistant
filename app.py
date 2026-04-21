import streamlit as st
from agent import agent_response
from state import AgentState

st.set_page_config(page_title="AutoStream AI Agent", page_icon="🎬")
st.title("🎬 AutoStream AI Assistant")
if "agent_state" not in st.session_state:
    st.session_state.agent_state = AgentState()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask about AutoStream...")
if user_input:
    response = agent_response(user_input, st.session_state.agent_state)
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("assistant", response))
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(msg)
