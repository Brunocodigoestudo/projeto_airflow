from time import sleep
from datetime import datetime
from airflow.decorators import dag, task

@dag(
        dag_id="DAG_PIPALINE",
        description="Pipaline",
        schedule="* * * * *",
        start_date=datetime(2024,11,24),
        catchup=False #backfill
)
def pipeline():

    @task
    def primeira_tarefa():
        print("Finalizou a primeira tarefa")
        sleep(2)

    @task
    def segunda_tarefa():
        print("Finalizou a segunda tarefa")
        sleep(2)

    @task
    def terceira_tarefa():
        print("Finalizou a terceira tarefa")
        sleep(2)

    @task
    def quarta_tarefa():
        print("Finalizou a Pipaline")
        sleep(2)

    t1 = primeira_tarefa()
    t2 = primeira_tarefa()
    t3 = primeira_tarefa()
    t4 = quarta_tarefa()

    t1>>t2>>t3>>t4

