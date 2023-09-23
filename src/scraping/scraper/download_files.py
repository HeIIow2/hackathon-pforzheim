import random
from urllib.parse import urlparse
import os

from .connections import Connection



def dump_url_content(keyword: str, extention: str, url: str):
    connection = Connection(host=url, timeout=2, tries=1)
    
    r = connection.get(url=url)
    if r is None:
        return 

    with open(f"src/scraping/dumps/{keyword}_{random.randint(0, 999999999)}.{extention}", "wb") as f:
        f.write(r.content) 
