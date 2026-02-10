'''One Task DAG'''
from datetime import datetime
from airflow.providers.standard.operators.bash import BashOperator
from airflow import DAG

default_args = {
        'owner': 'Siddharth',
        'depends_on_past': False,
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 0,
        'catchup': False,
        'start_date': datetime(2023, 1, 1)
}

with DAG(
        dag_id='one_task_dag', # name of the DAG, should be unique across the Airflow instance
        description='A one task Airflow DAG', # description of the DAG, optional but good to have
        schedule=None, # to define interval to repeat, not needed here
        default_args=default_args
    ) as dag:

    task1 = BashOperator(
            task_id='one_task', # name of the task, should be unique within the DAG
            bash_command='echo "hello, world!" > /Users/Siddharth.Kothari/Desktop/Airflow-DAG-Examples/temp/create-this-file.txt',
            dag=dag) # specifying the DAG that this task belongs to, not needed here since we are using context manager (with DAG(...) as dag)
