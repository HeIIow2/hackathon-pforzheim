from .connections import Connection


def get_rss_urls(url: str):
    connection = Connection(host=url)
    
    r = connection.get(url=url)
    print(r)

    return []
