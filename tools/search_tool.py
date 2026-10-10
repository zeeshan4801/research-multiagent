from duckduckgo_search import DDGS
from crewai.tools import tool



def search_web(query: str) -> str:
    """
    Normal Python web search function.
    Used by Streamlit.
    """

    results = []


    with DDGS() as ddgs:

        data = ddgs.text(
            query,
            max_results=5
        )


        for item in data:

            results.append(
                f"""
Title:
{item.get('title')}

Summary:
{item.get('body')}

URL:
{item.get('href')}
"""
            )


    return "\n\n".join(results)



@tool("web_search")
def web_search(query: str) -> str:
    """
    CrewAI compatible web search tool.
    """

    return search_web(query)
