import json
import os
import re
import uuid

from extract_blog.blog import search
from extract_blog.blog import util
from extract_blog.blog import error
from extract_blog.blog import log


def url_parsing(url):
    naver_pattern = r"https://m\.blog\.naver\.com/([^/]+)/(\d+)"

    match_naver = re.match(naver_pattern, url)

    if not match_naver:
        return False
    return True


def blog_crawler():
    # 해당 web 에 있는 모든 url 을 [수집 대기 URL queue] 에 전송
    # current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    blog_url_list = search.publish_embedded_links("https://section.blog.naver.com")
    log.info('publish_embedded_links done')

    path_list = []

    for blog_url in blog_url_list:
        # URL 유효성 체크
        try:
            util.status_check(blog_url)
        except error.WebRequestsError:
            raise

        if url_parsing(blog_url):
            page = util.read_web(blog_url)

            # # 1. html 데이터 수집
            # html_data = str(page)

            # 2. text 데이터 수집
            text_data = page.get_text()

            file_name = str(uuid.uuid4()) + ".txt"
            file_dir = "./extract_files/blog/"
            file_path = file_dir + file_name
            try:
                if not os.path.exists(file_dir):
                    os.makedirs(file_dir)
                bucket_name = "blog"
                try:
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(text_data, f, ensure_ascii=False, indent=4)
                except EOFError as e:
                    print(f"파일 저장 실패: {e}")

                return file_path, bucket_name
            except Exception as err:
                print(f"An error occurred: {err}")

            path_list.append(file_path)
    return path_list, bucket_name





if __name__ == "__main__":
    # test_url = 'https://covenant.tistory.com/247'
    test_url = 'https://section.blog.naver.com'
    crawler = blog_crawler(test_url)
