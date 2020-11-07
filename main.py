from lib import *
from finder import Finder

driver = driver_start()
finder = Finder(driver)

#video_link = 'https://www.youtube.com/watch?v=wufXF5YKR1M'
video_link = input('Введите ссылку на видео: ')

verification_email = input('Введите почту для подтверждения аккаунтов: ') # 'janakovbaha@gmail.com'

accounts = open_accounts() 

print('\nНачало работы\n')

for account in accounts:
    login, password = account.split(':')
  
    google_authorization(finder, login, password, verification_email)

    try:
        sleep(2)
        driver.get(video_link)

        # лайк и подписка в случайном порядке
        num = random.randint(0,0)

        if num == 0:
            yt_like(finder)
            yt_subscribe(finder)
        if num == 1:
            yt_subscribe(finder)
            yt_like(finder)

        yt_exit_account(finder)
        print(f'{login} - успешно завершено.')

    except:
        print('Ошибка в модулях лайка и подписки')
        continue

print('\nРабота программы завершена!')
temp = input('Введите <Enter> для выхода . . . ')
