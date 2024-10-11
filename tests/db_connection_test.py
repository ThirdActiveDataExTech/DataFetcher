import unittest

from src.load.load_portal import load_portal
from src.extract.extract_portal import ExtractPortal


class DBConnectionTest(unittest.TestCase):

    def test_get_data_portal(self):
        data_portal_base_url = "api.odcloud.kr/api"  # 데이터 포털의 기본 URL을 여기에 입력
        data_portal_endpoint = "/15113444/v1/uddi:1ae26320-fa56-4206-8d06-9ee5db5a8dcf"  # API 엔드포인트를 여기에 입력
        data_portal_service_key = ("xP4pzOKZFbsWOwq3JF9vXjeGW8FbftsjacKe8Os"
                                   "%2BbMnaK8U7gIWVZsTVtFnGRN5W6KvqrpApm9pIeQxIEMcrAw%3D%3D")
        data_portal_api = ExtractPortal(data_portal_base_url, data_portal_endpoint, data_portal_service_key)

        params = {"pageNo": "1", "numOfRows": "1", "_type": "json", "nm": "강북"}

        data_portal = data_portal_api.get_data_portal(params)

        load_portal(data_portal)

    def test_get_data_seoul(self):
        data_seoul_base_url = "openAPI.seoul.go.kr:8088/"
        data_seoul_endpoint = "/json/GoodsInstallState/1/5/"
        data_seoul_service_key = "6163496569656b66313130576a545761"

        data_seoul_api = ExtractPortal(data_seoul_base_url, data_seoul_endpoint, data_seoul_service_key)

        data_seoul = data_seoul_api.get_data_seoul()

        load_portal(data_seoul)
