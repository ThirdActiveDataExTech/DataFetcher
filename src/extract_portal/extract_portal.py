import json
import os
import uuid
from urllib.parse import urlencode

import requests


def make_file_path(url):
    response = requests.get(url)
    response.raise_for_status()

    file_name = str(uuid.uuid4()) + ".txt"
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_dir = os.path.join(root_dir, 'tmp_files/portal/')
    file_path = file_dir + file_name
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    return response, file_path


class ExtractPortal(object):
    def __init__(self, base_url, endpoint, service_key):
        """
        :param base_url: 데이터 포털 API의 기본 URL
        :param endpoint: 가져올 데이터의 end point
        :param service_key: 가져올 데이터의 service_key
        """
        self.base_url = base_url
        self.endpoint = endpoint
        self.service_key = service_key

    def get_data_portal(self, data_portal_params=None):
        """
        공공 데이터 포털 API에서 데이터를 가져옵니다.

        :param data_portal_params: 추가적인 파라미터 (딕셔너리 형태)
        :return: JSON 응답 데이터
        """
        param = urlencode(data_portal_params)

        url = f"https://{self.base_url}{self.endpoint}?serviceKey={self.service_key}&{param}"

        try:
            response, file_path = make_file_path(url)
            bucket_name = "dataportal"

            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(response.json(), f, ensure_ascii=False, indent=4)
            except EOFError as e:
                print(f"파일 저장 실패: {e}")

            return file_path, bucket_name
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None

    def get_data_seoul(self, data_seoul_params=None):
        """
        서울열린데이터포털 API에서 데이터를 가져옵니다.

        :return: JSON 응답 데이터
        """

        url = f"http://{self.base_url}{self.service_key}{self.endpoint}"

        try:
            response, file_path = make_file_path(url)
            bucket_name = "seoulportal"

            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(response.json(), f, ensure_ascii=False, indent=4)
            except EOFError as e:
                print(f"파일 저장 실패: {e}")

            return file_path, bucket_name
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None


if __name__ == "__main__":
    data_portal_base_url = "api.odcloud.kr/api"  # 데이터 포털의 기본 URL을 여기에 입력
    data_portal_endpoint = "/15113444/v1/uddi:1ae26320-fa56-4206-8d06-9ee5db5a8dcf"  # API 엔드포인트를 여기에 입력
    data_portal_service_key = ("xP4pzOKZFbsWOwq3JF9vXjeGW8FbftsjacKe8Os"
                               "%2BbMnaK8U7gIWVZsTVtFnGRN5W6KvqrpApm9pIeQxIEMcrAw%3D%3D")

    data_seoul_base_url = "openAPI.seoul.go.kr:8088/"
    data_seoul_endpoint = "/json/GoodsInstallState/1/5/"
    data_seoul_service_key = "6163496569656b66313130576a545761"

    data_portal_api = ExtractPortal(data_portal_base_url, data_portal_endpoint, data_portal_service_key)
    data_seoul_api = ExtractPortal(data_seoul_base_url, data_seoul_endpoint, data_seoul_service_key)

    params = {"pageNo": "1", "numOfRows": "1", "_type": "json", "nm": "강북"}

    data_portal = data_portal_api.get_data_portal(params)
    data_seoul = data_seoul_api.get_data_seoul()
    if data_portal:
        print(data_portal)
        print("\n")

    else:
        print("get_data_portal failed\n")

    if data_seoul:
        print(data_seoul)
        print("\n")
    else:
        print("get_data_seoul failed\n")
