import re



def extract_sources(text):

    urls = re.findall(

        r'https?://[^\s]+',

        text

    )


    return list(set(urls))
