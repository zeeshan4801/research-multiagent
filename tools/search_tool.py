import os

from tavily import TavilyClient



def search_web(query):

    """
    AI optimized web search
    """

    client = TavilyClient(

        api_key=os.getenv(
            "TAVILY_API_KEY"
        )

    )


    response = client.search(

        query=query,

        search_depth="advanced",

        max_results=5

    )


    results=[]


    for item in response["results"]:


        results.append(

            f"""
Title:
{item['title']}

Content:
{item['content']}

URL:
{item['url']}
"""

        )


    return "\n\n".join(results)
