from time import sleep
from loguru import logger ## pacote para log, monitoramento o que foi feito

logger.add("execution_logas.log", format="{time} - {message}", level="INFO", rotation="1 day")

def primeira_tarefa():
    #print("Finalizou a primeira tarefa")
    logger.info("Finalizou a primeira tarefa") #log
    sleep(2)

def segunda_tarefa():
    #print("Finalizou a segunda tarefa")
    logger.info("Finalizou a segunda tarefa") #log
    sleep(2)

def terceira_tarefa():
    #print("Finalizou a terceira tarefa")
    logger.info("Finalizou a terceira tarefa") #log
    sleep(2)

def pipeline():
    primeira_tarefa()
    primeira_tarefa()
    primeira_tarefa()
    #print("Pipeline Finalizou")
    logger.info("Pipeline Finalizou")

if __name__ == "__main__":
    while True: ##loop 
        pipeline()
        sleep(10)

