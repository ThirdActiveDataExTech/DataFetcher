import unittest

from extract_portal.extract_portal import ExtractPortal
from config.config import Config


class APIFetcherTest(unittest.TestCase):

    def test_fetch_data_go(self):
        base_url = "api.odcloud.kr/api"
        endpoint = Config.data_portal.endpoint
        service_key = Config.data_portal.service_key

        data_portal_extract = ExtractPortal(base_url, endpoint, service_key)
        params = {"page": "1", "perPage": "3", "returnType": "JSON"}

        file_path, bucket_name = data_portal_extract.get_data_portal(params)
        data = open(file_path, 'r', encoding='utf-8').read()

        expected = {
            "currentCount": 3,
            "data": [
                {
                    "규모": "381.93",
                    "데이터기준일": "2024-08-28",
                    "사업장구분": "일반음식점",
                    "상호명": "남도명가",
                    "연번": 1,
                    "음식물쓰레기 예상배출량(kg_년)": 10800,
                    "전화번호": "061-371-0085",
                    "주소": "전라남도 화순군 능주면 능주농공길 3"
                },
                {
                    "규모": "108.42",
                    "데이터기준일": "2024-08-28",
                    "사업장구분": "일반음식점",
                    "상호명": "전원",
                    "연번": 2,
                    "음식물쓰레기 예상배출량(kg_년)": 1300,
                    "전화번호": "061-372-1663",
                    "주소": "전라남도 화순군 능주면 죽수길 4"
                },
                {
                    "규모": "416.86",
                    "데이터기준일": "2024-08-28",
                    "사업장구분": "일반음식점",
                    "상호명": "남도의 향기",
                    "연번": 3,
                    "음식물쓰레기 예상배출량(kg_년)": 8280,
                    "전화번호": "061-373-8989",
                    "주소": "전라남도 화순군 도곡면 지강로 212"
                }
            ],
            "matchCount": 27,
            "page": 1,
            "perPage": 3,
            "totalCount": 27
        }

        self.assertEqual(expected, data)

        if data:
            print(data)

    def test_fetch_data_seoul(self):
        base_url = Config.seoul_portal.base_url
        endpoint = Config.seoul_portal.endpoint
        service_key = Config.seoul_portal.service_key

        data_seoul_extract = ExtractPortal(base_url, endpoint, service_key)

        file_path, bucket_name = data_seoul_extract.get_data_seoul()
        expected = {
            "SeoulAdminMesure": {
                "list_total_count": 290636,
                "RESULT": {
                    "CODE": "INFO-000",
                    "MESSAGE": "정상 처리되었습니다"
                },
                "row": [
                    {
                        "CGG_CODE": "3000000",
                        "ADM_DISPO_YMD": "20071128",
                        "GNT_NO": "0090",
                        "SNT_COB_NM": "숙박업(일반)",
                        "SNT_UPTAE_NM": "여관업",
                        "UPSO_NM": "향진",
                        "SITE_ADDR_RD": "서울특별시 종로구 창신길 28-7, (창신동)",
                        "SITE_ADDR": "서울특별시 종로구 창신동  581번지 8호  ",
                        "DRT_INSP_YMD": "20070728",
                        "ADMM_STATE": "처분확정",
                        "DISPO_CTN": "과징금부과 1,800,000",
                        "BAS_LAW": "공중위생관리법",
                        "VIOR_YMD": "20070728",
                        "VIOL_CN": "청소년 이성혼숙 장소제공",
                        "DISPO_CTN_DT": "과징금부과 1,800,000",
                        "DISPO_GIGAN": 0.0,
                        "TRDP_AREA": 82.64
                    },
                    {
                        "CGG_CODE": "3000000",
                        "ADM_DISPO_YMD": "20071228",
                        "GNT_NO": "0091",
                        "SNT_COB_NM": "숙박업(일반)",
                        "SNT_UPTAE_NM": "여관업",
                        "UPSO_NM": "영모텔",
                        "SITE_ADDR_RD": "서울특별시 종로구 보문로7길 5-1, (숭인동)",
                        "SITE_ADDR": "서울특별시 종로구 숭인동  339번지  ",
                        "DRT_INSP_YMD": "20070927",
                        "ADMM_STATE": "처분확정",
                        "DISPO_CTN": "경고",
                        "BAS_LAW": "공중위생관리법",
                        "VIOR_YMD": "20051219",
                        "VIOL_CN": "2005년도 위생교육 미이수",
                        "DISPO_CTN_DT": "경고",
                        "DISPO_GIGAN": 0.0,
                        "TRDP_AREA": 141.95
                    },
                    {
                        "CGG_CODE": "3000000",
                        "ADM_DISPO_YMD": "20190809",
                        "GNT_NO": "0091",
                        "SNT_COB_NM": "숙박업(일반)",
                        "SNT_UPTAE_NM": "여관업",
                        "UPSO_NM": "영모텔",
                        "SITE_ADDR_RD": "서울특별시 종로구 보문로7길 5-1, (숭인동)",
                        "SITE_ADDR": "서울특별시 종로구 숭인동  339번지  ",
                        "DRT_INSP_YMD": "20181106",
                        "ADMM_STATE": "처분확정",
                        "DISPO_CTN": "영업정지 3월",
                        "BAS_LAW": "법 제11조제1항",
                        "VIOR_YMD": "20181106",
                        "VIOL_CN": "성매매알선 등 행위의 처벌에 관한 법률 위반",
                        "DISPO_CTN_DT": "영업정지 3월",
                        "DISPO_GIGAN": 0.0,
                        "TRDP_AREA": 141.95
                    },
                    {
                        "CGG_CODE": "3000000",
                        "ADM_DISPO_YMD": "20131216",
                        "GNT_NO": "0092",
                        "SNT_COB_NM": "숙박업(일반)",
                        "SNT_UPTAE_NM": "일반호텔",
                        "UPSO_NM": "호텔더디자이너스 종로",
                        "SITE_ADDR_RD": "서울특별시 종로구 수표로 89-8, (관수동)",
                        "SITE_ADDR": "서울특별시 종로구 관수동  14번지 1호  ",
                        "DRT_INSP_YMD": "20131125",
                        "ADMM_STATE": "처분확정",
                        "DISPO_CTN": "경고 및 과태료부과",
                        "BAS_LAW": "공중위생관리법 제17조 위반",
                        "VIOR_YMD": "20131125",
                        "VIOL_CN": "2012년 위생교육 미이수",
                        "DISPO_CTN_DT": "경고 및 과태료부과",
                        "DISPO_GIGAN": 0.0,
                        "TRDP_AREA": 999.86
                    },
                    {
                        "CGG_CODE": "3000000",
                        "ADM_DISPO_YMD": "20170609",
                        "GNT_NO": "0097",
                        "SNT_COB_NM": "숙박업(일반)",
                        "SNT_UPTAE_NM": "여관업",
                        "UPSO_NM": "대호",
                        "SITE_ADDR_RD": "서울특별시 종로구 성균관로1길 6-2, (명륜3가)",
                        "SITE_ADDR": "서울특별시 종로구 명륜3가  149번지  ",
                        "DRT_INSP_YMD": "20170512",
                        "ADMM_STATE": "처분확정",
                        "DISPO_CTN": "과징금부과",
                        "BAS_LAW": "법 제11조제1항",
                        "VIOR_YMD": "20170512",
                        "VIOL_CN": "청소년 이성혼숙 장소제공",
                        "DISPO_CTN_DT": "과징금부과",
                        "DISPO_GIGAN": 0.0,
                        "TRDP_AREA": 317.85
                    }
                ]
            }
        }

        data = open(file_path, 'r', encoding='utf-8').read()

        self.assertEqual(expected, data)

        if data:
            print(data)
