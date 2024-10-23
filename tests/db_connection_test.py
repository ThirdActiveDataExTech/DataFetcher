from config.config import Config
from extract_portal.extract_portal import ExtractPortal
from load.load_meta_data import load_meta_data
from load.load_data import load_data
import unittest


class DBConnectionTest(unittest.TestCase):

    def test_load_data_portal(self):
        data_portal_base_url = Config.data_portal.base_url
        data_portal_endpoint = Config.data_portal.endpoint
        data_portal_service_key = Config.data_portal.service_key
        data_portal_api = ExtractPortal(data_portal_base_url, data_portal_endpoint, data_portal_service_key)

        params = {"pageNo": "1", "numOfRows": "1", "_type": "json", "nm": "강북"}

        file_path, bucket_name = data_portal_api.get_data_portal(params)

        file_path, file_size, bucket_name = load_data(file_path, bucket_name)

        expected = load_meta_data(file_path, file_size)

        self.assertEqual(expected, "메타데이터가 PostgreSQL에 저장되었습니다.")

    def test_load_metadata(self):
        file_path = "http://192.168.107.19:9004/dataportal/b082e81a-1aa5-4c29-43e7-b2fa84fc4d59.txt"
        file_size = 4120
        expected = load_meta_data(file_path, file_size)
        self.assertEqual(expected, "메타데이터가 PostgreSQL에 저장되었습니다.")
