import streamlit as st
from langchain_core.messages import AIMessage, ToolMessage
from tools.tools import TOOL_ICONS


def stream_agent_response(agent, messages):

    with st.chat_message("assistant"):

        thoughts_container = st.container()
        answer_placeholder = st.empty()

        answer = ""
        used_tools = set()

        with thoughts_container:

            for chunk, metadata in agent.stream(
                {"messages": messages},
                stream_mode="messages"
            ):

                node = metadata.get("langgraph_node", "")

                if node == "agent" and isinstance(chunk, AIMessage):

                    if getattr(chunk, "tool_calls", []):

                        for tc in chunk.tool_calls:
                            tool_display = TOOL_ICONS.get(tc["name"], tc["name"])

                            st.info(
                                f"Thinking: Calling {tool_display}"
                            )

                    elif chunk.content:

                        answer += chunk.content
                        answer_placeholder.markdown(answer)

                if node == "tools" and isinstance(chunk, ToolMessage):

                    tool_name = getattr(chunk, "name", "Tool")
                    display_name = TOOL_ICONS.get(tool_name, tool_name)

                    used_tools.add(display_name)

                    with st.expander(f"{display_name} Result", expanded=True):
                        st.markdown(chunk.content)

        if used_tools:
            st.caption(f"Sources used: {' · '.join(used_tools)}")

    return answer
