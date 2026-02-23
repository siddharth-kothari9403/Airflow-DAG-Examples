from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

default_args = {
    'owner' : 'Siddharth'
}

def print_function():
    print("The simplest possible Python operator!")

with DAG(
    dag_id = 'execute_python_operators',
    description = 'Python operators in DAGs',
    default_args = default_args,
    # schedule_interval = '@daily',
    schedule=None,
    tags = ['simple', 'python']
) as dag:
    
    task = PythonOperator(
        task_id = 'python_task',
        python_callable = print_function
    ) 