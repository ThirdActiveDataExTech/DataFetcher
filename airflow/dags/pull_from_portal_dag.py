from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from extract.extract_portal import ExtractPortal
from load.load_portal import load_portal
from load.load_portal_meta import load_portal_meta

default_args = {
    'owner': 'admin',
    'start_date': datetime(2023, 9, 19),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='pull_from_portal_dag',
    default_args=default_args,
    description='Pull Data From Portal and Load To DB DAG',
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
        data = data_portal_api.get_data_portal(params)
        kwargs['ti'].xcom_push(key='portal_data', value=data)
        return data
    except Exception as e:
        print("fetch data portal def error")
        raise Exception(e)


def load_portal_def(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='get_data_portal_task', key='portal_data')
    if data:
        file_path, file_size = load_portal(data)
        kwargs['ti'].xcom_push(key='file_path', value=file_path)
        kwargs['ti'].xcom_push(key='file_size', value=file_size)
    else:
        print("No data received")


def load_portal_meta_def(**kwargs):
    ti = kwargs['ti']
    file_path = ti.xcom_pull(task_ids='load_portal_task', key='file_path')
    file_size = ti.xcom_pull(task_ids='load_portal_task', key='file_size')
    if file_path:
        load_portal_meta(file_path, file_size)


get_data_portal_task = PythonOperator(
    task_id='get_data_portal_task',
    python_callable=fetch_data_portal_def,
    dag=dag,
    retries=3,
    do_xcom_push=True
)

load_portal_task = PythonOperator(
    task_id='load_portal_task',
    python_callable=load_portal_def,
    dag=dag,
    retries=3,
)

load_portal_meta_task = PythonOperator(
    task_id='load_portal_meta_task',
    python_callable=load_portal_meta_def,
    dag=dag,
    retries=3,
)

get_data_portal_task >> load_portal_task >> load_portal_meta_task
