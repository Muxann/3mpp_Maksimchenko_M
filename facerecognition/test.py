import vk_api
import time
import codecs


if __name__ == '__main__':
    
    vk_session = vk_api.VkApi('+79197299939', 'D67b49Ef4D')
    vk_session.auth()
    vk = vk_session.get_api()

    # Номер города
    city_number = 1

    # Открываем файл для записи результатов
    #ff = codecs.open('test.txt', 'w', encoding='utf8')

    time.sleep(2)
    # Пишем какую группу людей качаем
    #print('Download ID: ' + str(age) + ' age, born in ' + str(month))
    # Получаем 1000 юзеров - их ФИО, айди, и фотку
    z = vk.users.search(count=1000,
                        fields='id, photo_max_orig, has_photo, '
                                       'first_name, last_name',
                        city=city_number,
                                #age_from=14,
                                #age_to=14,
                        birth_month=11,
			birth_day=17,
			sex=5,
			birth_year=1902
			)
		             
    print('Peoples count: ' + str(z['count']))
    for x in z['items']:        
     #  if x['has_photo'] == 1:
          # Записываем данные о юзере в файл разделяя черточкой |
          #s = str(x['id'])+'\n'# + '|' + str(x['photo_max_orig']) + '|' + 
                  #str(x['first_name']) + ' ' + str(x['last_name']) + '\n'
          #ff.write(s)
         print('id='+str(x['id'])+'\t'+x['first_name']+' '+x['last_name'])

    #ff.close()
    print('Done!')
