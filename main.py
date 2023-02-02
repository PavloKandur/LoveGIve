import telebot
import time

import random
import sys

#Opening file with comments
f = open("com1111.txt","r")
txt = f.read()
f.close()

#Creating array with comments inside
comAr = txt.split()
#Variable with length of created array
endLen = len(comAr) - 1

#Creating 'real' random values
seed_value = random.randrange(sys.maxsize)
random.seed(seed_value)

#Function that throws message with comment in
def getCom():
    myCom = comAr[random.randint(0,endLen)]
    return myCom


slc = 0

bot = telebot.TeleBot('5842926641:AAF0UWsLR3rwMI_QQM3k2hzlTDXWB5S40TI')

@bot.message_handler(commands=['start'])
def start(message):

    greetings = f'Привіт <b><i>{message.from_user.first_name} {message.from_user.last_name}</i></b>'
    intro = 'Привіт, мене звати <b><i>LoveGive</i></b>, я - бот оповіщувач. Щодня я порційно роздаю своє кохання, щойно ти мене запустиш - усе побачиш. Тобі прийде повідомлення і кожного наступного дня тобі будуть надходити такі повідомлення в ту саму годину коли ти запустиш мене першого разу. \nДля того, щоб я почав працювати надішли мені такі повідомлення: \nStartLove \t\t-\t\t тобі прийде повідомлення, воно прийде наступного дня в той самий час; \nEnd \t\t-\t\t зупинити дію бота.'

    bot.send_message(message.chat.id,greetings,parse_mode='html')
    bot.send_message(message.chat.id,intro,parse_mode='html')


@bot.message_handler()
def startBot(message):
    global slc
    if message.text == 'StartLove':
        slc +=1
        while(True):
            if slc!=1:
                break
            myCom = getCom()
            mess = f'Ти така <b><i>{str(myCom)}</i></b>,тому я тебе і кохаю'
            bot.send_message(message.chat.id,f'{mess} 💞❤💋',parse_mode='html')
            time.sleep(86400.0)
    elif message.text=='End':
        slc-=1
        bot.send_message(message.chat.id,f"Кохання припинено =(. Щоб я знову почав працювати напиши 'StartLove'")
    else:
        ms = 'Я тебе не розумію, спробуй знову'
        bot.send_message(message.chat.id,ms)


bot.polling(non_stop=True)
