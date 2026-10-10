from crewai.tools import tool
import requests

from bs4 import BeautifulSoup



@tool("read_webpage")
def read_webpage(url:str):

    """
    Extract webpage text.
    """

    response=requests.get(
        url,
        timeout=10
    )


    soup=BeautifulSoup(
        response.text,
        "html.parser"
    )


    return soup.get_text(
        separator=" ",
        strip=True
    )[:5000]
