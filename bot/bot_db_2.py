import requests
import random
import pickle
import bot

# print(__name__)
# bot.get_chat_id()
bot_key = '5911642173:AAG7Kx7CP480AfzyA8JBEhSFhS9ld0WjV40'

url = f"https://api.telegram.org/bot{bot_key}/"  # don't forget to change the token!

command_d = 'del!'  # Команда на удаление вопроса и ответа
command_c = 'qui!'  # Команда на создание/изменения вопроса и ответа
separator_c = '/|*'  # Знак который указывает, что после него идёт ответ на вопрос
# 'qui!aaa1/|*bbb1'

def last_update(request):
    response = requests.get(request + 'getUpdates')
    response = response.json()
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
    # Проверка наличия файла. Если нет создаёт, если есть, считывает
    try:
        # чтение из файла
        with open('data.pickle', 'rb') as f:
            q_a = pickle.load(f)
    except:
        q_a = {}
        with open('data.pickle', 'wb') as f:
            pickle.dump(q_a, f)
    update_id = last_update(url)['update_id']
    while True:
        update = last_update(url)
        if update_id == update['update_id']:
            command_dictionary = {'day': '04/06/2022', 'pc': 'Dell'}
            with open('data.pickle', 'rb') as f:
                q_a = pickle.load(f)
            if get_message_text(update).lower() == 'hi' or get_message_text(
                    update).lower() == 'hello' or get_message_text(update).lower() == 'hey':
                send_message(get_chat_id(update), 'Greetings! Type "Dice" to roll the dice!')
            # Create
            elif command_c in get_message_text(update).lower():  # '?!temp/20'
                c = get_message_text(update).lower()
                l = len(command_c)
                ls = len(separator_c)
                c = c[l:]
                q = c[:c.find(separator_c)]
                a = c[c.find(separator_c) + ls:]
                q_a[q] = a
                # сохранение в файл
                with open('data.pickle', 'wb') as f:
                    pickle.dump(q_a, f)
                send_message(get_chat_id(update), 'OK')
            # Delete
            elif command_d in get_message_text(update).lower():  # 'd!temp'
                c = get_message_text(update).lower()
                l = len(command_d)
                c = c[l:]
                del q_a[c]
                with open('data.pickle', 'wb') as f:
                    pickle.dump(q_a, f)

                send_message(get_chat_id(update), 'OK')
                # Read
            elif get_message_text(update).lower() in q_a:
                c = get_message_text(update).lower()
                send_message(get_chat_id(update), q_a[c])
            elif get_message_text(update).lower() in command_dictionary:
                c = get_message_text(update).lower()
                send_message(get_chat_id(update), command_dictionary[c])
            elif get_message_text(update).lower() == 'dice':
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                send_message(get_chat_id(update),
                             'You have ' + str(_1) + ' and ' + str(_2) + '!\nYour result is ' + str(_1 + _2) + '!')
            elif get_message_text(update).lower() == 'bot':
                send_message(get_chat_id(update), 'C4012')
            else:
                send_message(get_chat_id(update), 'Sorry, I don\'t understand you :(')
            update_id += 1


if __name__ == '__main__':
    main()
