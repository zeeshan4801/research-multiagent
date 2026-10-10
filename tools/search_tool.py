import requests

from bs4 import BeautifulSoup

from urllib.parse import quote

from crewai.tools import tool



def search_web(query: str) -> str:
    """
    Simple web search using DuckDuckGo HTML.
    No external search package required.
    """

    try:

        url = (
            "https://html.duckduckgo.com/html/?q="
            + quote(query)
        )


        headers = {

            "User-Agent":
            "Mozilla/5.0"

        }


        response = requests.get(

            url,

            headers=headers,

            timeout=10

        )


        soup = BeautifulSoup(

            response.text,

            "html.parser"

        )


        results=[]


        for result in soup.select(".result")[:5]:


            title = result.select_one(
                ".result__title"
            )


            snippet = result.select_one(
                ".result__snippet"
            )


            link = result.select_one(
                ".result__a"
            )


            results.append(

                f"""
Title:
{title.text if title else ''}

Summary:
{snippet.text if snippet else ''}

Link:
{link.get('href') if link else ''}
"""
            )



        if not results:

            return "No web results found."



        return "\n\n".join(results)



    except Exception as e:

        return f"Search failed: {str(e)}"




@tool("web_search")
def web_search(query:str)->str:

    """
    CrewAI compatible search tool.
    """

    return search_web(query)
