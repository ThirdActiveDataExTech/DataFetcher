from urllib.parse import urlparse

import requests

from extract_blog import util

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
    try:
        page = util.read_web(target_url)
    except requests.exceptions.HTTPError:
        raise
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

        searched_url.add(f'{url.scheme}://{url.netloc}{url.path}')

    return searched_url


def get_base_url(url):
    url = urlparse(url)
    base_url = f'{url.scheme}://{url.netloc}'
    return base_url


def publish_embedded_links(main_url):
    base_url = get_base_url(main_url)
    embedded_links = search_link(base_url, main_url)

    return embedded_links


if __name__ == '__main__':
    # start_url = 'https://ksh-coding.tistory.com/144'
    start_url = 'https://section.blog.naver.com'
    publish_embedded_links(start_url)
