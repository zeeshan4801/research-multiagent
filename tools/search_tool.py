from crewai.tools import tool
from duckduckgo_search import DDGS



@tool("web_search")
def web_search(query:str):

    """
    Search internet for research information.
    """

    results=[]


    with DDGS() as search:

        data=search.text(
            query,
            max_results=5
        )


        for item in data:

            results.append(
                {
                    "title":item.get("title"),
                    "url":item.get("href"),
                    "content":item.get("body")
                }
            )


    return results
