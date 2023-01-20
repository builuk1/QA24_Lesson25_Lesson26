import random
from mensa_logger import mensa_log_to_file
from selenium import webdriver
import time

driver = webdriver.Chrome()

url = 'https://test.mensa.no/'

driver.get(url)
driver.maximize_window()

xpath_button_18_50 = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[2]'
button_18_50 = driver.find_element('xpath',xpath_button_18_50)
button_18_50.click()

xpath_button_start = '/html/body/div[2]/main/cach/div[2]/div/div/div/div[2]/button'
button_start = driver.find_element('xpath',xpath_button_start)
button_start.click()
time.sleep(2)
xpath_button_q1_a1 = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_q1_a1 = driver.find_element('xpath', xpath_button_q1_a1)
button_q1_a1.click()
mensa_log_to_file(xpath_button_q1_a1)
time.sleep(2)
xpath_button_q2_a1 = '/html/body/div[2]/main/cach/div[3]/div[2]/div[3]/div[1]/div/img'
button_q2_a1 = driver.find_element('xpath', xpath_button_q2_a1)
button_q2_a1.click()
mensa_log_to_file(xpath_button_q2_a1)
time.sleep(2)
xpath_button_q3_a1 = '/html/body/div[2]/main/cach/div[3]/div[3]/div[3]/div[1]/div/img'
button_q3_a1 = driver.find_element('xpath', xpath_button_q3_a1)
button_q3_a1.click()
mensa_log_to_file(xpath_button_q3_a1)
time.sleep(2)
for i in range(4,35+1):
    a = random.randint(1,6)
    xpath_button_q_a1 = f'/html/body/div[2]/main/cach/div[3]/div[{i}]/div[3]/div[{a}]/div/img'
    button_q_a1 = driver.find_element('xpath', xpath_button_q_a1)
    button_q_a1.click()
    mensa_log_to_file(xpath_button_q_a1)
    time.sleep(2)
time.sleep(10)