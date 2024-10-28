import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

from extract_blog import search

url_list = [
    'https://section.blog.naver.com',
    'https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=1&groupId=0',
    'https://section.blog.naver.com/ThemePost.naver?directoryNo=0&activeDirectorySeq=0&currentPage=1',
    'https://section.blog.naver.com/ThisMonthDirectory.naver',
    'https://section.blog.naver.com/OfficialBlog.naver?currentPage=1',
    'https://section.blog.naver.com/HotTopicChallenge.naver?currentPage=1'
]


def read_web(url):
    response = requests.get(url)

    if response.status_code != 200:  # 정상 연결시
        raise requests.exceptions.HTTPError

    driver = webdriver.Chrome()
    driver.get(url)
    try:
        if url not in url_list:
            try:
                WebDriverWait(driver, 5).until(
                    ec.frame_to_be_available_and_switch_to_it((By.ID, 'mainFrame'))
                )
            except TimeoutException:
                print(f"{url} : timed out")
        html = driver.page_source
    finally:
        driver.quit()
    res = BeautifulSoup(html, 'html.parser')
    return res


def status_check(url):
    response = requests.get(url)
    if response.status_code != 200:  # 정상 연결시
        raise requests.exceptions.HTTPError


if __name__ == "__main__":
    read_web('https://mangkyu.tistory.com/261')
