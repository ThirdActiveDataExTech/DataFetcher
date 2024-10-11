from minio import Minio, S3Error
from io import BytesIO
import json


def load_portal(**context):
    print("this is load portal data module")
    response = context['request'].xcom_pull(task_ids='get_data_portal')
    url = "minio-server-url"
    client = Minio(
        url,
        access_key="your-access-key",
        secret_key="your-secret-key",
        secure=True
    )
    json_str = json.dumps(response, ensure_ascii=False, indent=4)
    data = BytesIO(json_str.encode('utf-8'))

    bucket_name = "my-bucket"
    object_name = "api_response_data.txt"

    try:
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