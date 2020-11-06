from lib import *
from finder import Finder

driver = driver_start()
finder = Finder(driver)

video_link = 'https://www.youtube.com/watch?v=a_IA-8nQ4FY'
# video_link = input('Введите ссылку на видео:\t')

accounts = open_accounts() 

print('\nНачало работы\n')

for account in accounts:
    login, password = account.split(':')
    try:
        google_authorization(finder, login, password)
    except:
        print('Ошибка модуля авторизации, проверьте правильность логина и пароля в файле:', account)
        continue

    try:
        driver.get(video_link)

        # лайк и подписка в случайном порядке
        num = random.randint(0,1)

        if num == 0:
            yt_like(finder)
            yt_subscribe(finder)
        if num == 1:
            yt_subscribe(finder)
            yt_like(finder)

        print(f'{login} - выполнено.')

    except:
        print('Ошибка в модулях лайка и подписки')
        continue

