import os
from datetime import datetime
from config.config import Config


import psycopg2


def load_meta_data(file_path, file_size, bucket_name):

    if bucket_name == 'dataportal':
        database = "portalmeta"
    elif bucket_name == 'seoulportal':
        database = "seoulportal"
    else:
        database = "blog"

    conn = psycopg2.connect(
        host=Config.postgres_server.host,
        database=database,
        user=Config.postgres_server.user,
        password=Config.postgres_server.password,
        port=Config.postgres_server.port
    )

    cur = conn.cursor()

    if bucket_name == 'blog':
        num = 0
        for path in file_path:
            file_name = os.path.basename(path)
            try:
                insert_query = """
                    INSERT INTO file_metadata (file_name, upload_time, file_size, file_path)
                    VALUES (%s, %s, %s, %s)
                """
                cur.execute(insert_query, (file_name, datetime.now(), file_size[num], path))
                conn.commit()

                num += 1
            except psycopg2.Error as db_error:
                print(f"PostgreSQL 저장 중 오류 발생: {db_error}")
                conn.rollback()
    else:
        file_name = os.path.basename(file_path)
        try:
            insert_query = """
                INSERT INTO file_metadata (file_name, upload_time, file_size, file_path)
                VALUES (%s, %s, %s, %s)
            """
            cur.execute(insert_query, (file_name, datetime.now(), file_size, file_path))
            conn.commit()

        except psycopg2.Error as db_error:
            print(f"PostgreSQL 저장 중 오류 발생: {db_error}")
            conn.rollback()

    conn.close()
    return "메타데이터가 PostgreSQL에 저장되었습니다."
