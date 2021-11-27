import vk_botting
import datetime
import analys
import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


bot = vk_botting.Bot('/')
token = 'fb9871cf3cd1bef91cd5712e05889970b6994bf34069ad595953418a31c386d7afa855761d3a34dd6f188'
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
    print(f'Logged in as {bot.group.name}')
    #Имя группы, к которой я на данный момент имею доступ через бота
  
#демо фукция 
#@bot.listen()
#async def on_message_new(message):
    #if message.text.startswith('Дата'):
        #await message.send(datetime.datetime.now())


#Приветсвие бота
@bot.command(name='Привет')
async def greet(context):
    await context.reply('Вас привествует система Активный кампус!')

#начало диалога 
@bot.listen()
async def on_conversation_start(message):
    img = await bot.upload_photo(message.peer_id, filename= 'D:\\vk_bot\\PythonApplication1\\hello.jpg')
    await message.send(message = 'Вас привествует система Активный кампус!', attachment = img)
    #print(dir(message)) #смотрел все Атрибуты класса message

#получение ID пользователя и прочих данных
@bot.listen()
async def on_message_new(message):
    if message.text.startswith('Id'):
        await message.send(message.from_id)

#Вызывается, когда к фото добавляется новый комментарий
@bot.listen() 
async def on_photo_comment_new(comment):
    print(comment) 
    print(message.from_id) #Id пользователя написавшего комментарий
    print(message.text) #Содержание комментария
    print(message.peer_id) #ID поста комментари
    


#Вызывается, когда к видео добавляется новый комментарий
@bot.listen()
async def on_video_comment_new(comment):
    print(comment) 
    print(message.from_id) #Id пользователя написавшего комментарий
    print(message.text) #Содержание комментария
    print(message.peer_id) #ID поста комментари

#Вызывается, когда к обсуждению добавляется новый комментарий
@bot.listen()
async def on_board_post_new(comment):
    print(comment) 
    print(message.from_id) #Id пользователя написавшего комментарий
    print(message.text) #Содержание комментария
    print(message.peer_id) #ID поста комментария


@bot.listen()
async def on_wall_post_new(post):
    print(post.text) #Текст поста
    print(post.id)  #ID Поста
    print(dir(post)) #смотрел все Атрибуты класса comment
   
#Вызывается, когда пост со стены репостится
@bot.listen()
async def on_wall_repost(post):
    print(post.text) #Текст поста
    print(post.id)  #ID Поста
    print(post.from_id) #Кем репоститься
 

#Вызывается, когда на стену добавляется новый комментарий
@bot.listen()
async def on_wall_reply_new(comment):
    print(comment) 
    print(comment.from_id) #Id пользователя написавшего комментарий
    print(comment.text) #Содержание комментария
    print(comment.id) #ID комментария
    print(comment.post_id) #ID поста 
    print(dir(comment)) #смотрел все Атрибуты класса comment
    if (analys.Analys.Filter_rude_words(comment.text)): #проверка на мат. сейчас проверяет на слово дикая и выдрочка
         owner_id = bot.group.id
         comment_id= comment.id
         vk.wall.DeleteComment(-owner_id,comment_id) #Пока кая-то херня. не удаляетс, но детектится

#Вызывается, когда пользователь присоединяется к группе
@bot.listen()
async def  on_group_join(user, join_type):
    print(user.id) #запись uid в БД
    print(user.first_name) #запись first_name в БД
    print(user.last_name) #запись last_name в БД
    print(user.sex)  #запись пола в БД   
    print(join_type)

#Вызывается, когда в опросе появляется новый голос
@bot.listen()
async def  on_poll_vote_new(vote):
    print(vote.id)

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