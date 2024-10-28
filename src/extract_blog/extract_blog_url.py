import json
import os
import uuid

import requests

from extract_blog import search, util


def blog_crawler(url):
    # 해당 web 에 있는 모든 url 을 수집해 리턴
    blog_url_list = search.publish_embedded_links(url)

    path_list = []
    bucket_name = "blog"

    for blog_url in blog_url_list:
        # URL 유효성 체크
        try:
            util.status_check(blog_url)
        except requests.exceptions.HTTPError:
            raise
        try:
            page = util.read_web(blog_url)
        except requests.exceptions.HTTPError:
            continue
        text_data = page.get_text()

        file_name = str(uuid.uuid4()) + ".txt"
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_dir = os.path.join(root_dir, 'tmp_files/blog/')
        file_path = file_dir + file_name
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        try:
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(text_data, f, ensure_ascii=False, indent=4)
            except EOFError as e:
                print(f"파일 저장 실패: {e}")
        except Exception as err:
            print(f"An error occurred: {err}")

        path_list.append(file_path)
    return path_list, bucket_name


if __name__ == "__main__":
    test_url = 'https://section.blog.naver.com/ThisMonthDirectory.naver'
    crawler = blog_crawler(test_url)
