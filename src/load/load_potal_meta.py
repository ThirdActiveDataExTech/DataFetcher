import psycopg2
from datetime import datetime
from minio import Minio
from minio.error import S3Error
import os


def load_potal_meta(filepath):

    # MinIO 클라이언트 초기화
    client = Minio(
        "your-minio-server:9000",  # MinIO 서버의 URL 및 포트
        access_key="your-access-key",  # 액세스 키
        secret_key="your-secret-key",  # 비밀 키
        secure=False  # HTTPS 사용 여부
    )

    # PostgreSQL 연결
    conn = psycopg2.connect(
        host="your-postgres-host",
        database="your-database",
        user="your-username",
        password="your-password"
    )

    # Cursor 생성
    cur = conn.cursor()

    # 업로드할 파일 설정
    bucket_name = "my-bucket"
    file_path = filepath
    file_name = os.path.basename(file_path)
    object_name = file_name

    # 파일 업로드 및 메타데이터 저장
    try:
        # 파일 크기 계산
        file_size = os.path.getsize(file_path)

        # MinIO에 파일 업로드
        client.fput_object(bucket_name, object_name, file_path, content_type="application/octet-stream")

        # 업로드 시간
        upload_time = datetime.now()

        # 객체 URL 생성
        object_url = f"http://your-minio-server:9000/{bucket_name}/{object_name}"

        # PostgreSQL에 메타데이터 삽입
        insert_query = """
            INSERT INTO file_metadata (file_name, upload_time, file_size, bucket_name, object_url)
            VALUES (%s, %s, %s, %s, %s)
        """
        cur.execute(insert_query, (file_name, upload_time, file_size, bucket_name, object_url))

        # 트랜잭션 커밋
        conn.commit()

        print(f"파일 '{file_name}' 메타데이터가 PostgreSQL에 저장되었습니다.")

    except S3Error as exc:
        print(f"MinIO 업로드 중 오류 발생: {exc}")
    except psycopg2.Error as db_error:
        print(f"PostgreSQL 저장 중 오류 발생: {db_error}")
        conn.rollback()  # 오류 발생 시 트랜잭션 롤백
    finally:
        # PostgreSQL 연결 종료
        cur.close()
        conn.close()