'''Two Task DAG'''
from datetime import datetime
from airflow.providers.standard.operators.bash import BashOperator
from airflow import DAG

# Default settings applied to all tasks
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
    dag_id='two_task_dag',
    description='A two task Airflow DAG',
    schedule=None, # to define interval to repeat, not needed here
    default_args=default_args
    ) as dag:

    t0 = BashOperator(
        task_id='bash_task_0',
        bash_command='echo "First Airflow task!"' # Check Task Logs to see the output
    )

    t1 = BashOperator(
        task_id='bash_task_1',
        bash_command='echo "Sleeping..." && sleep 5s && echo "Second Airflow task!"'
    ) # not specifying dag=dag since we are using context manager (with DAG(...) as dag)

    t0 >> t1 # specifying dependency, t1 will run after t0 finishes

