#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
генератор случайных чисел
"""
import random

# random.random
print random.random() # — возвращает псевдослучайное число от 0.0 до 1.0


# random.seed
# random.seed(<Параметр>) — настраивает генератор случайных чисел на новую последовательность. По умолчанию используется системное время. Если значение параметра будет одиноким, то генерируется одинокое число:


random.seed(20)
print random.random()

random.uniform(0, 20)
print random.random()
random.uniform(0, 20)
print random.random()

random.randint(1,27)
print random.random()

random.choice('Chewbacca')
print random.random()
random.choice([1,2,'a','b'])
print random.random()
random.choice([1,2,'a','b'])
print random.random()

List = [1,2,3,4,5,6,7,8,9]
print List
random.shuffle(List)
print List
    