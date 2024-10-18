from urllib.parse import urlparse

import util

import log

SKIP_URL = {
    'tistory': ['tag', 'archive', 'category', 'rss', 'guestbook', 'manage', 'entry']
}

SITE_TYPE = {
    'com': {
        'tistory': 'TISTORY',
        'naver': 'NAVER',
    }
}


def search_link(base_url: str, target_url: str):
    searched_url = set()

    page = util.read_web(target_url)
    for row in page.find_all(['a']):
        path = row.get('href')
        if path is None:
            continue

        if path.startswith('/'):
            url = f"{base_url}{path}"
        elif path.startswith('http'):
            url = path
        else:
            continue

        try:
            url = urlparse(url)
        except ValueError as e:
            print("Error: " + ' '.join(e.args))
            continue
        url_path = url.path.split('/')
        if url.path in ('/', ''):
            continue
        if len(url_path) >= 2 and url_path[1] in SKIP_URL['tistory']:
            continue

        if get_site_type(url) is not None:
            searched_url.add(f'{url.scheme}://{url.netloc}{url.path}')

    return searched_url


def get_base_url(url):
    url = urlparse(url)
    base_url = f'{url.scheme}://{url.netloc}'
    return base_url


def get_site_type(url):
    url_netloc = url.netloc.rsplit('.', 2)
    if url_netloc[-1] in SITE_TYPE:
        if url_netloc[-2] in SITE_TYPE[url_netloc[-1]]:
            return SITE_TYPE[url_netloc[-1]][url_netloc[-2]]

    return None


def publish_embedded_links(main_url):
    base_url = get_base_url(main_url)
    embedded_links = search_link(base_url, main_url)

    log.info(embedded_links)

    return embedded_links

    # for item in embedded_links:
    #     response.publish(item, exchange='all_urls_exchange', routing_key='')


if __name__ == '__main__':
    # start_url = 'https://ksh-coding.tistory.com/144'
    start_url = 'https://section.blog.naver.com'
    publish_embedded_links(start_url)
