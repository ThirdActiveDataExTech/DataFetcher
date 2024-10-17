import os

import urllib3
from minio import Minio, S3Error
import json
import uuid

from src.extract.extract_portal import ExtractPortal


def load_portal(response):
    url = "192.168.107.19:9004"
    client = Minio(
        url,
        access_key="admin",
        secret_key="201920818",
        secure=False,
        http_client=urllib3.PoolManager(
            timeout=urllib3.Timeout.DEFAULT_TIMEOUT,
            retries=urllib3.Retry(
                total=1,
                backoff_factor=0.2,
                status_forcelist=()
            )
        )
    )

    file_name = str(uuid.uuid4()) + ".txt"
    file_dir = "./extract_files/portal/"
    file_path = file_dir + file_name
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    bucket_name = "dataportal"
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(response, f, ensure_ascii=False, indent=4)
    except S3Error as e:
        print(f"파일 저장 실패: {e}")

    try:
        client.fput_object(bucket_name, file_name, file_path)
        print(f"'{file_name}' 파일이 '{bucket_name}' 버킷에 업로드되었습니다.")
    except S3Error as e:
        print(f"파일 업로드 중 에러가 발생했습니다: {e}")

    minio_file_path = "http://" + url + "/" + bucket_name + "/" + file_name
    file_size = os.path.getsize(file_path)
    return minio_file_path, file_size




