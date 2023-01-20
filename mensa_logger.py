import time

import requests


def mensa_log_to_file(xpath):
    # xpath_button_q_a1 = f'/html/body/div[2]/main/cach/div[3]/div[{i}]/div[3]/div[{a}]/div/img'
    q_n = xpath[39:41]
    q = q_n
    if ']' in q_n:
        q = q_n[0]
    a = xpath[-10]
    f = open('mensalog.txt', 'at')
    if q == '1':
        f.write('\n')
        f.write('**********************************************************')
        f.write('\n')
        f.write('\n')
        f.write(str(time.time()))
        f.write('\n')
    d = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f'}
    s = f'Question : {q} Answer {d[a]}'
    f.write(s)
    f.write('\n')
    f.close()

def time_site(url):
    a = time.time()
    b = requests.get(url)
    c = time.time()
    return str(c-a)