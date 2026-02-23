from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

default_args = {
    'owner' : 'siddharth'
}

def greet_hello(name):
    print(f"Hello, {name}!")

def greet_hello_with_city(name, city):
    print(f"Hello, {name} from {city}")

with DAG(
    dag_id = 'execute_python_operators_with_arguments',
    description = 'Python operators in DAGs with parameters',
    default_args = default_args,
    # schedule_interval = '@daily',
    schedule = None,
    tags = ['parameters', 'python']
) as dag:

    taskA = PythonOperator(
        task_id = 'greet_hello',
        python_callable = greet_hello,
        op_kwargs={'name': 'Desmond'}
    )

    taskB = PythonOperator(
        task_id = 'greet_hello_with_city',
        python_callable = greet_hello_with_city,
        op_kwargs={'name': 'Louise', 'city': 'Seattle'}
    )

    taskA >> taskB