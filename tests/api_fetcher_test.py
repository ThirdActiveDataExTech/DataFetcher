import unittest

from extract_portal.extract_portal import ExtractPortal


class APIFetcherTest(unittest.TestCase):

    def test_fetch_data_go(self):
        base_url = "api.odcloud.kr/api"
        endpoint = "/15113444/v1/uddi:1ae26320-fa56-4206-8d06-9ee5db5a8dcf"
        service_key = "xP4pzOKZFbsWOwq3JF9vXjeGW8FbftsjacKe8Os%2BbMnaK8U7gIWVZsTVtFnGRN5W6KvqrpApm9pIeQxIEMcrAw%3D%3D"

        data_portal_extract = ExtractPortal(base_url, endpoint, service_key)
        params = {"page": "1", "perPage": "3", "returnType": "JSON"}

        data = data_portal_extract.get_data_portal(params)

        expected = {'currentCount': 3,
                    'data': [{'규모': '381.93',
                              '데이터기준일': '2024-08-28',
                              '사업장구분': '일반음식점',
                              '상호명': '남도명가',
                              '연번': 1,
                              '음식물쓰레기 예상배출량(kg_년)': 10800,
                              '전화번호': '061-371-0085',
                              '주소': '전라남도 화순군 능주면 능주농공길 3'},
                             {'규모': '108.42',
                              '데이터기준일': '2024-08-28',
                              '사업장구분': '일반음식점',
                              '상호명': '전원',
                              '연번': 2,
                              '음식물쓰레기 예상배출량(kg_년)': 1300,
                              '전화번호': '061-372-1663',
                              '주소': '전라남도 화순군 능주면 죽수길 4'},
                             {'규모': '416.86',
                              '데이터기준일': '2024-08-28',
                              '사업장구분': '일반음식점',
                              '상호명': '남도의 향기',
                              '연번': 3,
                              '음식물쓰레기 예상배출량(kg_년)': 8280,
                              '전화번호': '061-373-8989',
                              '주소': '전라남도 화순군 도곡면 지강로 212'}],
                    'matchCount': 27,
                    'page': 1,
                    'perPage': 3,
                    'totalCount': 27}

        self.assertEqual(expected, data)

        if data:
            print(data)

    def test_fetch_data_seoul(self):
        base_url = "openAPI.seoul.go.kr:8088/"
        endpoint = "/json/GoodsInstallState/1/5/"
        service_key = "6163496569656b66313130576a545761"

        data_seoul_extract = ExtractPortal(base_url, endpoint, service_key)

        data = data_seoul_extract.get_data_seoul()
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
