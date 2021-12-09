import os
import sys
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import webbrowser
import time
from bs4 import BeautifulSoup
import requests

engine = pyttsx3.init()

cmd1 = {'chek_search': ('найди', 'найти', "поищи"),
        'chek_translate': ("перевести", "переведи"),
        'name': ('пятница', 'friday', 'катэрия'),
        'question': ('как', 'где', 'почему', 'что'),
        'search':
            {'yandex': ('найди в яндексе', 'найти в яндек   се', 'поищи в яндексе',
                        'найди в интернете', 'найти в интернете', 'поищи в интернете'),
             'google': ('найди в гугле', 'найти в гугле', 'поищи в гугле'),
             'youtube': ('найди в ютубе', 'найти в ютубе', 'поищи в ютубе',
                         'найди в youtube', 'найти в youtube', 'поищи в youtube'),
             },
        'now_time': ('каторый сейчас час', 'сколько сейчас времени', 'время'),
        # 2 ввод
        "trb_v1": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', "расскрыть", 'в', 'на', 'до'),
        'poisk': {'web': ('найди', 'найти', 'поищи', 'поиск'),
                  'translate': ('переведи', 'перевести')},
        # команды бота
        "cmd": {
            'time': ("сколько вермя", "время", "часы", "который сейчас час", "который час", "сколько часов",),
            'radio': ('включи радео', 'радио'),
            'youtube': ("ютуб", "youtube", 'you tube', 'открыть ютуб', 'открыть youtube', 'открыть you tube'),
            'google': ('google', 'открыть гугл', 'открыть google'),
            'yandex': ("yandex", 'яндекс', 'открыть яндекс', "открыть yandex", 'открой страницу', 'web browser',
                       'открыть брайзер', 'страница'),
            'vk': ('vr', 'вк', 'вконтакте', 'в контакте', 'контакты'),
            'taimer': ('таймер', 'timer'),
            'zodiac': ('какой знак зодиака у меня', 'знак зодиака', 'зодиак', 'задиак', 'знак задиак'),
        }
        }


def speak(what):
    engine.say(what)
    engine.runAndWait()
    engine.stop()


def name(voice_text):
    text = voice_text.split()
    if text[0] in cmd1['name']:
        del text[0]
        chek(ls_text=text, full_text=voice_text)
    else:
        chek(ls_text=text, full_text=voice_text)


counter = 0


def say():
    rec = sr.Recognizer()
    global counter
    if counter == 3:
        counter = 0
        sleep()
    with sr.Microphone(device_index=1) as source:
        rec.pause_threshold = 1
        rec.adjust_for_ambient_noise(source, duration=1)
        audio = rec.listen(source)
    try:
        w_y_s = rec.recognize_google(audio, language="ru-RU").lower()
        print(w_y_s)
        counter = 0
        return w_y_s
    except sr.UnknownValueError:
        print('голон не сраспознан')
        counter += 1
        retur = say()
    return retur


def sleep_say():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        w_y_s = r.recognize_google(audio, language="ru-RU").lower()
        print(w_y_s)
        return w_y_s
    except sr.UnknownValueError:
        print('sleep')
        retur = sleep_say()
    return retur


# сон (если более 3 раз был голос не распознон)
def sleep():
    while True:
        print('sleep')
        chek = sleep_say()
        if chek == 'пятница':
            print(chek)
            break


def recognize_cmd(processed_voice):
    # в cmd будет присваивать адрес команды, percent уровень сравнение комнада должна совпадать на 75 %
    RC = {'cmd': '', 'percent': 75}
    # извлечение адреса команд с и самих команд v
    for c, v in cmd1['search'].items():
        for x in v:
            # сравнение с имеющимися командами и тем что сказал пользователь
            vrt = fuzz.ratio(processed_voice['command'], x)
            if vrt > RC['percent']:
                processed_voice['command'] = c
    return processed_voice


# функция получает текст из функции say и проверяет что нужно сделать найти, перевести...
def chek(ls_text, full_text):
    # Разделяет тест на слова и предлоги, после чего образует из них список
    text_voice = ls_text
    # TODO проверка типа данных
    for i in text_voice:
        print(type(i))
    # Опридиляет нужноли пользователю что-то найти или перевести
    if text_voice[0] in cmd1['chek_search'] or text_voice[0] in cmd1['chek_translate']:
        length = 3
        buffer = separator(text_voice, length)
        # TODO проверка команды
        print(buffer['command'])
        if buffer['command'] in ['переведи на английский ', 'перевести на английский ']:
            buffer['command'] = 'english'
            commands(buffer)
        elif buffer['command'] in ['переведи на русский ', 'перевести на русский ']:
            buffer['command'] = 'russia'
            commands(buffer)
        else:
            cmd_end_textcom = recognize_cmd(buffer)
            commands(cmd_end_textcom)
    # ищет задаваемы вопрос без обращшение
    elif text_voice[0] in cmd1['question']:
        buffer = {'command': '', 'text_command': ''}
        for i in text_voice:
            buffer['text_command'] = buffer['text_command'] + i + ' '
        buffer['command'] = 'question'
        commands(buffer)
    # выход из системы
    elif text_voice[0] in ['пока', 'прощай', 'выход']:
        sys.exit()
    elif '/' in text_voice or 'разделить' in text_voice:
        bb = str(int(text_voice[0]) / int(text_voice[-1]))
        speak(bb)
    elif '*' in text_voice or 'умножить' in text_voice:
        bb = str(int(text_voice[0]) * int(text_voice[-1]))
        speak(bb)
    elif '+' in text_voice or 'плюс' in text_voice:
        bb = str(int(text_voice[0]) + int(text_voice[-1]))
        speak(bb)
    elif '-' in text_voice or 'минус' in text_voice:
        bb = str(int(text_voice[0]) - int(text_voice[-1]))
        speak(bb)
    else:
        command(full_text)


# резделяет команду и тест команды в раздельные списки словаря
def separator(text, length):
    buffer = {'command': '', 'text_command': ''}
    # text = text.split()
    for i in text:
        if length > 0:
            buffer['command'] = buffer['command'] + i + ' '
            length -= 1
        else:
            buffer['text_command'] = buffer['text_command'] + i + ' '
    return buffer


def command(voice):
    # if voice.startswith(cmd1["name"]):
    #     # удоляет имя бота в запросе
    #     for x in cmd1["name"]:
    #         voice = voice.replace(x, '').strip()
    #     # удоляет слова помехи
    #     for x in cmd["trb_v1"]:
    #         voice = voice.replace(x, '').strip()
    #
    #     # нечеткое сравнение со словами командами
    #     voice = recognize_cmd1(voice)
    #     # выполнение команд
    #     execute_cmd(voice)

    # это необходимо если бот не услышал своё имя но команду нужно выполнить
    # else:
    # удаляет имя бота в запросе
    for x in cmd1["name"]:
        voice = voice.replace(x, '').strip()
    # удоляет слова помехи
    for x in cmd1["trb_v1"]:
        voice = voice.replace(x, '').strip()

    # нечеткое сравнение со словами командами
    processed_voice = recognize_cmd1(voice)
    # выполнение команд
    execute_cmd(processed_voice)


# узнает что за команда была задана
def recognize_cmd1(processed_voice):
    # в cmd будет присваивать адрес команды, percent уровень сравнение комнада должна совпадать на 50 %
    RC = {'cmd': '', 'percent': 50}
    # извлечение адреса команд с и самих команд v
    for c, v in cmd1['cmd'].items():
        for x in v:
            vrt = fuzz.ratio(processed_voice, x)  # сравнение с имеющимися командами и тем что сказал пользователь
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC


def zodiac(date):
    date_numbers = int(date[0:2])
    date_month = date[3:]
    if (date_numbers >= 22 and date_month == 'декабря') or (date_numbers <= 20 and date_month == 'января'):
        print('козерог')
    elif (date_numbers >= 21 and date_month == 'января') or (date_numbers <= 19 and date_month == 'февраля'):
        print('водолей')
    elif (date_numbers >= 20 and date_month == 'февраля') or (date_numbers <= 20 and date_month == 'марта'):
        print('рыба')
    elif (date_numbers >= 21 and date_month == 'марта') or (date_numbers <= 20 and date_month == 'апреля'):
        print('овен')
    elif (date_numbers >= 21 and date_month == 'апреля') or (date_numbers <= 21 and date_month == 'мая'):
        print('телец')
    elif (date_numbers >= 22 and date_month == 'мая') or (date_numbers <= 21 and date_month == 'июнь'):
        print('близнецы')
    elif (date_numbers >= 22 and date_month == 'июня') or (date_numbers <= 23 and date_month == 'июля'):
        print('рак')
    elif (date_numbers >= 24 and date_month == 'июля') or (date_numbers <= 23 and date_month == 'августа'):
        print('лев')
    elif (date_numbers >= 24 and date_month == 'августа') or (date_numbers <= 23 and date_month == 'сентября'):
        print('дева')
    elif (date_numbers >= 24 and date_month == 'сентября') or (date_numbers <= 23 and date_month == 'октября'):
        print('весы')
    elif (date_numbers >= 24 and date_month == 'октября') or (date_numbers <= 23 and date_month == 'ноября'):
        print('скорпион')
    elif (date_numbers >= 23 and date_month == 'ноября') or (date_numbers <= 21 and date_month == 'декабря'):
        print('телец')


def timer(minutes):
    while True:
        second = 0
        minute = 0
        hour = 0
        minutes = minutes * 60
        for _ in range(minutes):
            time.sleep(1)
            second += 1
            if second == 60:
                minute += 1
                second = 0
            if minute == 60:
                hour = 1
                minute = 0
        break
    print('hour:', hour, 'minute:', minute, 'second:', second)
    print('время закончилось')


# def now_time():
#     url = 'https://www.google.ru/search?q=время&newwindow=1&sxsrf=ALeKk03-MHBYlhrh1Rzc8EFTmc9yqwbjTw%3A1618758385674&ei=8Up8YJTWKIadrgT06IKYAw&oq=время&gs_lcp=Cgdnd3Mtd2l6EAMyCwgAELEDEIMBEMkDMgUIABCSAzIFCAAQkgMyAggAMgIIADICCAAyAggAMgIIADIFCAAQsQMyAggAOgcIIxDqAhAnOgQIIxAnOgsIABCxAxDHARCjAjoICAAQsQMQgwE6CAguELEDEIMBOg4IABCxAxCDARDHARCjAjoCCC46BAgAEENQ8rgKWNbMCmD00QpoAnACeACAAeYBiAGhCJIBBTAuNi4xmAEAoAEBqgEHZ3dzLXdperABCsABAQ&sclient=gws-wiz&ved=0ahUKEwjUkrj0iIjwAhWGjosKHXS0ADMQ4dUDCA4&uact=5'
#     user = {
#         'Accept': '*/*',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 YaBrowser/21.3.0.663 Yowser/2.5 Safari/537.36'
#     }
#
#     full_page = requests.get(url, headers=user)
#     father = BeautifulSoup(full_page.content, 'html.parser')
#     son = father.findAll('div', {'class': 'gsrt', 'class': 'dDoNo'})
#     son = son[0].text
#     print(son)


def execute_cmd(execution_command):
    # сказать текущее время
    if execution_command['cmd'] == 'time':
        print(execution_command['cmd'])
        now = datetime.datetime.now()
        print("Сейчас " + str(now.hour) + ":" + str(now.minute))
        a = "Сейчас " + str(now.hour) + ":" + str(now.minute)
        speak(a)
    # открывает youtube
    elif execution_command['cmd'] == 'youtube':
        print(execution_command['cmd'])
        webbrowser.open("https://www.youtube.com/")
    # открывает google
    elif execution_command['cmd'] == 'google':
        print(execution_command['cmd'])
        webbrowser.open("https://www.google.ru/")
    # открывает yandex
    elif execution_command['cmd'] == 'yandex':
        print(execution_command['cmd'])
        webbrowser.open("https://yandex.ru/")
    # открывает радио
    elif execution_command['cmd'] == 'radio':
        print(execution_command['cmd'])
        webbrowser.open("https://europaplus.ru/?go=chart40%20")


# поридиляет команду и выполняет ее
def commands(text):
    if text['command'] == 'youtube':
        webbrowser.open('https://www.youtube.com/results?search_query={}'.format(text['text_command']))
    elif text['command'] == "yandex" or text['command'] == 'question':
        webbrowser.open('https://yandex.ru/search/?lr=28&text={}'.format(text['text_command']))
    elif text['command'] == 'google':
        webbrowser.open('https://www.google.ru/search?q={}'.format(text['text_command']))
    elif text['command'] == 'russia':
        webbrowser.open(
            'https://translate.yandex.ru/?utm_source=wizard&lang=en-ru&text={}'.format(text['text_command']))
    elif text['command'] == 'english':
        webbrowser.open(
            'https://translate.yandex.ru/?utm_source=wizard&lang=ru-en&text={}'.format(text['text_command']))

speak('как дела')
# name('пятница где находится китай')
# while True:
#     a = input('aa')
#     speak(a)
a = 'открыть гугл'
name(a)

# print(a.split())