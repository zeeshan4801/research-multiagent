from crewai.tools import tool

from duckduckgo_search import DDGS



@tool("web_search")
def web_search(query: str) -> str:

    """
    Search the internet for research information.
    """

    results=[]


    with DDGS() as ddgs:

        search_results = ddgs.text(

            query,

            max_results=3

        )


        for item in search_results:

            results.append(

                f"""
                Title:
                {item.get('title')}

                Content:
                {item.get('body')}

                URL:
                {item.get('href')}
                """

            )


    return "\n\n".join(results)
