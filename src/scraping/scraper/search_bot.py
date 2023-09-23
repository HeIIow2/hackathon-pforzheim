from typing import List
from googlesearch import search


from . import shared


def search_keywords(keywords: List[str] = shared.KEYWORDS):
    for keyword in keywords:
        query = shared.SEARCH_MASK.format(keyword=keyword)
        
        print(query)
        for r in search(query):
            print(r)

        if shared.DEBUG:
            break
