import requests

class DataPortalAPI:
    def __init__(self, base_url, api_key):
        """
        :param base_url: 데이터 포털 API의 기본 URL
        :param api_key: 데이터 포털 API 키
        """
        self.base_url = base_url
        self.api_key = api_key

    def get_data(self, endpoint, params=None):
        """
        데이터 포털 API에서 데이터를 가져옵니다.

        :param endpoint: API 엔드포인트 (예: '/data/endpoint')
        :param params: 추가적인 파라미터 (딕셔너리 형태)
        :return: JSON 응답 데이터
        """
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # HTTP 오류가 있는 경우 예외 발생
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None

# 사용 예시
if __name__ == "__main__":
    base_url = "https://www.data.go.kr/index.do"  # 데이터 포털의 기본 URL을 여기에 입력
    api_key = "YOUR_API_KEY"  # API 키를 여기에 입력

    api = DataPortalAPI(base_url, api_key)
    endpoint = "/data/endpoint"  # API 엔드포인트를 여기에 입력
    params = {"param1": "value1", "param2": "value2"}  # 필요한 파라미터를 여기에 입력

    data = api.get_data(endpoint, params)
    if data:
        print(data)