from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun


def get_tools():

    arxiv_wrapper = ArxivAPIWrapper(
        top_k_results=1,
        doc_content_chars_max=200
    )

    arxiv = ArxivQueryRun(
        api_wrapper=arxiv_wrapper,
        name="arxiv",
        description="Search academic papers on Arxiv."
    )

    wiki_wrapper = WikipediaAPIWrapper(
        top_k_results=1,
        doc_content_chars_max=200
    )

    wiki = WikipediaQueryRun(
        api_wrapper=wiki_wrapper,
        name="wikipedia",
        description="Search Wikipedia for factual information."
    )

    search = DuckDuckGoSearchRun(
        name="search",
        description="Search the web using DuckDuckGo."
    )

    return [search, arxiv, wiki]
