from airflow.models import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import days_ago

with DAG(
    "etl_sales_daily",
    start_date=days_ago(1),
    schedule_interval=None,
) as dag:
    task_a = EmptyOperator(task_id="task_a")
    task_b = EmptyOperator(task_id="task_b")
    task_c = EmptyOperator(task_id="task_c")
    task_d = EmptyOperator(task_id="task_d")

    task_a >> [task_b, task_c]
    task_c >> task_d
