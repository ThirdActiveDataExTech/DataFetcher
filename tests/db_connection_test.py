import os

from load.load_portal_meta import load_portal_meta
from src.extract.extract_portal import ExtractPortal
from src.load.load_portal import load_portal
import unittest


class DBConnectionTest(unittest.TestCase):

    @staticmethod
    def test_load_data_portal(self):
        data_portal_base_url = "api.odcloud.kr/api"  # 데이터 포털의 기본 URL을 여기에 입력
        data_portal_endpoint = "/15113444/v1/uddi:1ae26320-fa56-4206-8d06-9ee5db5a8dcf"  # API 엔드포인트를 여기에 입력
        data_portal_service_key = ("xP4pzOKZFbsWOwq3JF9vXjeGW8FbftsjacKe8Os"
                                   "%2BbMnaK8U7gIWVZsTVtFnGRN5W6KvqrpApm9pIeQxIEMcrAw%3D%3D")
        data_portal_api = ExtractPortal(data_portal_base_url, data_portal_endpoint, data_portal_service_key)

        params = {"pageNo": "1", "numOfRows": "1", "_type": "json", "nm": "강북"}

        data_portal = data_portal_api.get_data_portal(params)

        file_path, file_size = load_portal(data_portal)

    @staticmethod
    def test_load_metadata():
        file_path = "http://192.168.107.19:9004/dataportal/b082e81a-1aa5-4c29-8ae7-b2fa84fc4d59.txt"
        file_size = 4120
        load_portal_meta(file_path, file_size)
