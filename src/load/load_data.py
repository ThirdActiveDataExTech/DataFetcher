import os

import urllib3
from minio import Minio, S3Error


def load_data(file_path, bucket_name):
    url = "0.0.0.0:1"
    client = Minio(
        url,
        access_key="admin",
        secret_key="secretkey",
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

    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)

    if bucket_name == "blog":
        minio_file_path = []
        file_size = []
        for path in file_path:
            file_name = os.path.basename(path)
            try:
                client.fput_object(bucket_name, file_name, path)
                print(f"'{file_name}' 파일이 '{bucket_name}' 버킷에 업로드되었습니다.")
            except S3Error as e:
                print(f"파일 업로드 중 에러가 발생했습니다: {e}")
            minio_path = "http://" + url + "/" + bucket_name + "/" + file_name
            minio_file_path.append(minio_path)

            size = os.path.getsize(file_path)
            file_size.append(size)
    else:
        file_name = os.path.basename(file_path)
        try:
            client.fput_object(bucket_name, file_name, file_path)
            print(f"'{file_name}' 파일이 '{bucket_name}' 버킷에 업로드되었습니다.")
        except S3Error as e:
            print(f"파일 업로드 중 에러가 발생했습니다: {e}")

        minio_file_path = "http://" + url + "/" + bucket_name + "/" + file_name
        file_size = os.path.getsize(file_path)
    return minio_file_path, file_size, bucket_name
