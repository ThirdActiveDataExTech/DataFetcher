from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from extract_blog.blog import extract_blog_url
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


def fetch_data_portal_def(**kwargs):
    params = {"page": "1", "perPage": "3", "returnType": "JSON"}
    try:
        data, bucket_name = data_portal_api.get_data_portal(params)
        kwargs['ti'].xcom_push(key='portal_data', value=data)
        kwargs['ti'].xcom_push(key='bucket_name', value=bucket_name)
        return data
    except Exception as e:
        print("fetch data portal def error")
        raise Exception(e)


def crawling_blog_def(**kwargs):
    try:
        data = extract_blog_url.blog_crawler()
        kwargs['ti'].xcom_push(key='blog_data', value=data)
        return data
    except Exception as e:
        print("fetch data blog def error")
        raise Exception(e)


def load_portal_def(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='get_data_portal_task', key='portal_data')
    bucket_name = ti.xcom_pull(task_ids='get_bucket_name', key='bucket_name')
    if data:
        file_path, file_size, bucket_name = load_data(data, bucket_name)
        kwargs['ti'].xcom_push(key='file_path', value=file_path)
        kwargs['ti'].xcom_push(key='file_size', value=file_size)
        kwargs['ti'].xcom_push(key='bucket_name', value=bucket_name)
    else:
        print("No data received")


def load_portal_meta_def(**kwargs):
    ti = kwargs['ti']
    file_path = ti.xcom_pull(task_ids='load_portal_task', key='file_path')
    file_size = ti.xcom_pull(task_ids='load_portal_task', key='file_size')
    bucket_name = ti.xcom_pull(task_ids='load_portal_task', key='bucket_name')
    if file_path:
        load_meta_data(file_path, file_size, bucket_name)


get_data_portal_task = PythonOperator(
    task_id='get_data_portal_task',
    python_callable=fetch_data_portal_def,
    dag=dag,
    do_xcom_push=True
)

get_data_blog_task = PythonOperator(
    task_id='get_data_blog_task',
    python_callable=crawling_blog_def,
    dag=dag,
    do_xcom_push=True
)

load_data_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load_portal_def,
    dag=dag,
)

load_meta_data_task = PythonOperator(
    task_id='load_meta_data_task',
    python_callable=load_portal_meta_def,
    dag=dag,
)

get_data_portal_task >> load_data_task >> load_meta_data_task
get_data_blog_task >> load_data_task >> load_meta_data_task
