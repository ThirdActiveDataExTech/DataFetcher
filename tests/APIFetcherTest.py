import unittest

from datafetcher import api_fetcher


class APIFetcherTest(unittest.TestCase):

    def test_fetch_data_go(self):
        base_url = "api.odcloud.kr/api"  # 데이터 포털의 기본 URL을 여기에 입력

        api = api_fetcher.ApiFetcher(base_url)
        endpoint = "/15113444/v1/uddi:00ba96f2-2548-4894-8e76-e597b5eadcac"  # API 엔드포인트를 여기에 입력
        servicekey = "xP4pzOKZFbsWOwq3JF9vXjeGW8FbftsjacKe8Os+bMnaK8U7gIWVZsTVtFnGRN5W6KvqrpApm9pIeQxIEMcrAw=="
        params = {"serviceKey": servicekey, "page": "1", "perPage": "3", "returnType": "JSON"}

        data = api.get_data_portal(endpoint, params)

        expected = {
          "currentCount": 3,
          "data": [
            {
              "규모": "1412.00",
              "데이터기준일": "2023-03-31",
              "사업장구분": "일반음식점",
              "상호명": "(주)풀무원푸드앤컬쳐",
              "연번": 1,
              "음식물쓰레기 예상배출량(kg_년)": 32400,
              "전화번호": "061-374-1050",
              "주소": "전라남도 화순군 화순읍 오성로 292-90 (무등산CC)"
            },
            {
              "규모": "500.00",
              "데이터기준일": "2023-03-31",
              "사업장구분": "집단급식소",
              "상호명": "(주)현대그린푸드 녹십자 화순점",
              "연번": 2,
              "음식물쓰레기 예상배출량(kg_년)": 32400,
              "전화번호": None,
              "주소": "전라남도 화순군 화순읍 산단길 40"
            },
            {
              "규모": "330.78",
              "데이터기준일": "2023-03-31",
              "사업장구분": "일반음식점",
              "상호명": "518낙지전문점",
              "연번": 3,
              "음식물쓰레기 예상배출량(kg_년)": 6000,
              "전화번호": None,
              "주소": "전라남도 화순군 도곡면 원화리 190-1"
            }
          ],
          "matchCount": 84,
          "page": 1,
          "perPage": 3,
          "totalCount": 84
        }

        self.assertEqual(expected, data)

        if data:
            print(data)

    def test_fetch_data_seoul(self):
        base_url = "openAPI.seoul.go.kr:8088/"  # 데이터 포털의 기본 URL을 여기에 입력

        api = api_fetcher.ApiFetcher(base_url)
        endpoint = "/json/GoodsInstallState/1/5/"  # API 엔드포인트를 여기에 입력
        servicekey = "6163496569656b66313130576a545761"

        data = api.get_data_seoul(servicekey, endpoint)

        expected = {
            "GoodsInstallState": {
                "list_total_count": 826,
                "RESULT": {
                    "CODE": "INFO-000",
                    "MESSAGE": "정상 처리되었습니다"
                },
                "row": [
                    {
                        "CTF_NO": "SGPD-00971",
                        "SGPD_NO": "27",
                        "REQ_TYPE_CD": "2",
                        "CD_NM": "공공시설물",
                        "PROD_NM": "보행자용휀스",
                        "MDL_NM": "Kgrim-39",
                        "REC_END_DT": "2022831 ",
                        "INST_ADDR": "서울특별시 구로구 구로동 69-7 일원",
                        "PRJ_NM": "관급자재구매(교통사고 잦은 곳 개선사업(거리공원오거리)-보행자안전휀스",
                        "INST_CNT": 74.0
                    },
                    {
                        "CTF_NO": "SGPD-01026",
                        "SGPD_NO": "28",
                        "REQ_TYPE_CD": "2",
                        "CD_NM": "공공시설물",
                        "PROD_NM": "바론형",
                        "MDL_NM": "ACP-2004, ACPL-SC050N",
                        "REC_END_DT": "20220320",
                        "INST_ADDR": "서울 동작구 동작동 102-18 이수스위첸포레힐즈아파트",
                        "PRJ_NM": "동작1 주택재건축정비사업 중 가로등 설비 전기공사",
                        "INST_CNT": 10.0
                    },
                    {
                        "CTF_NO": "SGPD-01026",
                        "SGPD_NO": "28",
                        "REQ_TYPE_CD": "2",
                        "CD_NM": "공공시설물",
                        "PROD_NM": "바론형",
                        "MDL_NM": "ACP-2004, ACPL-SC050N",
                        "REC_END_DT": "20220320",
                        "INST_ADDR": "서울 동작구 신대방동 686-48 협성휴포레시그니처 입구",
                        "PRJ_NM": "신대방 협성휴포레 아파트 신축공사 중 가로등 설비 전기공사",
                        "INST_CNT": 16.0
                    },
                    {
                        "CTF_NO": "SGPD-01045",
                        "SGPD_NO": "28",
                        "REQ_TYPE_CD": "2",
                        "CD_NM": "공공시설물",
                        "PROD_NM": "디자인형울타리",
                        "MDL_NM": "SN-103",
                        "REC_END_DT": "20220317",
                        "INST_ADDR": "서울 중랑구 용마산로 715",
                        "PRJ_NM": "디자인형울타리 구매(노후 보행자방호울타리 교체사업)",
                        "INST_CNT": 215.0
                    },
                    {
                        "CTF_NO": "SGPD-01045",
                        "SGPD_NO": "28",
                        "REQ_TYPE_CD": "2",
                        "CD_NM": "공공시설물",
                        "PROD_NM": "디자인형울타리",
                        "MDL_NM": "SN-103",
                        "REC_END_DT": "20220216",
                        "INST_ADDR": "서울특별시 중랑구 면목천교",
                        "PRJ_NM": "관급자재구매(디자인형울타리-2022년하천시설물 유지보수공사)",
                        "INST_CNT": 95.0
                    }
                ]
            }
        }

        self.assertEqual(expected, data)

        if data:
            print(data)

