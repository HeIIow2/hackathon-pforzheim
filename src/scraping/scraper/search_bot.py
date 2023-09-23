from typing import List, Dict
from functools import cache
#from googlesearch import search
from duckduckgo_search import DDGS

with DDGS() as ddgs:
    for r in ddgs.text('live free or die', region='wt-wt', safesearch='off', timelimit='y'):
        print(r)

from . import shared
from .download_files import dump_url_content


def search_keywords(keywords: List[str] = shared.KEYWORDS) -> Dict[str, List[str]]:
    for keyword in keywords:
        for MASK in shared.MASKS:
            extention = "html"

            splits = MASK.split(":")
            if len(splits) >= 2:
                extention = splits[-1].strip()

            query = MASK.format(keyword=keyword)
            
            results = []
            print(f"searching for \"{query}\"")
            with DDGS() as ddgs:
                for r in ddgs.text(keywords=query, region='wt-wt', safesearch='off', timelimit='y'):
                    dump_url_content(keyword, extention, r["href"])
            #for r in search(query):
            #    dump_url_content(keyword, extention, r)

