import requests
from bs4 import BeautifulSoup


def read_web(url):
    response = requests.get(url)

    if response.status_code != 200:  # 정상 연결시
        raise requests.exceptions.HTTPError

    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def status_check(url):
    response = requests.get(url)
    if response.status_code != 200:  # 정상 연결시
        raise requests.exceptions.HTTPError


if __name__ == "__main__":
    read_web('https://mangkyu.tistory.com/261')
