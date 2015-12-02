#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
генератор случайных чисел
"""
import random

# Щепотка цифр
str1 = '123456789'
# Щепотка строчных букв
str2 = 'qwertyuiopasdfghjklzxcvbnm'
# Щепотка прописных букв. Готовится преобразованием str2  в верхний регистр.
str3 = str2.upper()
print str3
# Выведет: 'QWERTYUIOPASDFGHJKLZXCVBNM'

# Соединяем все строки в одну
str4 = str1+str2+str3
print str4
# Выведет: '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

# Преобразуем получившуюся строку в список
ls = list(str4)
# Тщательно перемешиваем список
random.shuffle(ls)
# Извлекаем из списка 12 произвольных значений
psw = ''.join([random.choice(ls) for x in range(12)])
# Пароль готов
print psw
# Выведет: '1t9G4YPsQ5L7'