# import necessary libraries
import airflow 
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys

sys.path.append("/Users/austin/Desktop/Link_Slack_Bot")

from scripts.sga_scrape import scrape_bad_urls
from scripts.post_message import post_quote_to_channel



# define DAG
bl_dag=DAG(
    dag_id="broken_links",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None,
)



# write operators
get_links = PythonOperator(
    task_id = "get_links",
    python_callable=scrape_bad_urls,
    dag=bl_dag,
)

post_message = PythonOperator(
    task_id = "get_players",
    python_callable=post_quote_to_channel,
    dag=bl_dag,
)


# structure dag
get_links >> post_message
