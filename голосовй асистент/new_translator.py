#
# FIO = input('введите ФОИ через пробел: ')
# date = input('введите дд,мм,гг пример: 22,12,2002) ')
# height = int(input('введите ваш рос '))
# wess = int(input('ваш вес '))
# FIO_s = FIO.split()
# date_s = date.split(',')
# # print('ваше ФОИ', FIO)
# massa_tela = round(wess / ((height / 100) ** 2), 2)
# # print(f'у вас масса тела равна: {massa_tela}')
#
# if massa_tela <= 16:
#     massa_tela_text = ('У вас выраженный дефицит массы тела')
# elif massa_tela > 16 and massa_tela <= 18.5:
#     massa_tela_text = ('У вас недостаточная (дефицит) масса тела')
# elif massa_tela > 18.5 and massa_tela <= 24.99:
#     massa_tela_text = ('у вас норма')
# elif massa_tela > 25 and massa_tela <= 30:
#     massa_tela_text = ('У вас избыточная масса тела')
# elif massa_tela > 30 and massa_tela <= 35:
#     massa_tela_text = ('У вас ожирение')
# elif massa_tela > 35 and massa_tela <= 40:
#     massa_tela_text = ('У вас ожирение резкое')
# elif massa_tela > 40:
#     massa_tela_text = ('У вас очень ожирение резкое')
#
# tab = """
# =========================================================
# |16 и менее     Выраженный дефицит массы тела           |
# |16—18,5     Недостаточная (дефицит) масса тела         |
# |18,5—24,99     Норма                                   |
# |25—30             Избыточная масса тела (предожирение) |
# |30—35             Ожирение                             |
# |35—40             Ожирение резкое                      |
# |40 и более     Очень резкое ожирение                   |
# =========================================================
# """
# # print(tab)
#
# # print('ваше дата рdождения', date)
# date_numbers = int(date_s[0])
# date_month = date_s[1]
#
# if (date_numbers >= 22 and date_month == '12') or (date_numbers <= 20 and date_month == '1'):
#     zodiac = ('козерог')
# elif (date_numbers >= 21 and date_month == '1') or (date_numbers <= 19 and date_month == '2'):
#     zodiac = ('водолей')
# elif (date_numbers >= 20 and date_month == '2') or (date_numbers <= 20 and date_month == '3'):
#     zodiac = ('рыба')
# elif (date_numbers >= 21 and date_month == '3') or (date_numbers <= 20 and date_month == '4'):
#     zodiac = ('овен')
# elif (date_numbers >= 21 and date_month == '4') or (date_numbers <= 21 and date_month == '5'):
#     zodiac = ('телец')
# elif (date_numbers >= 22 and date_month == '5') or (date_numbers <= 21 and date_month == '6'):
#     zodiac = ('близнецы')
# elif (date_numbers >= 22 and date_month == '6') or (date_numbers <= 23 and date_month == '7'):
#     zodiac = ('рак')
# elif (date_numbers >= 24 and date_month == '7') or (date_numbers <= 23 and date_month == '8'):
#     zodiac = ('лев')
# elif (date_numbers >= 24 and date_month == '8') or (date_numbers <= 23 and date_month == '9'):
#     zodiac = ('дева')
# elif (date_numbers >= 24 and date_month == '9') or (date_numbers <= 23 and date_month == '10'):
#     zodiac = ('весы')
# elif (date_numbers >= 24 and date_month == '10') or (date_numbers <= 23 and date_month == '11'):
#     zodiac = ('скорпион')
# elif (date_numbers >= 23 and date_month == '11') or (date_numbers <= 21 and date_month == '12'):
#     zodiac = ('телец')
#
# gor = {
#     0: 'Крыса',
#     1: 'Бык',
#     2: 'Тигр',
#     3: 'Кролик',
#     4: 'Дракон',
#     5: 'Змея',
#     6: 'Лошадь',
#     7: 'Коза',
#     8: 'Обезьяна',
#     9: 'Петух',
#     10: 'Собака',
#     11: 'Свинья',
# }
# china_zodiac = gor[(int(date_s[2]) - 2008) % 12]
#
# tab = f"""
# ===========================================================
# Пользователь: {FIO_s[1]}
# ===========================================================
# |                                                         |
# | ФИО: {FIO}                                              |
# | Дата рождения: {date}                                   |
# | Ваш рост: {height}                                      |
# | Ваш вес: {wess}                                         |
# |                                                         |
# ===========================================================
# | ваша масса тела равна: {massa_tela} {massa_tela_text}    |
# |                                                         |
# | 16 и менее     Выраженный дефицит массы тела            |
# | 16—18,5     Недостаточная (дефицит) масса тела          |
# | 18,5—24,99     Норма                                    |
# | 25—30             Избыточная масса тела (предожирение)  |
# | 30—35             Ожирение                              |
# | 35—40             Ожирение резкое                       |
# | 40 и более     Очень резкое ожирение                    |
# ===========================================================
# |                                                         |
# | Ваш знак зодиака: {zodiac}                              |
# | Ваш знак зодиака по китайскому гороскопу: {china_zodiac}|
# ===========================================================
# """
# print(tab)
# with open(f'index.txt', 'w') as file:
#     file.write(tab)
# #
#
# tabimport time70


# def countdown(time_sec):
#     while time_sec:
#         mins, sec = divmod(time_sec, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, sec)
#         print(timeformat)
#         time.sleep(1)
#         time_sec -= 1
#     print('stop')
#
#
# def times(timer):
#     minute = 0
#     second = 0
#     hour = 0
#     while True:
#         if second > 59:
#             minute += 1
#             second = 0
#         if minute > 59:
#             hour += 1
#             minute = 0
#         if timer < 1:
#             break
#         second += 1
#         timer -= 1
#         print(f'{hour}:{minute}:{second}')
#         time.sleep(1)
#
#
# # times(20)
#
# countdown(5)


mass = []

for i in range(3):
    a = []
    for j in range(3):
        a.append(int(input()))
    mass.append(a)

print(max(mass[0]))
print(max(mass[2]))

import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3 as p
from datetime import datetime
import time
import datetime
import random

# Создаем лог
chat_log = [['SESSION_ID', 'DATE', 'AUTHOR', 'TEXT', 'AUDIO_NUM']]
# Узнаем номер сессии
i = 1
exit = 0
while exit == 0:
    session_id = str(i)
    if session_id not in os.listdir():
        os.mkdir(session_id)
        exit = 1
    else:
        i = i + 1
# Первое сообщение пишет bot
author = 'Bot'
text = 'Привет! Чем я могу вам помочь?'


# Добавляем данные к логу с помощью этой процедуры
def log_me(author, text, audio):
    now = datetime.datetime.now()
    i = 1
    exit = 0
    while exit == 0:
        audio_num = str(i) + '.wav'
        if audio_num not in os.listdir(session_id):
            exit = 1
        else:
            i = i + 1
    os.chdir(session_id)
    with open(audio_num, "wb") as file:
        file.write(audio.get_wav_data())
    chat_log.append([now.strftime("%Y-%m-%d %H:%M:%S"), author, text, audio_num])


# Произношение words
engine = pyttsx3.init()


def talk(words):
    engine.say(words)
    engine.runAndWait()



#Настройка микрофона
def command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        #Бот ожидает нашего голоса
        print('Bot: ...')
        #Небольшая задержка в записи
        rec.pause_threshold = 1
        #Удаление фонового шума с записи
        rec.adjust_for_ambient_noise(source, duration=1)
        audio = rec.listen(source)
    try:
        #Распознание теста с помощью сервиса GOOGLE
        text = rec.recognize_google(audio, language="ru-RU").lower()
        #Вывод сказанного текста на экран
        print('Вы:  ' + text[0].upper() + text[1:])
        log_me('User', text, audio)
    #Если не распознался тест из аудио
    except sr.UnknownValueError:
        text = 'Не понимаю. Повторите.'
        print('Bot: ' + text)
        talk(text)
        #Начинаем заново слушать
        text = command()
        log_me('Bot', text, Null)
    return text


def makeSomething(text):
    if 'открой сайт' in text:
        print('Bot: Открываю сайт NewTechAudit.')
        talk('Открываю сайт NewTechAudit.')
        log_me('Bot','Открываю сайт NewTechAudit.', Null)
        webbrowser.open('https://newtechaudit.ru/')


#Повторение фразы пользователя
    elif 'произнеси' in text or 'скажи' in text or 'повтори' in text:
        print('Bot: ' + text[10].upper() + text[11:])
        talk(text[10:])
        log_me('Bot', text[10].upper() + text[11:] , Null)


#Ответ на вопрос как зовут бота
    elif 'своё имя' in text or 'как тебя зовут' in text or 'назови себя' in text:
        print('Bot: Меня зовут Bot.')
        talk('Меня зовут Bot')
        log_me('Bot', 'Меня зовут Bot', Null)

#Определение случайного числа
    elif 'случайное число' in text:
        ot=text.find('от')
        do=text.find('до')
        f_num=int(text[ot+3:do-1])
        l_num=int(text[do+3:])
        r=str(random.randint(f_num, l_num))
        print('Bot: ' + r)
        talk(r)
        log_me('Bot', r, Null)

    elif 'пока' in text or 'до свидания' in text:
        print('Bot: До свидания!')
        talk('До свидания')
        log_me('Bot', 'Конец сессии', Null)
        os.chdir(session_id)
        log_file = open( session_id + ".txt", "w")
        for row in chat_log:
            np.savetxt(log_file, row)
        log_file.close()
        sys.exit()


while True:
    makeSomething(command())