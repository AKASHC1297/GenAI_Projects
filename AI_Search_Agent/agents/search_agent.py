from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent


def build_agent(api_key, tools):

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="openai/gpt-oss-20b",
        streaming=True
    )

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=(
           prompt=(
        "You are a research assistant with access to the following tools:\n"
        "1. search - DuckDuckGo web search\n"
        "2. wikipedia - general knowledge lookup\n"
        "3. arxiv - academic research papers\n\n"
        "Use ONLY these exact tool names when calling tools."
)

        )
    )

    return agent
