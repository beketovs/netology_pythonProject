"""Взять из папки файлы с новостями newsafr.json и newsafr.xml
Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort или sorted."""
# Задача №1. Написать программу для файла в формате json.

import json
from collections import Counter

with open("newsafr.json", encoding="utf-8") as f:
    data = json.load(f)
    array = list()
    temp_list = data['rss']['channel']['items']
    for key in temp_list:
        if key['description']:
            words = key['description'].split(" ")
            for word in words:
                if len(word) >= 6:
                    array.append(word)
print("ТОП 10 самых встречаемых слов:")
num_str = 0
for print_word, count in Counter(array).most_common()[0:10]:
    num_str += 1
    print(f'{num_str}. Слово "{print_word}" встречается в файле {count} раз(а)')