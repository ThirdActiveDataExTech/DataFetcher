from minio import Minio, S3Error
from io import BytesIO
import json


def save_data_to_minio(url, response):
    client = Minio(
        url,  # MinIO 서버 주소
        access_key="your-access-key",  # 액세스 키
        secret_key="your-secret-key",  # 시크릿 키
        secure=True
    )
    json_str = json.dumps(response, ensure_ascii=False, indent=4)
    data = BytesIO(json_str.encode('utf-8'))

    # MinIO에 파일 업로드
    bucket_name = "my-bucket"
    object_name = "api_response_data.txt"

    try:
        # MinIO에 데이터 업로드
        client.put_object(
            bucket_name,
            object_name,
            data,
            length=len(response.content),
            content_type="text/plain"
        )
        print("파일이 MinIO에 성공적으로 업로드되었습니다.")
    except S3Error as err:
        print(f"MinIO 업로드 실패: {err}")

    filepath = f"{url}/{bucket_name}/{object_name}"
    return filepath