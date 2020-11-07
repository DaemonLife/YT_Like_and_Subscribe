from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import platform # определение платформы
import threading, random
from datetime import timedelta, datetime

from urllib.request import urlopen
import pickle # печеньки

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def licence(d, m, y):
   res = urlopen('http://just-the-time.appspot.com/')
   result = res.read().strip()
   result_str = result.decode('utf-8')
   x = result_str.split(" ")
   today_date = x[0].split("-")
   now = datetime(int(today_date[0]), int(today_date[1]), int(today_date[2]))
   end_time = datetime(y, m, d)
   print(end_time)
   print(now)
   if (now >= end_time):
       if (os.path.exists(BASE_DIR + 'key5543y7.txt') == 1):
           print('Key is here')
           return 1
       print('Заплати - и получи ключ!')
       return 0
   else:
       return 1

def my_system():
    my_sys = (platform.platform())[:5]
    if my_sys == "Linux":
        return "Linux"
    elif my_sys == "Windo":
        return "Windows"
    elif my_sys == "macOS":
        return "MacOS"

if (my_system() == "Linux") or (my_system() == "MacOS"):
    BASE_DIR += "/"
elif my_system() == "Windo":
    BASE_DIR += "\\"
else:
    print('Ошибка определения вашей системы')

def driver_start():
    my_sys = my_system()
    if my_sys == "Windows":
        driver_path = 'driver\\Windows\\chromedriver.exe'
    elif my_sys == "Linux":
        driver_path = 'driver/Linux/chromedriver'
    elif my_sys == "MacOS":
        driver_path = 'driver/MacOS/chromedriver'

    opts = Options()

    mobile_emulation = { "deviceName": "iPhone X" } # type your device from list
    opts.add_experimental_option("mobileEmulation", mobile_emulation)

    # opts.add_argument("--headless") 
    driver = webdriver.Chrome(chrome_options=opts, executable_path=r'' + BASE_DIR + driver_path)

    return driver # возвращаем объект

def open_accounts():

    my_sys = my_system()
    if my_sys == "Windows":
        file_path = 'files\\accounts.txt'
    elif my_sys == "Linux":
        file_path = 'files/accounts.txt'
    elif my_sys == "MacOS":
        file_path = 'files/accounts.txt'

    f = open(BASE_DIR + file_path, 'r')
    acc_list = []
    for line in f:
        acc_list.append(line)
    f.close()
    return acc_list

def pro_send_keys(element, text):
    t = 0
    while t < 5:
        try:
            element.send_keys(text)
            return None
        except:
            t += 1
            sleep(1)

def pro_click(element):
    t = 0
    while t < 5:
        try:
            element.click()
            return None
        except:
            t += 1
            sleep(1)

def google_authorization(finder, login, password, verification_email):
    driver = finder.driver
    driver.get('https://accounts.google.com/signin/oauth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3ABBC%2C16%3A9b15b0994c6df9fc%2C10%3A1591711286%2C16%3A66b338ce162d6599%2Ca78a0c663f0beb12c0559379b61a9f5d62868c4fbd2f00e46a86ac26796507a1%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22921f8f04441041069683cc2377152422%22%7D&response_type=code&o2v=1&as=NCQvtBXI4prkLLDbn4Re0w&flowName=GeneralOAuthFlow')

    # вход в другой аккаунт
    try:
        el = "//*[contains(text(), 'Сменить аккаунт')]"
        el = finder.element_by_xpath(el, 6)
        pro_click(el)
    except:
        pass

    # отправить почту | номер телефона
    el = finder.element_by_name('identifier', 5)
    pro_send_keys(el, login)
    # кнопка Далее
    el = finder.element_by_xpath('//*[@id="identifierNext"]/div/button', 5)
    sleep(random.uniform(0.5,1))
    pro_click(el)

    # отправить пароль
    el = finder.element_by_name('password', 5)
    pro_send_keys(el, password)
    # кнопка Далее
    el = finder.element_by_xpath('//*[@id="passwordNext"]/div/button', 5)
    sleep(random.uniform(0.5,1))
    pro_click(el)

    # блок срабатывает, если Гугл просит подтверждения аккаунта
    t = 0
    while t < 3: # ждем, не прогрузился ли следующий сайт
        if 'https://stackoverflow.com/' in driver.current_url:
            print(f'{login} - вход выполнен!')
            break
        t += 1
        sleep(1)

    if t >= 3:
        try:
            # нажать кнопку подтвердить по почте
            el = '//ul/li[1]/div'
            el = finder.element_by_xpath(el, 5)
            pro_click(el)
            # отправка почты
            el = '//*[@id="knowledge-preregistered-email-response"]'
            el = finder.element_by_xpath(el, 5)
            el.send_keys(verification_email) # почта для подтверждения
            el = '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button'
            el = finder.element_by_xpath(el, 5)
            pro_click(el)
            print(f'{login} - вход выполнен!')
        except:
            print(f'{login} - ошибка входа!')
        
def yt_like(finder):
    # like button
    el = '//ytm-slim-video-metadata-renderer/div[2]/c3-material-button[1]/button'
    el = finder.element_by_xpath(el)
    try:
        pro_click(el)
    except:
        pass
    sleep(random.uniform(1,2))

def yt_subscribe(finder):
    # subscribe button
    el = '//ytm-subscribe-button-renderer/div/c3-material-button/button'
    el = finder.element_by_xpath(el)
    try:
        pro_click(el)
    except:
        pass
    sleep(random.uniform(1,2))

def yt_exit_account(finder):
    driver = finder.driver
    # перейти на меню аккаунта
    driver.get('https://m.youtube.com/logout')
    # # открыть выход
    # el = '//ytm-active-account-header-renderer/div[1]/div/div[1]'
    # el = finder.element_by_xpath(el)
    # el.click()
    # # выйти
    # el = 