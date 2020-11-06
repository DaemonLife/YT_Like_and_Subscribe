from lib import *
from finder import Finder

driver = driver_start()
finder = Finder(driver)

video_link = 'https://youtube.com/watch?v=lY3g3h0iP3A'
# video_link = input('Введите ссылку на видео:\t')

accounts = open_accounts() 

print('\nНачало работы\n')

for account in accounts:
    login, password = account.split(':')
    # try:
    google_authorization(finder, login, password)
    # except:
    #     print('Ошибка модуля авторизации, проверьте правильность логина и пароля в файле:\n', account)
    #     continue

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
