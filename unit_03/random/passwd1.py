#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
генератор случайных чисел
"""
import random

print ''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(12)])