from os import system
from time import sleep
from datetime import datetime

def clean_scream():
    system('clear') or None


def custom_sleep(secunds):
    sleep(secunds)
    
def date_today():
    return datetime.now()

def format_date(date_convert):
    date_convert = datetime.strptime(date_convert, '%Y-%m-%d %H:%M:%S.%f')
    date_convert = date_convert.strftime('%d-%m-%Y %H:%M:%S')
    return date_convert