''' Load DAG '''
from datetime import datetime
from airflow.providers.standard.operators.bash import BashOperator
from airflow import DAG

with DAG('load_dag',
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False) as dag:

    load_task = BashOperator(
        task_id='load_task',
        bash_command='echo -e ".separator ","\n.import --skip 1 /Users/Siddharth.Kothari/Desktop/Airflow-DAG-Examples/temp/lab/orchestrated/airflow-transform-data.csv top_level_domains" | sqlite3 /Users/Siddharth.Kothari/Desktop/Airflow-DAG-Examples/temp/lab/orchestrated/airflow-load-db.db',
        dag=dag
    )

