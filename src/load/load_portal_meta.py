import os
from datetime import datetime


import psycopg2


def load_portal_meta(file_path, file_size, bucket_name):

    if bucket_name == 'dataportal':
        database = "portalmeta"
    elif bucket_name == 'seoulportal':
        database = "seoulportal"
    else:
        database = "blog"

    conn = psycopg2.connect(
        host="0.0.0.0:0",
        database="dbname",
        user="admin",
        password="admin",
        port=5432
    )

    cur = conn.cursor()

    file_name = os.path.basename(file_path)

    try:
        insert_query = """
            INSERT INTO file_metadata (file_name, upload_time, file_size, file_path)
            VALUES (%s, %s, %s, %s)
        """
        cur.execute(insert_query, (file_name, datetime.now(), file_size, file_path))
        conn.commit()

        print(f"메타데이터가 PostgreSQL에 저장되었습니다.")

    except psycopg2.Error as db_error:
        print(f"PostgreSQL 저장 중 오류 발생: {db_error}")
        conn.rollback()
    finally:
        conn.close()
