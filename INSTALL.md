# Apache Airflow Installation Steps

The first step is to configure the Apache Airflow Home Directory using - 

```
nano ~/.zshrc
```

Add the following line to the file

```
export AIRFLOW_HOME=~/airflow
```

Save the configuration and load it into the current terminal using 

```
source ~/.zshrc
```

Now, to install Apache Airflow, use the command - 

```
pip install apache-airflow==AIRFLOW_VERSION --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-AIRFLOW_VERSION/constraints-PYTHON_VERSION.txt"
```

Here AIRFLOW_VERSION should be replaced by the version you want to install, and the PYTHON_VERSION should be replaced by the python version installed on the system. The existence of the .txt file should be checked beforehand, which can be used to indicate the versions of python which are compatible with this version of Airflow. 

Once Airflow is installed, start the db instance using 

```
airflow db migrate
```

The configuration file for Airflow can be found at AIRFLOW_HOME/airflow.cfg. Change the auth_manager line to the following and save the file - 

```
auth_manager = airflow.providers.fab.auth_manager.fab_auth_manager.FabAuthManager
```

Also, disable the examples being loaded by changing the following in the AIRFLOW_HOME/airflow.cfg file.

```
load_examples = False
```

We then need to create an Admin user, which can be done using the following command - 

```
airflow users create \
    --username admin \
    --firstname YOUR_NAME \
    --lastname YOUR_LAST_NAME \
    --role Admin \
    --email admin@example.com \
    --password your_new_password
```

Finally, we need to start the Airflow Web Server UI (which can be used to view the Airflow DAGS running) and the Airflow Scheduler (which is used to schedule and run the DAGs). Run the following commands on 2 separate terminals - 

```
airflow api-server --port 8080
airflow scheduler
```

The Airflow UI can now be accessed at port 8080. To run any new DAGs, they should be created in the AIRFLOW_HOME/dags folder, which can be changed in the AIRFLOW_HOME/airflow.cfg file by changing the line - 

```
dags_folder = /path/to/folder/containing/dags
```

Finally, when a new DAG is created, to view if the syntax is correct, use the command - 

```
python3 -W ignore dag_file_name.py
```

Occassionally, to see new DAG files in the UI, we may need to reserialize the dags, which can be done using the command - 

```
airflow dags reserialize
```