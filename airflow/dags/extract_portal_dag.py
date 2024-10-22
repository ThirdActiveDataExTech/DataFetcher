from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from extract_portal.extract_portal import ExtractPortal
from load.load_data import load_data
from load.load_meta_data import load_meta_data

default_args = {
    'owner': 'admin',
    'start_date': datetime(2023, 9, 19),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='extract_portal_dag',
    default_args=default_args,
    description='Extract Data From Portal and Load To DB DAG',
    schedule_interval=None,
)

data_portal_api = ExtractPortal(
    "api.odcloud.kr/api",
    "/15113444/v1/uddi:1ae26320-fa56-4206-8d06-9ee5db5a8dcf",
    "xP4pzOKZFbsWOwq3JF9vXjeGW8FbftsjacKe8Os%2BbMnaK8U7gIWVZsTVtFnGRN5W6KvqrpApm9pIeQxIEMcrAw%3D%3D"
)


def crawling_portal_def(**kwargs):
    params = {"page": "1", "perPage": "3", "returnType": "JSON"}
    try:
        file_path, bucket_name = data_portal_api.get_data_portal(params)
    except Exception as e:
        print(f"fetch data portal def error : {e}")
        raise Exception(e)
    kwargs['ti'].xcom_push(key='file_path', value=file_path)
    kwargs['ti'].xcom_push(key='bucket_name', value=bucket_name)


def load_portal_def(**kwargs):
    ti = kwargs['ti']
    file_path = ti.xcom_pull(task_ids='crawling_portal_task', key='file_path')
    bucket_name = ti.xcom_pull(task_ids='crawling_portal_task', key='bucket_name')
    if file_path:
        minio_path, file_size, bucket_name = load_data(file_path, bucket_name)
        kwargs['ti'].xcom_push(key='minio_path', value=minio_path)
        kwargs['ti'].xcom_push(key='file_size', value=file_size)
        kwargs['ti'].xcom_push(key='bucket_name', value=bucket_name)
    else:
        print("No data received")


def load_portal_meta_def(**kwargs):
    ti = kwargs['ti']
    minio_path = ti.xcom_pull(task_ids='load_portal_task', key='minio_path')
    file_size = ti.xcom_pull(task_ids='load_portal_task', key='file_size')
    bucket_name = ti.xcom_pull(task_ids='load_portal_task', key='bucket_name')
    if minio_path:
        load_meta_data(minio_path, file_size, bucket_name)


crawling_portal_task = PythonOperator(
    task_id='crawling_portal_task',
    python_callable=crawling_portal_def,
    dag=dag,
    do_xcom_push=True
)

load_portal_task = PythonOperator(
    task_id='load_portal_task',
    python_callable=load_portal_def,
    dag=dag,
)

load_portal_meta_task = PythonOperator(
    task_id='load_portal_meta_task',
    python_callable=load_portal_meta_def,
    dag=dag,
)

crawling_portal_task >> load_portal_task >> load_portal_meta_task
