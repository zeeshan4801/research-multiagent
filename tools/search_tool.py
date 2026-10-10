from duckduckgo_search import DDGS
from crewai.tools import tool



def search_web(query: str) -> str:
    """
    Normal web search function.
    """

    results = []


    try:

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

Source:
{item.get('href')}
"""

                )


        if not results:

            return "No search results found."


        return "\n\n".join(results)



    except Exception as e:

        return f"Search error: {str(e)}"





@tool("web_search")
def web_search(query: str) -> str:

    """
    CrewAI web search tool.
    """

    return search_web(query)
