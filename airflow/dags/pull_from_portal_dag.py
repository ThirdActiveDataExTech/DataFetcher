from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from src.extract.extract_portal import ExtractPortal
from src.load.load_portal import load_portal
from src.load.load_portal_meta import load_portal_meta

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
    schedule=None,
)

get_data_portal = PythonOperator(
    task_id='get_data_portal',
    python_callable=ExtractPortal.get_data_portal,
    op_args=["api.odcloud.kr/api", "/15113444/v1/uddi:1ae26320-fa56-4206-8d06-9ee5db5a8dcf",
             {"serviceKey": "xP4pzOKZFbsWOwq3JF9vXjeGW8FbftsjacKe8Os%2BbMnaK8U7gIWVZsTVtFnGRN5W6KvqrpApm9pIeQxIEMcrAw"
                            "%3D%3D",
              "page": "1", "perPage": "3", "returnType": "JSON"}],
    dag=dag,
)

load_portal = PythonOperator(
    task_id='load_portal',
    python_callable=load_portal,
    dag=dag
)

load_potal_meta = PythonOperator(
    task_id='load_potal_meta',
    python_callable=load_portal_meta,
    dag=dag,
)

get_data_portal >> load_portal >> load_potal_meta
