import time

import requests
import random

bot_key = '5821664449:AAH9Y0TTTmOjgzXDradZSPbVzjpn1WEYbKM'

url = f"https://api.telegram.org/bot{bot_key}/"  # don't forget to change the token!


def last_update(request):
    response = requests.get(request + 'getUpdates')
    print(response)
    response = response.json()
    print(response)
    results = response['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def get_message_text(update):
    message_text = update['message']['text']
    return message_text


def send_message(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    update_id = last_update(url)['update_id']
    while True:
        # pythonanywhere
        time.sleep(3)
        update = last_update(url)
        if update_id == update['update_id']:
            if get_message_text(update).lower() == 'hi' or get_message_text(
                    update).lower() == 'hello' or get_message_text(update).lower() == 'hey':
                send_message(get_chat_id(update), 'Greetings! Type "Dice" to roll the dice!')
            elif get_message_text(update).lower() == 'qa24':
                send_message(get_chat_id(update), 'Python')
            elif get_message_text(update).lower() == 'python':
                send_message(get_chat_id(update), 'version 3.10')
            elif get_message_text(update).lower() == 'dice':
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                send_message(get_chat_id(update),
                             'You have ' + str(_1) + ' and ' + str(_2) + '!\nYour result is ' + str(_1 + _2) + '!')
            else:
                send_message(get_chat_id(update), 'Sorry, I don\'t understand you :(')
            update_id += 1


# print(__name__)
if __name__ == '__main__':
    main()
# print(__name__)
# print('HELLO') #При подключении файла как бибилиотеки import bot, в другой .py файл проекта, этот код будет запускатся при включении того, другого файла
