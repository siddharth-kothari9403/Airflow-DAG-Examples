from datetime import timedelta
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id = 'executing_multiple_tasks',
    description = 'DAG with multiple tasks and dependencies',
    # schedule_interval = timedelta(days=1)
    schedule = None,
    tags = ['scripts', 'template search'],
    template_searchpath = '/Users/Siddharth.Kothari/airflow/dags/bash_scripts'
) as dag:

    taskA = BashOperator(
        task_id = 'taskA',
        bash_command = 'taskA.sh'
    )

    taskB = BashOperator(
        task_id = 'taskB',
        bash_command = 'taskB.sh'
    )

    taskC = BashOperator(
        task_id = 'taskC',
        bash_command = 'taskC.sh'
    )
    
    taskD = BashOperator(
        task_id = 'taskD',
        bash_command = 'taskD.sh'
    )

    taskE = BashOperator(
        task_id = 'taskE',
        bash_command = 'taskE.sh'
    )

    taskF = BashOperator(
        task_id = 'taskF',
        bash_command = 'taskF.sh'
    )

    taskG = BashOperator(
        task_id = 'taskG',
        bash_command = 'taskG.sh'
    )

    taskA >> taskB >> taskE
    taskA >> taskC >> taskF
    taskA >> taskD >> taskG
