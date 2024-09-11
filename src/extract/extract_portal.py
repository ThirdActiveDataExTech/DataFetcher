from urllib.parse import urlencode

import requests


class ExtractPortal(object):
    def __init__(self, base_url):
        """
        :param base_url: 데이터 포털 API의 기본 URL
        :param api_key: 데이터 포털 API 키
        """
        self.base_url = base_url

    def get_data_portal(self, endpoint, params=None):
        """
        데이터 포털 API에서 데이터를 가져옵니다.

        :param endpoint: API 엔드포인트 (예: '/data/endpoint')
        :param params: 추가적인 파라미터 (딕셔너리 형태)
        :return: JSON 응답 데이터
        """
        param = urlencode(params)

        url = f"https://{self.base_url}{endpoint}?{param}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # HTTP 오류가 있는 경우 예외 발생

            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None

    def get_data_seoul(self, servicekey, endpoint):
        """
        서울열린데이터포털 API에서 데이터를 가져옵니다.

        :param endpoint: API 엔드포인트 (예: '/data/endpoint')
        :param params: 추가적인 파라미터 (딕셔너리 형태)
        :return: JSON 응답 데이터
        """

        url = f"http://{self.base_url}{servicekey}{endpoint}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # HTTP 오류가 있는 경우 예외 발생
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None



if __name__ == "__main__":
    base_url = "apis.data.go.kr/B500001/waternow/twdClwr"  # 데이터 포털의 기본 URL을 여기에 입력

    api = ExtractPortal(base_url)

    endpoint = "/wdr/clwrList"  # API 엔드포인트를 여기에 입력
    servicekey = "xP4pzOKZFbsWOwq3JF9vXjeGW8FbftsjacKe8Os+bMnaK8U7gIWVZsTVtFnGRN5W6KvqrpApm9pIeQxIEMcrAw=="
    params = {"serviceKey": servicekey, "pageNo": "1", "numOfRows": "1", "_type": "json", "nm": "강북"}

    data = api.get_data_portal(endpoint, params)
    if data:
        print(data)
