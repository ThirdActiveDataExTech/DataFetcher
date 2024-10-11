import os
from datetime import datetime


import psycopg2


def load_portal_meta(**context):
    filepath = context['filepath'].xcom_pull(task_ids='load_portal')

    conn = psycopg2.connect(
        host="localhost",
        database="airflow_db",
        user="airflow",
        password="201920818"
    )

    cur = conn.cursor()

    bucket_name = "my-bucket"
    file_path = filepath
    file_name = os.path.basename(file_path)
    object_name = file_name

    try:
        file_size = os.path.getsize(file_path)
        upload_time = datetime.now()
        object_url = f"http://your-minio-server:9000/{bucket_name}/{object_name}"

        insert_query = """
            INSERT INTO file_metadata (file_name, upload_time, file_size, bucket_name, object_url)
            VALUES (%s, %s, %s, %s, %s)
        """
        cur.execute(insert_query, (file_name, upload_time, file_size, bucket_name, object_url))
        conn.commit()

        print(f"파일 '{file_name}' 메타데이터가 PostgreSQL에 저장되었습니다.")

    except psycopg2.Error as db_error:
        print(f"PostgreSQL 저장 중 오류 발생: {db_error}")
        conn.rollback()
    finally:
        conn.close()
