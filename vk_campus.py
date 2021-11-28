import vk_botting
import datetime
import analys
import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import json
import sys
from request import TestUsersRequests as req

sys.stdout.encoding 

check_form = {}
сheck_tag  = {}
check_user = {}
check_password = {}
multichet = {}
name_wait = {}
check_data = {}
check_time ={}
check_name = {}
check_contant= {}
check_tags = {}
make_comment = {}
new_password = {}
check_user_new ={}
user_name ={}
i = 1
first_time = {}
vk_uid = {}
bot = vk_botting.Bot('/')
token = 'f9cfd2b114457b41a8a35449cd562ee77737590ff068d436155e2e95de41e1bd3edcf07ccb6e9bf0946d3'
vk_session = VkApi(token=token)
#longPoll = VkBotLongPoll(vkBotSession, groupId)

vk = vk_session.get_api()
#Представляет собой бота ВК. 
#'/pr' - Префикс команды - это то, с чего должно начинаться сообщение, чтобы бот распознал его как команду
bot.case_insensitive = True
# case_insensitive - нечуствительной к регистру.
bot.force = True
#force - втоматически устанавливать оптимальные настройки LongPoll
#bot.add_command('Привествие')

@bot.listen()
async def on_ready():
    global first_time
    print(f'Logged in as {bot.group.name}')
    vk_uid  = req.get_user_add('vk_uid')
    for w in vk_uid:
        if (w=='None'):
            print(w)
        else: 
            first_time[w] = 1 
    #Имя группы, к которой я на данный момент имею доступ через бота
  
#демо фукция 
#@bot.listen()
#async def on_message_new(message):
    #if message.text.startswith('Дата'):
        #await message.send(datetime.datetime.now())

def next(j):
    print('next name')
    text_path  = f'.\\model data\\{j}.txt'
    image_path = f'.\\model data\\{j}.png'
    print(text_path)
    print(image_path )
    j = j + 1
    if (j > 3): j = 1
    print(j)
    return text_path, image_path, j

def find(name):
    print('some')

#начало диалога 
@bot.listen()
async def on_conversation_start(message):
    global check_form, сheck_tag, check_user, check_password, name_wait, check_data, check_name, check_time, check_contant, check_tags
    global make_comment, check_user_new,new_password
    img = await bot.upload_photo(message.peer_id, filename= 'hello.jpg')
    with open('Hello_world.json') as f:
        d = json.load(f)
    await bot.send_message(peer_id = message.from_id, message =f'Привет, я бот Эковектора!'
                         f'\nЧем могу помочь?',keyboard = d, attachment = img)
    make_comment[message.from_id] = 0
    check_form[f'{message.from_id}'] = 0
    сheck_tag[f'{message.from_id}'] = 0
    check_user[f'{message.from_id}'] = 0
    check_password[f'{message.from_id}'] = 0
    multichet[f'{message.from_id}'] = 0
    name_wait[f'{message.from_id}'] = 0
    check_data[f'{message.from_id}'] = 0
    check_name[f'{message.from_id}'] = 0
    check_time[f'{message.from_id}'] = 0
    check_contant[f'{message.from_id}'] = 0
    check_tags[f'{message.from_id}'] = 0
    check_user_new[f'{message.from_id}'] = 0
    new_password[f'{message.from_id}']  = 0
    user_name[f'{message.from_id}']  = '' 
    #print(dir(message)) #смотрел все Атрибуты класса message

#получение ID пользователя и прочих данных
@bot.listen()
async def on_message_new(message):
    global check_form, сheck_tag, check_user, check_password, name_wait, check_data, check_name, check_time, check_contant, check_tags
    global make_comment, first_time, new_password, user_name
    global check_user_new
  
    if message.text =='Начать':
      img = await bot.upload_photo(message.peer_id, filename= 'hello.jpg')
      with open('Hello_world.json') as f:
           d = json.load(f)
      await bot.send_message(peer_id = message.from_id, message =f'Привет, я бот Эковектора!'
                         f'\nЧем могу помочь?',keyboard = d, attachment = img)

      check_form[f'{message.from_id}'] = 0
      сheck_tag[f'{message.from_id}'] = 0
      check_user[f'{message.from_id}'] = 0
      check_password[f'{message.from_id}'] = 0
      multichet[f'{message.from_id}'] = 0
      name_wait[f'{message.from_id}'] = 0
      check_data[f'{message.from_id}'] = 0
      check_name[f'{message.from_id}'] = 0
      check_time[f'{message.from_id}'] = 0
      check_contant[f'{message.from_id}'] = 0
      check_tags[f'{message.from_id}'] = 0
      make_comment[f'{message.from_id}'] = 0
      check_user_new[f'{message.from_id}'] = 0

    try:
        if (first_time[f'{message.from_id}'] == 0):
            print('я тебя знаю')
    except:
       
         check_form[f'{message.from_id}'] = 0
         сheck_tag[f'{message.from_id}'] = 0
         check_user[f'{message.from_id}'] = 0
         check_password[f'{message.from_id}'] = 0
         multichet[f'{message.from_id}'] = 0
         name_wait[f'{message.from_id}'] = 0
         check_data[f'{message.from_id}'] = 0
         check_name[f'{message.from_id}'] = 0
         check_time[f'{message.from_id}'] = 0
         check_contant[f'{message.from_id}'] = 0
         check_tags[f'{message.from_id}'] = 0
         make_comment[f'{message.from_id}'] = 0
         first_time[f'{message.from_id}']  = 0
         print(first_time[f'{message.from_id}'])
         new_password[f'{message.from_id}']  = 0
         check_user_new[f'{message.from_id}'] = 0

    if message.text =='Баланс':
        list = get_user_subs()
        print(list)

    if message.text =='Мои комментарии':
        list = get_user_subs()
        print(list)

    if (first_time[f'{message.from_id}'] == 0):
        

        if (check_form[f'{message.from_id}'] == 0):
          if (analys.Analys.Filter_rude_words(message.text)):
                await bot.send_message(peer_id = message.from_id, message ='Ведите себя прилично!')
        else:
            text = message.text
            image  = message.attachment
            print(dict(message.attachment))
            print(image)
            print(text)
            
        if ( сheck_tag[f'{message.from_id}'] == 0):
            print('')
        with open('Hello_world.json') as f:
            d = json.load(f)
            print(message.from_id)
            make_comment[f'{message.from_id}'] = 0
        print('dijdhigbhicfnihobfciohn')
        print(check_user[f'{message.from_id}'])


        if (check_password[f'{message.from_id}'] == 1): #получение пароля
            password = message.text
            print('check_password')
            check_password[f'{message.from_id}'] = 0
            await bot.send_message(peer_id = message.from_id, message ='Верификация прошла успешно!')
            with open('Events.json') as f:
               d = json.load(f)
            img = await bot.upload_photo(peer_id = message.from_id, filename= 'team.png') 
            await bot.send_message(peer_id = message.from_id, message ='Комманда тебя ждёт!',keyboard = d, attachment = img)
        
        if (new_password[f'{message.from_id}'] == 1): #получение нового
            print('new_password')
            password = message.text
            user = user_name[f'{message.from_id}']
            id = req.get_user_add_num() + 1
            print(id)
            req.post_user_add(id, message.from_id, user, password)
            new_password[f'{message.from_id}'] = 0
            await bot.send_message(peer_id = message.from_id, message ='Данные записаны!')
            with open('Events.json') as f:
               d = json.load(f)
            img = await bot.upload_photo(peer_id = message.from_id, filename= 'team.png') 
            await bot.send_message(peer_id = message.from_id, message ='Комманда тебя ждёт!',keyboard = d, attachment = img)




        if (check_user[f'{message.from_id}'] == 1):
           print('check_user')
           user_name[f'{message.from_id}']  = message.text  
           username = message.text
           vk_uid = message.from_id
           check_user[f'{message.from_id}'] = 0


           await bot.send_message(peer_id = message.from_id, message ='Введи пароль записи')
           new_password[f'{message.from_id}'] = 1


        if (name_wait[f'{message.from_id}'] == 1): #Пользователь решает, что он будет делать 
            if message.text.startswith('1'):
                name_wait[f'{message.from_id}'] = 0
                text_path, image_path, i = next(i)
                img = await bot.upload_photo(message.from_id, filename= image_path) 
                str = open(text_path, 'r', encoding='utf-8').read()
                with open('Events_menu.json') as f:
                    d = json.load(f)
                await bot.send_message(peer_id = message.from_id, message =  str, attachment = img, keyboard = d)
            else: 
                  find(message.text)

        if (check_tags[f'{message.from_id}'] == 1):
            check_tags[f'{message.from_id}'] = 0
            await bot.send_message(peer_id = message.from_id, message ='Поздравляю вы создали мерпориятие!')
            with open('Events.json') as f:
               d = json.load(f)
            img = await bot.upload_photo(peer_id = message.from_id, filename= 'team.png') 
            await bot.send_message(peer_id = message.from_id, message ='Комманда тебя ждёт!',keyboard = d, attachment = img)


        if (check_contant[f'{message.from_id}'] == 1):
            check_tags[f'{message.from_id}'] = 1
            check_contant[f'{message.from_id}'] = 0
            description = message.text
            await bot.send_message(peer_id = message.from_id, message ='Напишите теги из списка')
            str = open('tags.txt', 'r', encoding='utf-8').read()
            await bot.send_message(peer_id = message.from_id, message = str)
            f.close

        if (check_data[f'{message.from_id}'] == 1):
           check_data[f'{message.from_id}'] = 0 
           check_contant[f'{message.from_id}']= 1
           data = message.text
           await bot.send_message(peer_id = message.from_id, message ='Введите краткое описание мероприятия')

        if (check_time[f'{message.from_id}'] == 1):
            check_time[f'{message.from_id}'] = 0 
            time = message.text
            check_data[f'{message.from_id}'] = 1
            await bot.send_message(peer_id = message.from_id, message ='Введите время мероприятия')

        if (check_name[f'{message.from_id}'] ==1): 
           name = message.text
           check_name[f'{message.from_id}'] = 0
           check_time[f'{message.from_id}'] =1
           await bot.send_message(peer_id = message.from_id, message ='Дату в формате дд.мм.гг')

        if  (make_comment[f'{message.from_id}'] == 1):
            comment = message.text
            make_comment[f'{message.from_id}'] = 0
            await bot.send_message(peer_id = message.from_id, message ='Ваш комментарий принят!')
            if (analys.Analys.Filter_rude_words(message.text)):
                await bot.send_message(peer_id = message.from_id, message ='Ведите себя прилично!')

        if (check_user[f'{message.from_id}'] == 2): #получение имени пользователя
           print('check_user_new')
           user_name[f'{message.from_id}']  = message.text
           username = message.text
           vk_uid = message.from_id   
           print('username')
           u = req.get_user_name(username)
           print(u)
           if (u):
               check_user[f'{message.from_id}'] = 0
               await bot.send_message(peer_id = message.from_id, message ='Введи пароль записи')
               new_password[f'{message.from_id}'] = 1         
           else:
               await bot.send_message(peer_id = message.from_id, message ='Такого пользователя не существует')
       
       
        



@bot.listen()
async def on_message_event(event):
        global i
        global check_form, сheck_tag, check_user, check_password,check_user_new
        global check_data, check_name, check_time, check_contant, check_tags
        global make_comment
        global first_time, new_password, user_name
        print(event.payload)
        consume = event.payload

        if consume == '{"button": "1"}':
            event.user_id
            img = await bot.upload_photo(event.user_id, filename= 'eco_hum.jpg')
            try:                 
                if (first_time[event.user_id] == 1):
                    with open('Tags_menu.json') as f:
                        d = json.load(f)
                    await bot.send_message(peer_id = event.user_id, message ='Введите название мероприятия')
                    check_name[f'{event.user_id}'] = 1
            except:
                with open('Registr.json') as f:
                    d = json.load(f)

                await bot.send_message(peer_id = event.user_id, message ='Ты здесь впервые?',keyboard = d, attachment = img)

        if consume == '{"button": "2"}':
            await bot.send_message(peer_id = event.user_id, message =f'Меня создали на Miigaik GeoHack 2021!'
                                   f'\nЧем могу помочь?')

        if consume == '{"button": "3"}':
            with open('Tags_menu.json') as f:
                d = json.load(f)
            await bot.send_message(peer_id = event.user_id, message ='Введите название мероприятия')
            check_name[f'{event.user_id}'] = 1


        if consume == '{"button": "4"}':

             str = open('names.txt', 'r', encoding='utf-8').read()
             with open('lenta.json') as f:
                d = json.load(f)
             name_wait[f'{event.user_id}'] = 1
             await bot.send_message(peer_id = event.user_id, message =  str)
             await bot.send_message(peer_id = event.user_id, message = 'Что дальше?',keyboard = d)



        if consume == '{"button": "6"}':
            with open('Events.json') as f:
                d = json.load(f)
            await bot.send_message(peer_id = event.user_id, message ='Добавьте теги',keyboard = d)
            check_form[f'{event.user_id}'] = 0

        if consume == '{"button": "7"}':
            tags_list = []
     #       await bot.send_message(peer_id = event.user_id, message ='Cписок тегов',keyboard = d)

        if consume == '{"button": "8"}':
            await bot.send_message(peer_id = event.user_id, message ='Введите новый тег',keyboard = d)
            check_tag[f'{event.user_id}'] = 1

        if consume == '{"button": "9"}':  #пойду на мероприятие
            text_path, image_path, i = next(i)
            img = await bot.upload_photo(event.user_id, filename= image_path) 
            str = open(text_path, 'r', encoding='utf-8').read()
            with open('Events_menu.json') as f:
                d = json.load(f)
            await bot.send_message(peer_id = event.user_id, message =  str, attachment = img, keyboard = d)


        if consume == '{"button": "11"}':   #cледующее
            text_path, image_path, i = next(i)
            img = await bot.upload_photo(event.user_id, filename= image_path) 
            str = open(text_path, 'r', encoding='utf-8').read()
            with open('Events_menu.json') as f:
                d = json.load(f)
            await bot.send_message(peer_id = event.user_id, message =  str, attachment = img,keyboard = d)

        if consume == '{"button": "12"}': #вернуться в главное меню
            with open('Hello_world.json') as f:
                d = json.load(f)
            await bot.send_message(peer_id = event.user_id, message ='Стартовое меню',keyboard = d)

        if consume == '{"button": "13"}': #регистрация в системе
            await bot.send_message(peer_id = event.user_id, message ='Давай знакомиться! (Введи имя пользователя)')
            check_user[f'{event.user_id}'] = 1
            print(check_user[f'{event.user_id}'])

        if consume == '{"button": "14"}': #я уже пользователь
            await bot.send_message(peer_id = event.user_id, message ='Введи имя пользователя')
            check_user[f'{event.user_id}'] = 2
            print('check_user_new')
           

        if consume == '{"button": "15"}': #отмена
          img = await bot.upload_photo(event.user_id, filename= 'hello.jpg')
          with open('Hello_world.json') as f:
              d = json.load(f)
          await bot.send_message(peer_id = event.user_id, message ='Привет, я бот Эковектора!',keyboard = d, attachment = img)

        if consume == '{"button": "16"}': #Планирую посетить
          img = await bot.upload_photo(event.user_id, filename= 'hello.jpg')
          text_path, image_path, i = next(i)
          img = await bot.upload_photo(event.user_id, filename= image_path) 
          str = open(text_path, 'r', encoding='utf-8').read()
          with open('Events_menu.json') as f:
                d = json.load(f)
          await bot.send_message(peer_id = event.user_id, message =  str, attachment = img,keyboard = d)

        if consume == '{"button": "17"}': #Не интересует
          img = await bot.upload_photo(event.user_id, filename= 'hello.jpg')
          text_path, image_path, i = next(i)
          img = await bot.upload_photo(event.user_id, filename= image_path) 
          str = open(text_path, 'r', encoding='utf-8').read()
          with open('Events_menu.json') as f:
                d = json.load(f)
          await bot.send_message(peer_id = event.user_id, message =  str, attachment = img,keyboard = d)

        if consume == '{"button": "18"}': #1
          await bot.send_message(peer_id = event.user_id, message ='Поставлена оценка 1 балл')
          rating = 1
          img = await bot.upload_photo(event.user_id, filename= 'hello.jpg')
          i = i - 1
          text_path, image_path, i = next(i)
          img = await bot.upload_photo(event.user_id, filename= image_path) 
          str = open(text_path, 'r', encoding='utf-8').read()
          with open('Events_menu.json') as f:
                d = json.load(f)
          await bot.send_message(peer_id = event.user_id, message =  str, attachment = img,keyboard = d)

        if consume == '{"button": "19"}': #2 балл
          await bot.send_message(peer_id = event.user_id, message ='Поставлена оценка 2 балла')
          rating = 2
          img = await bot.upload_photo(event.user_id, filename= 'hello.jpg')
          i = i - 1
          text_path, image_path, i = next(i)
          img = await bot.upload_photo(event.user_id, filename= image_path) 
          str = open(text_path, 'r', encoding='utf-8').read()
          with open('Events_menu.json') as f:
                d = json.load(f)
          await bot.send_message(peer_id = event.user_id, message =  str, attachment = img,keyboard = d)

        if consume == '{"button": "20"}': #3 балла
          await bot.send_message(peer_id = event.user_id, message ='Поставлена оценка 3 балла')
          rating = 3
          img = await bot.upload_photo(event.user_id, filename= 'hello.jpg')
          i = i - 1
          text_path, image_path, i = next(i)
          img = await bot.upload_photo(event.user_id, filename= image_path) 
          str = open(text_path, 'r', encoding='utf-8').read()
          with open('Events_menu.json') as f:
                d = json.load(f)
          await bot.send_message(peer_id = event.user_id, message =  str, attachment = img,keyboard = d)

        if consume == '{"button": "21"}': #4 балла
          await bot.send_message(peer_id = event.user_id, message ='Поставлена оценка 4 балла')
          rating = 4
          img = await bot.upload_photo(event.user_id, filename= 'hello.jpg')
          i = i - 1
          text_path, image_path, i = next(i)
          img = await bot.upload_photo(event.user_id, filename= image_path) 
          str = open(text_path, 'r', encoding='utf-8').read()
          with open('Events_menu.json') as f:
                d = json.load(f)
          await bot.send_message(peer_id = event.user_id, message =  str, attachment = img,keyboard = d)

        if consume == '{"button": "22"}': #5 балла
          await bot.send_message(peer_id = event.user_id, message ='Поставлена оценка 5 балла')
          img = await bot.upload_photo(event.user_id, filename= 'hello.jpg')
          i = i - 1
          text_path, image_path, i = next(i)
          img = await bot.upload_photo(event.user_id, filename= image_path) 
          str = open(text_path, 'r', encoding='utf-8').read()
          with open('Events_menu.json') as f:
                d = json.load(f)
          await bot.send_message(peer_id = event.user_id, message =  str, attachment = img,keyboard = d)

        if consume == '{"button": "23"}': #отмена
          img = await bot.upload_photo(event.user_id, filename= 'hello.jpg')
          i = i - 1
          text_path, image_path, i = next(i)
          img = await bot.upload_photo(event.user_id, filename= image_path) 
          str = open(text_path, 'r', encoding='utf-8').read()
          with open('Events_menu.json') as f:
                d = json.load(f)
          await bot.send_message(peer_id = event.user_id, message =  str, attachment = img,keyboard = d)

        if consume == '{"button": "28"}': #отмена
           img = await bot.upload_photo(event.user_id, filename= 'team.png')
           with open('Events.json') as f:
               d = json.load(f)
           await bot.send_message(peer_id =  event.user_id, message ='Комманда тебя ждёт!',keyboard = d, attachment = img)

        if consume == '{"button": "30"}': #Оценить
           with open('Like.json') as f:
               d = json.load(f)
           await bot.send_message(peer_id =  event.user_id, message ='Каков ваш вердикт?',keyboard = d)

        if consume == '{"button": "31"}': #лента
          img = await bot.upload_photo(event.user_id, filename= 'hello.jpg')
          text_path, image_path, i = next(i)
          img = await bot.upload_photo(event.user_id, filename= image_path) 
          str = open(text_path, 'r', encoding='utf-8').read()
          with open('Events_menu.json') as f:
                d = json.load(f)
          await bot.send_message(peer_id = event.user_id, message =  str, attachment = img,keyboard = d)

        if consume == '{"button": "32"}': #Оценить
           await bot.send_message(peer_id = event.user_id, message =  'Не реализовано')

        if consume == '{"button": "33"}': #Оставить комментарий
           await bot.send_message(peer_id = event.user_id, message =  'Оставить комментарий?')
           print(event.user_id)
           make_comment[f'{event.user_id}'] = 1


@bot.listen()
async def on_wall_post_new(post):
    print(post.text) #Текст поста
    print(post.id)  #ID Поста
    print(dir(post)) #смотрел все Атрибуты класса comment
   

#Вызывается, когда на стену добавляется новый комментарий
@bot.listen()
async def on_wall_reply_new(comment):
    print(comment) 
    print(comment.from_id) #Id пользователя написавшего комментарий
    print(comment.text) #Содержание комментария
    print(comment.id) #ID комментария
    print(comment.post_id) #ID поста 
    print(dir(comment)) #смотрел все Атрибуты класса comment
    owner_id = bot.group.id
    comment_id= comment.id
    comment.reply_to_user
    if (analys.Analys.Filter_rude_words(comment.text)): #проверка на мат. сейчас проверяет на слово дикая и выдрочка
         owner_id = bot.group.id
         comment_id= comment.id
         comment.reply_to_user
         print(bot.group.id)
         print(comment.id)
         try:
             await bot.send_message(peer_id = comment.from_id, message ='Хулиган!')
      #   vk.wall.DeleteComment(-owner_id,comment_id) #Пока кая-то херня. не удаляетс, но детектится
         except: 
            print('У нас завёлся хулиган'&comment.from_id)
    if (comment.text =='Хочу предсказание'):
        post_id = comment.post_id 
        await bot.send_message(peer_id = comment.from_id, message ='Мы в тебя верим!')


#async def is_owner(ctx):
   # return ctx.author == 191228910

#@bot.command(name='www')
#@limiters.check(is_owner)
#async def _eval(ctx, *, code):
    """A bad example of an eval command"""
   # await ctx.send(eval(code))

#@secretdata.error
#async def secretdata_error(ctx, error):
   # if isinstance(error, exceptions.CheckFailure):
       # await ctx.send('nothing to see here comrade.')

bot.run('fb9871cf3cd1bef91cd5712e05889970b6994bf34069ad595953418a31c386d7afa855761d3a34dd6f188')
#ключ для подключения 