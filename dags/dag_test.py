from datetime import datetime, timedelta

import pendulum

# import spotify_auth
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def create_new_year_playlist() -> None:
    """Create new year playlist. To be triggered on 12/31 every year."""
    # Get next year
    year = (datetime.now() + timedelta(days=1)).year
    pendulum.now("Europe/Paris")
    # Playlist informations
    playlist_name = str(year)

    # try:
    #     # Get spotify client
    #     sp = spotify_auth.get_spotify_client()
    #     # Get my user id
    #     user_id = sp.me()["id"]
    #     # Request to create the
    #     sp.user_playlist_create(
    #         user_id, playlist_name, public=True, description=playlist_description
    #     )
    # except Exception:
    #     raise AirflowSkipException

    print(f"Playlist '{playlist_name}' created successfully.")


# DAG definition
default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "schedule_interval": "@yearly",
}

with DAG("test", default_args=default_args) as dag:
    # Use python  operator to run the DAG
    create_playlist_task = PythonOperator(
        task_id="create_spotify_playlist",
        python_callable=create_new_year_playlist,
        dag=dag,
    )
