#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
генератор случайных чисел
"""
import random

psw = '' # предварительно создаем переменную psw
for x in range(12):
   psw = psw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

print psw