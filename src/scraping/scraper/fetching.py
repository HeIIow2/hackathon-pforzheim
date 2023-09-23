from typing import List


from .search_bot import search_keywords
from .rss import get_rss_urls


def fetch(keyword: str):
    pass

def fetch_all():
    r = search_keywords()

    for keyword, url_list in r.items():
        rss_feeds: List[str] = []
        for url in url_list:
            rss_feeds.extend(get_rss_urls(url))

        print(rss_feeds)
