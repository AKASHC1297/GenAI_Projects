import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from langchain_core.messages import AIMessage, HumanMessage

from utils.config import load_environment
from tools.tools import get_tools
from agents.search_agent import build_agent
from ui.chat_ui import stream_agent_response


load_environment()

st.set_page_config(page_title="LangChain Search Engine", page_icon="🔎")

st.title("LangChain - Chat with Search")
st.caption("Powered by Groq · Wikipedia · Arxiv · DuckDuckGo")

with st.sidebar:

    st.header("Settings")

    api_key = st.text_input(
        "Groq API Key",
        type="password"
    )

    st.divider()

    st.markdown("Active Tools")
    st.markdown("DuckDuckGo")
    st.markdown("Wikipedia")
    st.markdown("Arxiv")

    st.divider()

    st.code("openai/gpt-oss-20b")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "display_messages" not in st.session_state:
    st.session_state["display_messages"] = [
        {"role": "assistant", "content": "Hi! I'm a search-powered chatbot."}
    ]

for msg in st.session_state.display_messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask anything..."):

    if not api_key:
        st.error("Enter Groq API Key")
        st.stop()

    st.session_state.messages.append(HumanMessage(content=prompt))
    st.session_state.display_messages.append(
        {"role": "user", "content": prompt}
    )

    st.chat_message("user").write(prompt)

    tools = get_tools()
    agent = build_agent(api_key, tools)

    answer = stream_agent_response(
        agent,
        st.session_state.messages
    )

    st.session_state.messages.append(AIMessage(content=answer))
    st.session_state.display_messages.append(
        {"role": "assistant", "content": answer}
    )
