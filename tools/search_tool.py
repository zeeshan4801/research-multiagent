from crewai.tools import tool
from duckduckgo_search import DDGS



@tool("web_search")
def web_search(query: str) -> str:
    """
    Search web and return useful research information.
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

Link:
{item.get('href')}
"""

            )


    return "\n\n".join(results)
