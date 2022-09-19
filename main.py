#!/bin/python3

# Заполнить API_TOKEN telegrambot
# Заполнить TELEGRAM_USERID
# Заполнить команду для выполнения COMMNAD_LINE
# Заполнить строку что нужно парсить USER_NICKNAME

import subprocess
import requests

def sendNotification(message):
    url = "https://api.telegram.org/bot" + f'API_TOKEN'
    method = url + "/sendMessage"

    requests.post(method, data={
        "chat_id": 'TELEGRAM_USERID',
        "text": message
    })
    print('Отправлено')

def main(nickname: str): 
    data = str(subprocess.check_output('COMMNAD_LINE', stderr=subprocess.STDOUT, shell=True))
    if nickname in data:
        sendNotification(message=f'{nickname} зашёл на сервер')

if __name__ == '__main__':
    main(nickname='USER_NICKNAME')
