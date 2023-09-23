from typing import List, Dict
from functools import cache
from googlesearch import search

from . import shared


def search_keywords(keywords: List[str] = shared.KEYWORDS) -> Dict[str, List[str]]:
    keyword_to_result: dict = {}

    for keyword in keywords:
        query = shared.SEARCH_MASK.format(keyword=keyword)
        
        results = []
        print(f"searching for \"{query}\"")
        for r in search(query):
            print(r)
            results.append(str(r))

        keyword_to_result[keyword] = results

        if shared.DEBUG:
            break

    return keyword_to_result
