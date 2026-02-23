import pandas as pd
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
import io

default_args = {
   'owner': 'Siddharth'
}

def read_csv_file():
    df = pd.read_csv('/Users/Siddharth.Kothari/airflow/datasets/insurance.csv')
    print(df)
    return df.to_json()

def remove_null_values(ti):
    json_data = ti.xcom_pull(task_ids='read_csv_file')
    df = pd.read_json(io.StringIO(json_data))
    df = df.dropna()
    print(df)
    return df.to_json()

def groupby_smoker(ti):
    json_data = ti.xcom_pull(task_ids='remove_null_values')
    df = pd.read_json(io.StringIO(json_data))

    smoker_df = df.groupby('smoker').agg({
        'age': 'mean', 
        'bmi': 'mean',
        'charges': 'mean'
    }).reset_index()

    smoker_df.to_csv(
        '/Users/Siddharth.Kothari/airflow/output/grouped_by_smoker.csv', index=False)

def groupby_region(ti):
    json_data = ti.xcom_pull(task_ids='remove_null_values')
    df = pd.read_json(io.StringIO(json_data))

    region_df = df.groupby('region').agg({
        'age': 'mean', 
        'bmi': 'mean', 
        'charges': 'mean'
    }).reset_index()
    
    region_df.to_csv(
        '/Users/Siddharth.Kothari/airflow/output/grouped_by_region.csv', index=False)


with DAG(
    dag_id = 'python_pipeline',
    description = 'Running a Python pipeline',
    default_args = default_args,
    schedule = '@once',
    tags = ['python', 'transform', 'pipeline']
) as dag:
    
    read_csv_file = PythonOperator(
        task_id='read_csv_file',
        python_callable=read_csv_file
    )

    remove_null_values = PythonOperator(
        task_id='remove_null_values',
        python_callable=remove_null_values
    )
    
    groupby_smoker = PythonOperator(
        task_id='groupby_smoker',
        python_callable=groupby_smoker
    )
    
    groupby_region = PythonOperator(
        task_id='groupby_region',
        python_callable=groupby_region
    )

read_csv_file >> remove_null_values >> [groupby_smoker, groupby_region]