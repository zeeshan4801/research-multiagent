import re


def extract_sources(text):

    urls = re.findall(
        r'https?://[^\s]+',
        text
    )

    cleaned = []

    for url in urls:

        url = url.rstrip(".,)")

        if url not in cleaned:

            cleaned.append(url)


    return cleaned
