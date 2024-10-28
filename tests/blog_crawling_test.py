import unittest
from extract_blog import extract_blog_url
from load.load_data import load_data
from load.load_meta_data import load_meta_data
from unittest.mock import patch


class BlogCrawlingTest(unittest.TestCase):

    def test_blog_crawling(self):
        test_url = 'https://section.blog.naver.com'
        path_list, bucket_name = extract_blog_url.blog_crawler(test_url)

        self.assertEqual(bucket_name, "blog")

        minio_file_path, file_size, bucket_name = load_data(path_list, bucket_name)
        expected = load_meta_data(minio_file_path, file_size)

        self.assertEqual(expected, "메타데이터가 PostgreSQL에 저장되었습니다.")

    @patch('extract_blog.search.publish_embedded_links')
    def test_blog_crawling_list(self, mok_publish_embedded_links):
        test_url = 'https://section.blog.naver.com'
        searched_url = set()
        searched_url.add('https://blog.naver.com/julie2366/223585634101')

        mok_publish_embedded_links.return_value = searched_url

        path_list, bucket_name = extract_blog_url.blog_crawler(test_url)

        minio_file_path, file_size, bucket_name = load_data(path_list, bucket_name)
        expected = load_meta_data(minio_file_path, file_size)

        self.assertEqual(expected, "메타데이터가 PostgreSQL에 저장되었습니다.")
