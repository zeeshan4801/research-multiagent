import os

from tavily import TavilyClient



def search_web(query):

    client = TavilyClient(

        api_key=os.getenv(
            "TAVILY_API_KEY"
        )

    )


    response = client.search(

        query=query,

        search_depth="basic",

        max_results=3

    )


    results=[]


    for item in response.get("results", []):


        results.append(

            f"""
Title:
{item.get('title')}

Content:
{item.get('content','')[:700]}

URL:
{item.get('url')}
"""

        )


    return "\n\n".join(results)
