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

url_list = [
    'https://www.naver.com/',
    'https://www.naver.com/rules/service.html',
    'https://section.blog.naver.com/OfficialBlog.naver',
    'https://blog.naver.com/post/blog_use.htm',
    'https://section.blog.naver.com/HotTopicChallenge.naver',
    'https://section.blog.naver.com/PowerBlog.naver',
    'https://section.blog.naver.com/ThemePost.naver',
    'https://www.naver.com/rules/disclaimer.html',
    'https://help.naver.com/service/5593/contents/5043',
    'https://section.blog.naver.com/BlogHome.naver',
    'https://www.naver.com/rules/privacy.html',
    'https://section.blog.naver.com/thisMonthDirectory.naver',
    'https://section.blog.naver.com/PreviousThisMonthBlog.naver',
    'https://right.naver.com',
    'https://www.navercorp.com/',
]


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
        url_path = f'{url.scheme}://{url.netloc}{url.path}'

        if url_path not in url_list:
            searched_url.add(url_path)

        print()
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
