from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.models import Variable

default_args = {
    'owner': 'Siddharth'
}

employees_table = Variable.get("emp", default_var=None)
departments_table = Variable.get("dept", default_var=None)
employees_departments_table = Variable.get("emp_dept", default_var=None)

with DAG(
        'running_sql_queries',
        description = 'Here we are creating a simple pipeline using SqliteOperator.',
        default_args = default_args,
        schedule = None,
        template_searchpath = '/Users/Siddharth.Kothari/airflow/sql_statements'
) as dag:
    
    create_employees_table = SQLExecuteQueryOperator(
        task_id='create_employees_table',
        sql='create_employee_table.sql',
        params={'employees_table': employees_table},
        conn_id='my_sqlite_comm'
    )

    create_departments_table = SQLExecuteQueryOperator(
        task_id='create_departments_table',
        sql='create_department_table.sql',
        params={'departments_table': departments_table},
        conn_id='my_sqlite_comm'
    )

    insert_data_employees = SQLExecuteQueryOperator(
        task_id='insert_data_employees',
        sql='insert_data_employees.sql',
        params={'employees_table': employees_table},
        conn_id='my_sqlite_comm'
    )

    insert_data_departments = SQLExecuteQueryOperator(
        task_id='insert_data_departments',
        sql='insert_data_departments.sql',
        params={'departments_table': departments_table},
        conn_id='my_sqlite_comm'
    )

    join_tables = SQLExecuteQueryOperator(
        task_id='join_tables',
        sql='join_table.sql',
        params={'employees_departments_table': employees_departments_table},
        conn_id='my_sqlite_comm'
    )

    result_sql = SQLExecuteQueryOperator(
        task_id='result_sql',
        sql='display_emp_dept.sql',
        params={'employees_departments_table': employees_departments_table},
        conn_id='my_sqlite_comm',
        do_xcom_push=True
    )

    create_employees_table >> insert_data_employees
    create_departments_table >> insert_data_departments
    [insert_data_employees, insert_data_departments] >> join_tables >> result_sql
