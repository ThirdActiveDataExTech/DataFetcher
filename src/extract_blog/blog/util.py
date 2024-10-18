import requests
from bs4 import BeautifulSoup
import error
import bs4


def read_web(url):
    response = requests.get(url, timeout=5)

    if response.status_code != 200:  # 정상 연결시
        raise error.WebRequestsError(url, response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')

    return soup


def status_check(url):
    response = requests.get(url)
    if response.status_code != 200:  # 정상 연결시
        raise error.WebRequestsError(url, response.status_code)


def remove_tag(data: bs4.element.Tag, is_all=True):
    if is_all:
        content = data.text \
            .replace('\n', '') \
            .replace('\xa0', '')
        return data.name, content
    else:
        # blockquote
        for tag in data.children:
            tag: bs4.element.Tag
            if tag.name is not None:
                if tag.name not in ['br', 'code']:
                    tag.decompose()
        data.attrs = {}
    return data.name, data


if __name__ == "__main__":
    read_web('https://mangkyu.tistory.com/261')
