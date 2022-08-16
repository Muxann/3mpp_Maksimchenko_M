import vk_api
import time
import codecs
import random



def captcha_handler(captcha):
    key = input("Enter Captcha {0}: ".format(captcha.get_url())).strip()
    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)


if __name__ == '__main__':
   
    vk_session = vk_api.VkApi('+79640163414', 'D67b49Ef4D', captcha_handler=captcha_handler)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)

    vk = vk_session.get_api()

    # Пишем возраст от и до людей которых надо спарсить
    age = 43
    age_max = 43

    # birth_day вызов дня рождения
    # Номер города
    city_number = 1
    # 1 - девушки, 2 - парни
    gender = 1


    # Открываем файл для записи результатов
    ff = codecs.open('ids.txt', 'w', encoding='utf8')

    # Перебор возрастов
    while age <= age_max:
        month = 2
        day = 4
        # Перебор месяцев рождения
        while month <= 12:
            # Пауза для API
            time.sleep(1)
            # Пишем какую группу людей качаем
            print('Download ID: ' + str(age) + ' age, born in ' + str(month) + ' ' + str(day))
            # Получаем 1000 юзеров - их ФИО, айди, и фотку
            z = vk.users.search(count=1000,
                                fields='id, photo_max_orig, has_photo, '
                                       'first_name, last_name',
                                city=city_number,
                                age_from=age,
                                age_to=age,
                                birth_month=month,
                                birth_day=day,
                                sex=gender)
            day = day + 1
            if day > 31:
                month = month + 1
                day = 1
            print('Peoples count: ' + str(z['count']))
            for x in z['items']:
                if x['has_photo'] == 1:
                    # Записываем данные о юзере в файл разделяя черточкой |
                    try:
                        s = str(x['id']) + '|' + str(x['photo_max_orig']) + '|' + str(
                            x['first_name']) + ' ' + str(x['last_name']) + '\n'
                        ff.write(s)
                    except:
                        print("Error! No photo available.")    
        age = age + 1

    ff.close()
    print('Done!')
