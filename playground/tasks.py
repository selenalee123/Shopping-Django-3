from time import sleep
from celery import shared_task

@shared_task
def notify_customers(message):
    print('Sending email to customers...')
    print(message)
    sleep(10)
    print('Email sent to customers.')   