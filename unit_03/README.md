# 21v-pyqt 02


[![PyQt4](https://img.shields.io/badge/PyQt4-Requirements-yellowgreen.svg)](http://pyqt.sourceforge.net/Docs/PyQt4/index.html)
[![PyQt Books](https://img.shields.io/badge/PyQtBooks-Dep-brightgreen.svg)](https://wiki.python.org/moin/PyQt/Books)
[![PyQt wiki](https://img.shields.io/badge/PyQt-Wiki-orange.svg)](https://ru.wikipedia.org/wiki/PyQt)
[![devDependencies](https://img.shields.io/badge/JanusNic-Units-blue.svg)](https://github.com/janusnic/21v-pyqt)
[![MIT License](https://img.shields.io/cocoapods/l/AFNetworking.svg)](http://opensource.org/licenses/MIT)


QTimer ТАЙМЕРЫ
==============

Некоторые GUI приложения привязаны ко времени и крайне важно использовать таймер для захвата информации о работе программы и других аналогичных задач. Вы также можете использовать таймеры для генерации некоторых событий через определенный промежуток времени, рассчитать затраченное время на выполнение некоторых операций и прочее. 

Класс QtCore.QTimer
-------------------
Класс QTimer– это высокий уровень программного интерфейса для таймеров. Он использует повторяющие и одиночные таймеры. Повторяющиеся таймеры работают непрерывно и перезапускаются после того, как дойдут до конца заданного времени. Одиночные таймеры проходят заданный временной интервал один раз. Таймер может быть запущен, выполнив вызов start() объекта QTimer и может быть приостановлен в любой промежуток заданного времени командой stop():

```
QTimer.start(1000)
QTimer.stop()
```
Единица измерения в таймере - миллисекунда. Точность таймера зависит от операционной системы и оборудования. Большинство платформ поддерживают разрешение в 1 миллисекунду, хотя точность таймера может не соответствовать действительности.

Использование таймера в Qt
---------------------------
Для использования таймера в Qt предназначен класс QTimer. Сначала надо задать время, по истечении которого он будет срабатывать. Так же нужно определить слот, который обработает сигнал, излученный в следствие переполнения таймера. Таким образом, обязательным условием использования QTimer есть возможность использования сигналов и слотов. 

```
# call f() in 3 seconds
QTimer.singleShot(3000, f)

# Create a QTimer
timer = QTimer()

# Connect it to f
timer.timeout.connect(f)

# Call f() every 5 seconds
timer.start(5000)
```

pro­ces­­sEv­ents
-------------

```
def f():
    try:
        # Do things
    finally:
        QTimer.singleShot(5000, f)
f()
```
QtGui.QLCDNumber
----------------
QtGui.QLCDNumber отображает числа в стиле LCD. Числа, которые могут отображаться в стиле LCD, это 0/O, 1, 2, 3, 4, 5/S, 6, 7, 8, 9/g, минус, точка, A, B, C, D, E, F, h, H, L, o, P, r, u, U, Y, двоеточие, знак градуса (который указывается в виде одинарной кавычки в строках) и пробел. QtGui.QLCDNumber заменяет недопустимые символы на пробелы. Используя это, мы может вывести текст\цифры в любом размере. 

Секундомер timer1.py:
---------------------

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

# В большинстве GUI-приложений нам понадобится всего два класса. Это QtCore и QtGui. Модуль QtCore отвечает за обработку сигналов, слотов и за общее управление приложением. Модуль QtGui содержит в себе методы для создания и изменения различных GUI компонентов: окон и виджетов.

from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys

# Python поддерживает библиотеку стандартных модулей, которые встраиваются в интерпретатор и обеспечивают доступ к операциям, которые не являются частью основного языка. Один из таких модулей - sys, он предоставляет доступ к некоторым переменным и функциям, которые тесно взаимодействуют с интерпретатором. 

class myLCDNumber(QLCDNumber):
  value = 60
  # Следующий метод (слот) вызывется при каждом переполнении таймера  
  @pyqtSlot()
  def count(self):
    self.display(self.value)
    self.value = self.value-1


def main():    
    # нам нужен модуль sys, чтобы передать аргументы командной строки sys.argv в качестве параметра для класса QApplication. Он содержит список аргументов командной строки, передаваемых через Python. 

    app      = QApplication(sys.argv)
    lcdNumber    = myLCDNumber()

    # Resize width and height
    lcdNumber.resize(250,250)    
    lcdNumber.setWindowTitle('PyQt QTimer Секундомер')
    # Обновляем значение времени на форме  
    lcdNumber.display(60)
    timer = QTimer()
    # Связываем сигнал переполнения таймера со слотом
    lcdNumber.connect(timer,SIGNAL("timeout()"),lcdNumber,SLOT("count()"))
    # Задаем время срабатывания таймера (в мс)
    timer.start(1000) 

    lcdNumber.show()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```

В основной функции мы создали экземпляр класса QApplication. QApplication создает основный цикл обработки событий, где все события из оконной системы и других источников обрабатываются и передаются. Этот класс отвечает за инициализацию приложения, финализацию и управление сеансами. Он также обрабатывает события и следит за изменениями в приложение. Этот класс выстраивает свое поведение, отталкиваясь от полученных аргументов командой строки (sys.argv). Во всем приложение позволяется создавать только одни объект QApplication, даже если планируется создать несколько окон.

Объект QApplication должен создаваться до того, как другой объект обработается системой и внесет изменение в настройки вашего приложения. Так же следует создавать его до того, как будут переданы любые изменения аргументов командной строки.


создадим цифровые часы, объясняющих понятие таймеров.
-----------------------------------------------------

В классе, который является наследником QMainWindow (для примера используем стандартный класс главного окна ) объявляем экземпляр QTimer и слот для обработки:

timer2.py часы:
---------------
```
import sys
from PyQt4 import QtGui, QtCore
 
from time import strftime
 
class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
 
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        self.timer.start(1000)
 
        self.lcd = QtGui.QLCDNumber(self)
        self.lcd.display(strftime("%H"+":"+"%M"))
 
        self.setCentralWidget(self.lcd)
 
#---------Window settings --------------------------------
# Две функции setWindowTitle и setGeometry являются функциями QWidget, которая наследовала их классу QLabel. 
# Они используются, чтобы установить заголовок у ока и его положение на экране.         
        self.setGeometry(300,300,250,100)
        self.setWindowTitle("Clock")
 
#-------- Slots ------------------------------------------
 
    def Time(self):
        self.lcd.display(strftime("%H"+":"+"%M"))
         
def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
```
Функция setDigitCount
----------------------
Функция setDigitCount задает число цифр для отображение на дисплее, по умолчанию их используется пять.

timer3.py часы:
---------------
```

#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class myLCDNumber(QLCDNumber):

  @pyqtSlot()
  def showTime(self):
    #Show Current Time in "hh:mm:ss" format
    self.display(QTime.currentTime().toString(QString("hh:mm:ss")))
    

def main():    
    app      = QApplication(sys.argv)
    lcdNumber    = myLCDNumber()
    timer    = QTimer()

    #Resize width and height
    lcdNumber.resize(250,250)    
    lcdNumber.setWindowTitle("PyQt QLcdNumber-Current Time")  
    lcdNumber.setDigitCount(8)
    
    lcdNumber.connect(timer,SIGNAL("timeout()"),lcdNumber,SLOT("showTime()"))
    timer.start(1000) 

    lcdNumber.show()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```
Функция setSegmentStyle()
-------------------------
Функция setSegmentStyle() устанавливает стиль отображения QLCDNumber, он может принимать следующие параметры:

- QLCDNumber.Outline – цифры имеют цвет, как и цвет фона
- QLCDNumber.Filled – цифры имеют цвет, как и цвет текста
- QLCDNumber.Flat – цифры немного толщи, имеют цвет текста

dc.py:
------
```
#!/usr/bin/env python

from PyQt4 import QtCore, QtGui

class DigitalClock(QtGui.QLCDNumber):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        self.setSegmentStyle(QtGui.QLCDNumber.Filled)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

        self.setWindowTitle("Digital Clock")
        self.resize(150, 60)

    def showTime(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.display(text)


if __name__ == '__main__':

    import sys
    
    app = QtGui.QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    
    # вызываем функцию exec_() объекта QApplication, 
    # которая запустит основной цикл и начнет выполнять Qt код. 
    # И в конце мы завершаем программу, вызвав sys.exit().
    sys.exit(app.exec_())
```

Класс QtCore.QDateTime
----------------------
Класс QtCore.QDateTime содержит функции календаря и часов. Это сочетание классов QtCore.QDate и QtCore.QTime. Как и в любом другом фреймворке, класс QDateTime содержит функции для сравнения и манипуляции с датой и временем. Он содержит полный набор операторов для сравнения двух объектов QDateTime, где меньше - значит раньше, а больше - позже. QDateTime может хранить время, как локальное, так и UTC. Функция QDateTime.toUTC() может быть применена на объект QDateTime для преобразования местное времени в UTC. Также этот класс может переходить на летнее время.

QDateTime - dc1.py:
-------------------
Для отображения времени с точностью до секунды, мы запускаем таймер, который обновляется каждую секунду. Когда у таймера заканчивается время, мы вызываем функцию updtTime(), которая обновляет текущее время и отображает его на экране. Для того, чтобы отобразить часы в цифровом формате, мы использует специальное отображение QLCDNumber.
```
# -*- coding: utf-8 -*- 
import sys
from PyQt4.QtCore import QDateTime, QTimer, SIGNAL
from PyQt4.QtGui import QApplication, QWidget, QLCDNumber
 
class MyTimer(QWidget):
 
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle(u'Цифровые часы')
        
        timer = QTimer(self)
        
        self.connect(timer, SIGNAL("timeout()"), self.updtTime)
        self.myTimeDisplay = QLCDNumber(self)
        self.myTimeDisplay.setSegmentStyle(QLCDNumber.Filled)
        self.myTimeDisplay.setDigitCount(8)
        self.myTimeDisplay.resize(500, 150)
        
        timer.start(1000)
    
    def updtTime(self):
        currentTime = QDateTime.currentDateTime().toString('hh:mm:ss')
        self.myTimeDisplay.display(currentTime)
 
if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        myWindow = MyTimer()
        myWindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
```

Настройка изображений в качестве фона
-------------------------------------
Изображение можно "вставить" в компонент с помощью метода setBrush или с помощью CSS.

timer4.py часы:
---------------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class myLCDNumber(QLCDNumber):

  @pyqtSlot()
  def showTime(self):
    #Show Current Time in "hh:mm:ss" format
    self.display(QTime.currentTime().toString(QString("hh:mm:ss")))
    

def main():    
    app      = QApplication(sys.argv)
    lcdNumber    = myLCDNumber()
    timer    = QTimer()

    # создание объекта-палитры с помощью компонента
    palette = QPalette() 
    
    palette.setBrush(QPalette.Background,QBrush(QImage("bg.jpg")))    
    # использование объекта-палитры
    lcdNumber.setPalette(palette)    
    lcdNumber.setWindowTitle("QLcdnumber Background Image")    
    #Resize width and height
    lcdNumber.resize(500,400)

    lcdNumber.setDigitCount(8)
    
    lcdNumber.connect(timer,SIGNAL("timeout()"),lcdNumber,SLOT("showTime()"))
    timer.start(1000) 

    lcdNumber.show()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

```
QRadioButton
------------
Кнопка издает сигнал, когда она активируется каким-либо внешним воздействием, будь то мышь или клавиша пробел или сочетания клавиш. Виджет может быть связан с этим событием, которое выполняется при получение этого сигнала, в Qt его называют слотом - сигнал привязывается к слоту. Так же имеются и другие сигналы, вызываемые кнопкой, такие как нажата, отпущена, выбрана, активна и тд. Помимо нажатия кнопки, имеются и другие типы кнопок: QToolButton, QRadioButton, QCommandLinkButton и QCheckBox

timer5.py часы:
---------------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
 
from time import strftime
 
var = True
 
class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
 
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Time)
#Reduced update time to fasten the change from w/ secs to w/o secs
        timer.start(10)
 
        self.lcd = QtGui.QLCDNumber(self)
        self.lcd.resize(500,280)
         
#Added self.lcd.move and moved the clock 30px down to make space for buttons
         
        self.lcd.move(0,30)
        self.lcd.display(strftime("%H"+":"+"%M"))
 
        self.r1 = QtGui.QRadioButton("Hide seconds",self)
        self.r1.move(10,0)
        self.r2 = QtGui.QRadioButton("Show seconds",self)
        self.r2.move(110,0)
 
        self.r1.toggled.connect(self.woSecs)
        self.r2.toggled.connect(self.wSecs)
 
#---------Window settings --------------------------------
 
# Expanded window height by 30px
 
        
        self.setGeometry(500,500,500,300)
        self.setWindowTitle("Clock")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()
 
#-------- Slots ------------------------------------------
 
    def Time(self):
        global var
        if var == True:
            self.lcd.display(strftime("%H"+":"+"%M"))
        elif var == False:
            self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))
 
    def wSecs(self):
        global var
        var = False
         
        self.resize(500,300)
        self.lcd.resize(500,280)
        self.lcd.setDigitCount(8)
 
    def woSecs(self):
        global var
        var = True
         
        self.resize(500,300)
        self.lcd.resize(500,280)
        self.lcd.setDigitCount(5)

     
def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    # создание объекта-палитры с помощью получения текущей палитры компонента
    palette = main.palette() 
    # установка цвета для фона состояния Normal
    palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QImage("bg.jpg"))) 
    # использование объекта-палитры
    main.setPalette(palette)  
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
```

Генерация случайных чисел (модуль random)
=========================================
«Генерация случайных чисел слишком важна, чтобы оставлять её на волю случая»

—  Роберт Кавью

Python порождает случайные числа на основе формулы, так что они на самом деле не случайные, а, как говорят, псевдослучайные. Этот способ удобен для большинства приложений (кроме онлайновых казино).

Модуль random позволяет генерировать случайные числа. Прежде чем использовать модуль, необходимо подключить его с помощью инструкции:
```
import random
random.random
random.random() — возвращает псевдослучайное число от 0.0 до 1.0
```

random.seed
-------------
random.seed(Параметр) — настраивает генератор случайных чисел на новую последовательность. По умолчанию используется системное время. Если значение параметра будет одиноким, то генерируется одинокое число:

```
   random.seed(20)
   random.random()
```

random.uniform
--------------
random.uniform(Начало, Конец) — возвращает псевдослучайное вещественное число в диапазоне от Начало до Конец:

```
   random.uniform(0, 20)
   15.330185127252884
   random.uniform(0, 20)
   18.092324756265473
```
random.randint
---------------
random.randint(Начало, Конец) — возвращает псевдослучайное целое число в диапазоне от Начало до Конец:

```
    random.randint(1,27)
    9
    random.randint(1,27)
    22
```
random.choince
---------------
random.choince(Последовательность) — возвращает случайный элемент из любой последовательности (строки, списка, кортежа):

```

    random.choice('Chewbacca')
    'h'
    random.choice([1,2,'a','b'])
    2
    random.choice([1,2,'a','b'])
    'a'
```
random.randrange
-----------------
random.randrange(Начало, Конец, Шаг) — возвращает случайно выбранное число из последовательности.

random.shuffle
---------------
random.shuffle(Список) — перемешивает последовательность (изменяется сама последовательность). Поэтому функция не работает для неизменяемых объектов.

```
    List = [1,2,3,4,5,6,7,8,9]
    List
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(List)
    List
    [6, 7, 1, 9, 5, 8, 3, 2, 4]

```

Вероятностные распределения
---------------------------
- random.triangular(low, high, mode) — случайное число с плавающей точкой, low ≤ N ≤ high. Mode - распределение.

- random.betavariate(alpha, beta) — бета-распределение. alpha>0, beta>0. Возвращает от 0 до 1.

- random.expovariate(lambd) — экспоненциальное распределение. lambd равен 1/среднее желаемое. Lambd должен быть отличным от нуля. Возвращаемые значения от 0 до плюс бесконечности, если lambd положительно, и от минус бесконечности до 0, если lambd отрицательный.

- random.gammavariate(alpha, beta) — гамма-распределение. Условия на параметры alpha>0 и beta>0.

- random.gauss(значение, стандартное отклонение) — распределение Гаусса.

- random.lognormvariate(mu, sigma) — логарифм нормального распределения. Если взять натуральный логарифм этого распределения, то вы получите нормальное распределение со средним mu и стандартным отклонением sigma. mu может иметь любое значение, и sigma должна быть больше нуля.

- random.normalvariate(mu, sigma) — нормальное распределение. mu - среднее значение, sigma - стандартное отклонение.

- random.vonmisesvariate(mu, kappa) — mu - средний угол, выраженный в радианах от 0 до 2π, и kappa - параметр концентрации, который должен быть больше или равен нулю. Если каппа равна нулю, это распределение сводится к случайному углу в диапазоне от 0 до 2π.

- random.paretovariate(alpha) — распределение Парето.

- random.weibullvariate(alpha, beta) — распределение Вейбулла.

Генерация произвольного пароля
---------------------------------

Хороший пароль должен быть произвольным и состоять минимум из 6 символов, в нём должны быть цифры, строчные и прописные буквы. Приготовить такой пароль можно по следующему рецепту:

passwd.py
----------
```
    import random
    # Щепотка цифр
    str1 = '123456789'
    # Щепотка строчных букв
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    # Щепотка прописных букв. Готовится преобразованием str2  в верхний регистр.
    str3 = str2.upper()
    print(str3)
    # Выведет: 'QWERTYUIOPASDFGHJKLZXCVBNM'

    # Соединяем все строки в одну
    str4 = str1+str2+str3
    print(str4)
    # Выведет: '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

    # Преобразуем получившуюся строку в список
    ls = list(str4)
    # Тщательно перемешиваем список
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    psw = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    print(psw)
    # Выведет: '1t9G4YPsQ5L7'
```
Этот же скрипт можно записать всего в две строки:
```

    import random
    print(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxc
vbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(12)]))
```
Данная команда является краткой записью цикла for, вместо неё можно было написать так:
```
    import random
    psw = '' # предварительно создаем переменную psw
    for x in range(12):
        psw = psw + random.choice(list('123456789qwertyuiopasdfgh
jklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    print(psw)
    # Выведет: Ci7nU6343YGZ
```
Данный цикл повторяется 12 раз и на каждом круге добавляет к строке psw произвольно выбранный элемент из списка.


Сапёр (игра)
============

Принцип игры
--------------
Плоское или объёмное игровое поле разделено на смежные ячейки (квадраты, шестиугольники, кубы и т. п.), некоторые из которых «заминированы»; количество «заминированных» ячеек известно. Целью игры является открытие всех ячеек, не содержащих мины.

Игрок открывает ячейки, стараясь не открыть ячейку с миной. Открыв ячейку с миной, он проигрывает. Мины расставляются после первого хода, поэтому проиграть на первом же ходу невозможно. Если под открытой ячейкой мины нет, то в ней появляется число, показывающее, сколько ячеек, соседствующих с только что открытой, «заминировано» (в каждом варианте игры соседство определяется по-своему); используя эти числа, игрок пытается рассчитать расположение мин, однако иногда даже в середине и в конце игры некоторые ячейки всё же приходится открывать наугад. Если под соседними ячейками тоже нет мин, то открывается некоторая «не заминированная» область до ячеек, в которых есть цифры. «Заминированные» ячейки игрок может пометить, чтобы случайно не открыть их. Открыв все «не заминированные» ячейки, игрок выигрывает.

## Оценка сложности поля
Часто сложность поля оценивают с помощью величины 3BV (Bechtel’s Board Benchmark Value). Эта величина численно равна минимальному количеству непосредственных открытий ячеек (в стандартном варианте «Сапёра» открытия ячеек только левой кнопкой мыши, без использования флагов и двойных кликов), необходимому для открытия всего поля. Следует отметить, что эта величина отображает лишь количество определённых действий в идеальном случае при определенной манере игры, а вовсе не трудность расстановки для конкретного игрока.

## Рекорды
В большинстве вариантов игры подсчитывается время решения головоломки, поэтому регистрируются рекорды для стандартных уровней сложности игры. Для серьёзных соревнований используются версии игры, фиксирующие время прохождения с точностью до миллисекунд.

Результат сильно зависит от расположения мин. Теоретически при любых игровых параметрах есть вероятность прохождения одним щелчком. Но практическая реализация генератора случайных комбинаций не позволяет получить слишком простую расстановку на больших досках. Поэтому результаты на уровнях сложности Intermediate и Expert хорошо отражают уровень игрока. В официальных программах установлены ограничители для простых досок по 3bv. В настоящее время они составляют 2 для уровня сложности Beginner, 30 — Intermediate и 100 — Expert.
m1.py:
-------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Mine Sweeper Game
"""
import sys

from PyQt4 import QtCore, QtGui

class MyButton(QtGui.QPushButton):
  def __init__(self, parent=None):
    super(MyButton, self).__init__(parent)

class MainWindow(QtGui.QWidget):
  """ Main Wrapper For GUI """
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    setting = QtCore.QSettings()
    layout = QtGui.QGridLayout()
    layout.setMargin(1)
    layout.setSpacing(1)
    self.button = []
    for r in range(16):
      self.button.append( [] )
      for c in range(16):
        self.button[r].append( MyButton() )
        self.button[r][c].setFixedSize(20,20)
        self.button[r][c].row = r
        self.button[r][c].col = c
        self.button[r][c].parent = self
        self.button[r][c].revealed = False
        layout.addWidget( self.button[r][c], r, c)
    mainLayout = QtGui.QGridLayout()

    mainLayout.addLayout(layout,1,0)

    self.setLayout(mainLayout)
    self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)

  
### Main script
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

```
m2.py:
------

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Mine Sweeper Game
"""
import sys
from PyQt4 import QtCore, QtGui

class MyButton(QtGui.QPushButton):
  def __init__(self, parent=None):
    super(MyButton, self).__init__(parent)


class MainWindow(QtGui.QWidget):
  """ Main Wrapper For GUI """
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    setting = QtCore.QSettings()
    layout = QtGui.QGridLayout()
    layout.setMargin(1)
    layout.setSpacing(1)
    self.button = []
    for r in range(16):
      self.button.append( [] )
      for c in range(16):
        self.button[r].append( MyButton() )
        self.button[r][c].setFixedSize(20,20)
        self.button[r][c].row = r
        self.button[r][c].col = c
        self.button[r][c].parent = self
        self.button[r][c].revealed = False
        layout.addWidget( self.button[r][c], r, c)

    layouttop = QtGui.QHBoxLayout()
    layouttop.addWidget(QtGui.QLabel("BombCount"))
    self.bombcount = QtGui.QLabel("0/40")
    layouttop.addWidget(self.bombcount)
    self.timer = QtCore.QTimer()
    self.timelabel = QtGui.QLabel("0.0 secs")
    self.timelabel.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0,255,0)")

    layouttop.addWidget(self.timelabel)
    newgameButton = QtGui.QPushButton("&NewGame")
    newgameButton.setEnabled(True)
    layouttop.addWidget(newgameButton)
    topscore = QtGui.QPushButton("Top&Score>>")
    topscore.setCheckable(True)
    layouttop.addWidget(topscore)
    
    mainLayout = QtGui.QGridLayout()
    mainLayout.addLayout(layouttop,0,0)
    mainLayout.addLayout(layout,1,0)
    
    self.setLayout(mainLayout)
    self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)

### Main script
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

```

m3.py:
------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Mine Sweeper Game
"""

import sys
from PyQt4 import QtCore, QtGui

class MyButton(QtGui.QPushButton):
  def __init__(self, parent=None):
    super(MyButton, self).__init__(parent)

class MainWindow(QtGui.QWidget):
  """ Main Wrapper For GUI """
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    setting = QtCore.QSettings()
    layout = QtGui.QGridLayout()
    layout.setMargin(1)
    layout.setSpacing(1)
    self.button = []
    for r in range(16):
      self.button.append( [] )
      for c in range(16):
        self.button[r].append( MyButton() )
        self.button[r][c].setFixedSize(20,20)
        self.button[r][c].row = r
        self.button[r][c].col = c
        self.button[r][c].parent = self
        self.button[r][c].revealed = False
        layout.addWidget( self.button[r][c], r, c)
        
    layouttop = QtGui.QHBoxLayout()
    layouttop.addWidget(QtGui.QLabel("BombCount"))
    self.bombcount = QtGui.QLabel("0/40")
    layouttop.addWidget(self.bombcount)
    self.timer = QtCore.QTimer()
    self.timelabel = QtGui.QLabel("0.0 secs")
    self.timelabel.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0,255,0)")
    
    layouttop.addWidget(self.timelabel)
    newgameButton = QtGui.QPushButton("&NewGame")
    newgameButton.setEnabled(True)
    layouttop.addWidget(newgameButton)
    topscore = QtGui.QPushButton("Top&Score>>")
    topscore.setCheckable(True)
    layouttop.addWidget(topscore)
    self.scoreframe = QtGui.QFrame()
    self.scoreframe.setFrameStyle(QtGui.QFrame.StyledPanel|QtGui.QFrame.Sunken)
    scorelayout = QtGui.QVBoxLayout()
    scorelayout.addWidget(QtGui.QLabel(u"<b>Игра «Сапёр»</b> <i>Данное приложение является реализацией игры «Сапёр» <br>и может быть использовано как по прямому назначению, <br>так и в качестве reference solution.</i> <br>" ) )
    self.scoreframe.setLayout(scorelayout)
    self.scoreframe.setVisible(False)
    mainLayout = QtGui.QGridLayout()
    mainLayout.addLayout(layouttop,0,0)
    mainLayout.addLayout(layout,1,0)
    mainLayout.addWidget(self.scoreframe,0,1,2,1)
    self.setLayout(mainLayout)
    self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)
    
    Система обработки событий в PyQt4 построена на механизме сигналов и слотов. Если мы щёлкнем на кнопке, то будет послан сигнал clicked(). Слот может быть как слотом PyQt4 так и любым возможным для языка Пайтон. Метод QtCore.QObject.connect() соединяет сигнал и слот.

    QtCore.QObject.connect(topscore, QtCore.SIGNAL("clicked(bool)"), self.scoreframe.setVisible )

### Main script
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

```
QCloseEvent
------------
Когда мы закрываем виджет, генерируется событие QCloseEvent. Для изменения поведения виджета нам нужно изменить обработчик события QCloseEvent.
main4.py
---------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Mine Sweeper Game
"""
import sys
import os
import random
from PyQt4 import QtCore, QtGui

class MyButton(QtGui.QPushButton):
  def __init__(self, parent=None):
    super(MyButton, self).__init__(parent)

class MainWindow(QtGui.QWidget):
  """ Main Wrapper For GUI """
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    setting = QtCore.QSettings()
    tmp = setting.value("position", QtCore.QPoint(0,0))

    layout = QtGui.QGridLayout()
    layout.setMargin(1)
    layout.setSpacing(1)
    self.button = []
    for r in range(16):
      self.button.append( [] )
      for c in range(16):
        self.button[r].append( MyButton() )
        self.button[r][c].setFixedSize(20,20)
        self.button[r][c].row = r
        self.button[r][c].col = c
        self.button[r][c].parent = self
        self.button[r][c].revealed = False
        layout.addWidget( self.button[r][c], r, c)

    layouttop = QtGui.QHBoxLayout()
    layouttop.addWidget(QtGui.QLabel("BombCount"))
    self.bombcount = QtGui.QLabel("0/40")
    layouttop.addWidget(self.bombcount)
    self.timer = QtCore.QTimer()
    self.timelabel = QtGui.QLabel("0.0 secs")
    self.timelabel.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0,255,0)")
    self.newGame()
    layouttop.addWidget(self.timelabel)
    newgameButton = QtGui.QPushButton("&NewGame")
    newgameButton.setEnabled(True)
    layouttop.addWidget(newgameButton)
    topscore = QtGui.QPushButton("Top&Score>>")
    topscore.setCheckable(True)
    layouttop.addWidget(topscore)
    self.scoreframe = QtGui.QFrame()
    self.scoreframe.setFrameStyle(QtGui.QFrame.StyledPanel|QtGui.QFrame.Sunken)
    scorelayout = QtGui.QVBoxLayout()
    scorelayout.addWidget(QtGui.QLabel(u"<b>Игра «Сапёр»</b> <i>Данное приложение является реализацией игры «Сапёр» <br>и может быть использовано как по прямому назначению, <br>так и в качестве reference solution.</i> <br>" ) )
    self.scoreframe.setLayout(scorelayout)
    self.scoreframe.setVisible(False)
    mainLayout = QtGui.QGridLayout()
    mainLayout.addLayout(layouttop,0,0)
    mainLayout.addLayout(layout,1,0)
    mainLayout.addWidget(self.scoreframe,0,1,2,1)
    self.setLayout(mainLayout)
    self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)
    QtCore.QObject.connect(newgameButton, QtCore.SIGNAL("clicked()"), self.newGame)
    QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateTime)
    QtCore.QObject.connect(topscore, QtCore.SIGNAL("clicked(bool)"), self.scoreframe.setVisible )

  def newGame(self):

    self.marked = 0
    self.gamestarted = 0
    self.timer.stop()
    self.time = QtCore.QTime(0,0,0)
    self.timelabel.setText("0.0 secs")
    self.bombcount.setText("0/40")

#-----------------------------------------------------
  def updateTime(self):
    tmp = round(self.time.elapsed() / 1000, 1)
    self.timelabel.setText( str(tmp) + " secs" )
#-----------------------------------------------------
  def closeEvent(self, event):
    setting = QtCore.QSettings()
    setting.setValue("position", self.pos())

### Main script
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

```
main5.py
---------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Mine Sweeper Game
"""
import sys
import os
import random
from PyQt4 import QtCore, QtGui

class MyButton(QtGui.QPushButton):
  def __init__(self, parent=None):
    super(MyButton, self).__init__(parent)

class MainWindow(QtGui.QWidget):
  """ Main Wrapper For GUI """
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    setting = QtCore.QSettings()
    tmp = setting.value("position", QtCore.QPoint(0,0))

    layout = QtGui.QGridLayout()
    layout.setMargin(1)
    layout.setSpacing(1)
    self.button = []
    for r in range(16):
      self.button.append( [] )
      for c in range(16):
        self.button[r].append( MyButton() )
        self.button[r][c].setFixedSize(20,20)
        self.button[r][c].row = r
        self.button[r][c].col = c
        self.button[r][c].parent = self
        self.button[r][c].revealed = False
        layout.addWidget( self.button[r][c], r, c)

    layouttop = QtGui.QHBoxLayout()
    layouttop.addWidget(QtGui.QLabel("BombCount"))
    self.bombcount = QtGui.QLabel("0/40")
    layouttop.addWidget(self.bombcount)
    self.timer = QtCore.QTimer()
    self.timelabel = QtGui.QLabel("0.0 secs")
    self.timelabel.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0,255,0)")
    self.newGame()
    layouttop.addWidget(self.timelabel)
    newgameButton = QtGui.QPushButton("&NewGame")
    newgameButton.setEnabled(True)
    layouttop.addWidget(newgameButton)
    topscore = QtGui.QPushButton("Top&Score>>")
    topscore.setCheckable(True)
    layouttop.addWidget(topscore)
    self.scoreframe = QtGui.QFrame()
    self.scoreframe.setFrameStyle(QtGui.QFrame.StyledPanel|QtGui.QFrame.Sunken)
    scorelayout = QtGui.QVBoxLayout()
    scorelayout.addWidget(QtGui.QLabel(u"<b>Игра «Сапёр»</b> <i>Данное приложение является реализацией игры «Сапёр» <br>и может быть использовано как по прямому назначению, <br>так и в качестве reference solution.</i> <br>" ) )
    self.scoreframe.setLayout(scorelayout)
    self.scoreframe.setVisible(False)
    mainLayout = QtGui.QGridLayout()
    mainLayout.addLayout(layouttop,0,0)
    mainLayout.addLayout(layout,1,0)
    mainLayout.addWidget(self.scoreframe,0,1,2,1)
    self.setLayout(mainLayout)
    self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)
    QtCore.QObject.connect(newgameButton, QtCore.SIGNAL("clicked()"), self.newGame)
    QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateTime)
    QtCore.QObject.connect(topscore, QtCore.SIGNAL("clicked(bool)"), self.scoreframe.setVisible )

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
  def newGame(self):
    self.populateBombs()
    self.marked = 0
    self.gamestarted = 0
    self.timer.stop()
    self.time = QtCore.QTime(0,0,0)
    self.timelabel.setText("0.0 secs")
    self.bombcount.setText("0/40")

    for r in range(16):
      for c in range(16):
        self.button[r][c].revealed  = False
        self.button[r][c].setText("")
        self.button[r][c].setFlat(False)
        self.button[r][c].setEnabled(True)
        self.button[r][c].setPalette(QtGui.QPalette(QtGui.QColor(222,222,222)))
#-----------------------------------------------------
  def updateTime(self):
    tmp = round(self.time.elapsed() / 1000, 1)
    self.timelabel.setText( str(tmp) + " secs" )
#-----------------------------------------------------
  def closeEvent(self, event):
    setting = QtCore.QSettings()
    setting.setValue("position", self.pos())
#-----------------------------------------------------
# random.sample(population, k) - список длиной k из последовательности population.
  def populateBombs(self):
    bomblocation = random.sample(range(256), 40)
    x = 0
    for r in range(16):
      for c in range(16):
        self.button[r][c].bomb = True if x in bomblocation else False
        x = x + 1

### Main script
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

```

main6.py
---------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Mine Sweeper Game
"""
import sys
import os
import random
from PyQt4 import QtCore, QtGui


class MyButton(QtGui.QPushButton):
  def __init__(self, parent=None):
    super(MyButton, self).__init__(parent)

class MainWindow(QtGui.QWidget):
  """ Main Wrapper For GUI """
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    setting = QtCore.QSettings()
    tmp = setting.value("position", QtCore.QPoint(0,0))

    layout = QtGui.QGridLayout()
    layout.setMargin(1)
    layout.setSpacing(1)
    self.button = []
    for r in range(16):
      self.button.append( [] )
      for c in range(16):
        self.button[r].append( MyButton() )
        self.button[r][c].setFixedSize(20,20)
        self.button[r][c].row = r
        self.button[r][c].col = c
        self.button[r][c].parent = self
        self.button[r][c].revealed = False
        layout.addWidget( self.button[r][c], r, c)
        QtCore.QObject.connect(self.button[r][c], QtCore.SIGNAL("clicked()"), self.revealButtonWrapper )
    layouttop = QtGui.QHBoxLayout()
    layouttop.addWidget(QtGui.QLabel("BombCount"))
    self.bombcount = QtGui.QLabel("0/40")
    layouttop.addWidget(self.bombcount)
    self.timer = QtCore.QTimer()
    self.timelabel = QtGui.QLabel("0.0 secs")
    self.timelabel.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0,255,0)")
    self.newGame()
    layouttop.addWidget(self.timelabel)
    newgameButton = QtGui.QPushButton("&NewGame")
    newgameButton.setEnabled(True)
    layouttop.addWidget(newgameButton)
    topscore = QtGui.QPushButton("Top&Score>>")
    topscore.setCheckable(True)
    layouttop.addWidget(topscore)
    self.scoreframe = QtGui.QFrame()
    self.scoreframe.setFrameStyle(QtGui.QFrame.StyledPanel|QtGui.QFrame.Sunken)
    scorelayout = QtGui.QVBoxLayout()
    scorelayout.addWidget(QtGui.QLabel(u"<b>Игра «Сапёр»</b> <i>Данное приложение является реализацией игры «Сапёр» <br>и может быть использовано как по прямому назначению, <br>так и в качестве reference solution.</i> <br>" ) )
    self.scoreframe.setLayout(scorelayout)
    self.scoreframe.setVisible(False)
    mainLayout = QtGui.QGridLayout()
    mainLayout.addLayout(layouttop,0,0)
    mainLayout.addLayout(layout,1,0)
    mainLayout.addWidget(self.scoreframe,0,1,2,1)
    self.setLayout(mainLayout)
    self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)
    QtCore.QObject.connect(newgameButton, QtCore.SIGNAL("clicked()"), self.newGame)
    QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateTime)
    QtCore.QObject.connect(topscore, QtCore.SIGNAL("clicked(bool)"), self.scoreframe.setVisible )

  def newGame(self):
    self.populateBombs()
    self.marked = 0
    self.gamestarted = 0
    self.timer.stop()
    self.time = QtCore.QTime(0,0,0)
    self.timelabel.setText("0.0 secs")
    self.bombcount.setText("0/40")

    for r in range(16):
      for c in range(16):
        self.button[r][c].revealed  = False
        self.button[r][c].setText("")
        self.button[r][c].setFlat(False)
        self.button[r][c].setEnabled(True)
        self.button[r][c].setPalette(QtGui.QPalette(QtGui.QColor(222,222,222)))
#-----------------------------------------------------
  def disableAll(self):
    for r in range(16):
      for c in range(16):
        self.button[r][c].setEnabled(False)
        self.button[r][c].setFlat(True)
#-----------------------------------------------------
  def updateTime(self):
    tmp = round(self.time.elapsed() / 1000, 1)
    self.timelabel.setText( str(tmp) + " secs" )
#-----------------------------------------------------
  def closeEvent(self, event):
    setting = QtCore.QSettings()
    setting.setValue("position", self.pos())
#-----------------------------------------------------
  def revealButtonWrapper(self):
    if self.gamestarted == 0:
      self.time.start()
      self.timer.start(100)
      self.gamestarted = 1
    button = self.sender()
#-----------------------------------------------------
  def populateBombs(self):
    bomblocation = random.sample(range(256), 40)
    x = 0
    for r in range(16):
      for c in range(16):
        self.button[r][c].bomb = True if x in bomblocation else False
        x = x + 1

### Main script
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

```

main7.py
---------

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Mine Sweeper Game
"""
import sys
import os
import random
from PyQt4 import QtCore, QtGui

class MyButton(QtGui.QPushButton):
  def __init__(self, parent=None):
    super(MyButton, self).__init__(parent)
  
class MainWindow(QtGui.QWidget):
  """ Main Wrapper For GUI """
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    setting = QtCore.QSettings()
    tmp = setting.value("position", QtCore.QPoint(0,0))

    layout = QtGui.QGridLayout()
    layout.setMargin(1)
    layout.setSpacing(1)
    self.button = []
    for r in range(16):
      self.button.append( [] )
      for c in range(16):
        self.button[r].append( MyButton() )
        self.button[r][c].setFixedSize(20,20)
        self.button[r][c].row = r
        self.button[r][c].col = c
        self.button[r][c].parent = self
        self.button[r][c].revealed = False
        layout.addWidget( self.button[r][c], r, c)
        QtCore.QObject.connect(self.button[r][c], QtCore.SIGNAL("clicked()"), self.revealButtonWrapper )
    layouttop = QtGui.QHBoxLayout()
    layouttop.addWidget(QtGui.QLabel("BombCount"))
    self.bombcount = QtGui.QLabel("0/40")
    layouttop.addWidget(self.bombcount)
    self.timer = QtCore.QTimer()
    self.timelabel = QtGui.QLabel("0.0 secs")
    self.timelabel.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0,255,0)")
    self.newGame()
    layouttop.addWidget(self.timelabel)
    newgameButton = QtGui.QPushButton("&NewGame")
    newgameButton.setEnabled(True)
    layouttop.addWidget(newgameButton)
    topscore = QtGui.QPushButton("Top&Score>>")
    topscore.setCheckable(True)
    layouttop.addWidget(topscore)
    self.scoreframe = QtGui.QFrame()
    self.scoreframe.setFrameStyle(QtGui.QFrame.StyledPanel|QtGui.QFrame.Sunken)
    scorelayout = QtGui.QVBoxLayout()
    scorelayout.addWidget(QtGui.QLabel(u"<b>Игра «Сапёр»</b> <i>Данное приложение является реализацией игры «Сапёр» <br>и может быть использовано как по прямому назначению, <br>так и в качестве reference solution.</i> <br>" ) )
    self.scoreframe.setLayout(scorelayout)
    self.scoreframe.setVisible(False)
    mainLayout = QtGui.QGridLayout()
    mainLayout.addLayout(layouttop,0,0)
    mainLayout.addLayout(layout,1,0)
    mainLayout.addWidget(self.scoreframe,0,1,2,1)
    self.setLayout(mainLayout)
    self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)
    QtCore.QObject.connect(newgameButton, QtCore.SIGNAL("clicked()"), self.newGame)
    QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateTime)
    QtCore.QObject.connect(topscore, QtCore.SIGNAL("clicked(bool)"), self.scoreframe.setVisible )

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
  def newGame(self):
    self.populateBombs()
    self.marked = 0
    self.gamestarted = 0
    self.timer.stop()
    self.time = QtCore.QTime(0,0,0)
    self.timelabel.setText("0.0 secs")
    self.bombcount.setText("0/40")

    for r in range(16):
      for c in range(16):
        self.button[r][c].revealed  = False
        self.button[r][c].setText("")
        self.button[r][c].setFlat(False)
        self.button[r][c].setEnabled(True)
        self.button[r][c].setPalette(QtGui.QPalette(QtGui.QColor(222,222,222)))
#-----------------------------------------------------
  def disableAll(self):
    for r in range(16):
      for c in range(16):
        self.button[r][c].setEnabled(False)
        self.button[r][c].setFlat(True)
#-----------------------------------------------------
  def updateTime(self):
    tmp = round(self.time.elapsed() / 1000, 1)
    self.timelabel.setText( str(tmp) + " secs" )
#-----------------------------------------------------
  def closeEvent(self, event):
    setting = QtCore.QSettings()
    setting.setValue("position", self.pos())
#-----------------------------------------------------
  def revealButtonWrapper(self):
    if self.gamestarted == 0:
      self.time.start()
      self.timer.start(100)
      self.gamestarted = 1
    button = self.sender()
    self.revealButton( button )
#-----------------------------------------------------
Открыв ячейку с миной, игрок проигрывает.

  def revealButton(self, button):
    if button.bomb == True:
      txt = "X"
      color = QtGui.QColor(222,0,0)
      self.timer.stop()
      self.disableAll()
#-----------------------------------------------------
  def populateBombs(self):
    bomblocation = random.sample(range(256), 40)
    x = 0
    for r in range(16):
      for c in range(16):
        self.button[r][c].bomb = True if x in bomblocation else False
        x = x + 1

### Main script
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

```
main8.py
---------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Mine Sweeper Game
"""
import sys
import os
import random
from PyQt4 import QtCore, QtGui


class MyButton(QtGui.QPushButton):
  def __init__(self, parent=None):
    super(MyButton, self).__init__(parent)

class MainWindow(QtGui.QWidget):
  """ Main Wrapper For GUI """
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    setting = QtCore.QSettings()
    tmp = setting.value("position", QtCore.QPoint(0,0))

    layout = QtGui.QGridLayout()
    layout.setMargin(1)
    layout.setSpacing(1)
    self.button = []
    for r in range(16):
      self.button.append( [] )
      for c in range(16):
        self.button[r].append( MyButton() )
        self.button[r][c].setFixedSize(20,20)
        self.button[r][c].row = r
        self.button[r][c].col = c
        self.button[r][c].parent = self
        self.button[r][c].revealed = False
        layout.addWidget( self.button[r][c], r, c)
        QtCore.QObject.connect(self.button[r][c], QtCore.SIGNAL("clicked()"), self.revealButtonWrapper )
    layouttop = QtGui.QHBoxLayout()
    layouttop.addWidget(QtGui.QLabel("BombCount"))
    self.bombcount = QtGui.QLabel("0/40")
    layouttop.addWidget(self.bombcount)
    self.timer = QtCore.QTimer()
    self.timelabel = QtGui.QLabel("0.0 secs")
    self.timelabel.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0,255,0)")
    self.newGame()
    layouttop.addWidget(self.timelabel)
    newgameButton = QtGui.QPushButton("&NewGame")
    newgameButton.setEnabled(True)
    layouttop.addWidget(newgameButton)
    topscore = QtGui.QPushButton("Top&Score>>")
    topscore.setCheckable(True)
    layouttop.addWidget(topscore)
    self.scoreframe = QtGui.QFrame()
    self.scoreframe.setFrameStyle(QtGui.QFrame.StyledPanel|QtGui.QFrame.Sunken)
    scorelayout = QtGui.QVBoxLayout()
    scorelayout.addWidget(QtGui.QLabel(u"<b>Игра «Сапёр»</b> <i>Данное приложение является реализацией игры «Сапёр» <br>и может быть использовано как по прямому назначению, <br>так и в качестве reference solution.</i> <br>" ) )
    self.scoreframe.setLayout(scorelayout)
    self.scoreframe.setVisible(False)
    mainLayout = QtGui.QGridLayout()
    mainLayout.addLayout(layouttop,0,0)
    mainLayout.addLayout(layout,1,0)
    mainLayout.addWidget(self.scoreframe,0,1,2,1)
    self.setLayout(mainLayout)
    self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)
    QtCore.QObject.connect(newgameButton, QtCore.SIGNAL("clicked()"), self.newGame)
    QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateTime)
    QtCore.QObject.connect(topscore, QtCore.SIGNAL("clicked(bool)"), self.scoreframe.setVisible )

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
  def newGame(self):
    self.populateBombs()
    self.marked = 0
    self.gamestarted = 0
    self.timer.stop()
    self.time = QtCore.QTime(0,0,0)
    self.timelabel.setText("0.0 secs")
    self.bombcount.setText("0/40")

    for r in range(16):
      for c in range(16):
        self.button[r][c].revealed  = False
        self.button[r][c].setText("")
        self.button[r][c].setFlat(False)
        self.button[r][c].setEnabled(True)
        self.button[r][c].setStyleSheet("background-color: rgb(130, 130, 0); color: rgb(0,255,0)")
        
#-----------------------------------------------------
  def disableAll(self):
    for r in range(16):
      for c in range(16):
        self.button[r][c].setEnabled(False)
        self.button[r][c].setFlat(True)
#-----------------------------------------------------
  def updateTime(self):
    tmp = round(self.time.elapsed() / 1000, 1)
    self.timelabel.setText( str(tmp) + " secs" )
#-----------------------------------------------------
  def closeEvent(self, event):
    setting = QtCore.QSettings()
    setting.setValue("position", self.pos())
#-----------------------------------------------------
  def revealButtonWrapper(self):
    if self.gamestarted == 0:
      self.time.start()
      self.timer.start(100)
      self.gamestarted = 1
      Мины расставляются после первого хода, поэтому проиграть на первом же ходу невозможно.
    button = self.sender()
    self.revealButton( button )
#-----------------------------------------------------
  def revealButton(self, button):
    Открыв ячейку с миной, игрок проигрывает.
    if button.bomb == True:
      txt = "X"
      color = QtGui.QColor.fromRgb(255,0,0)
      self.timer.stop()
      self.disableAll()
    else:
      Если под открытой ячейкой мины нет, то в ней появляется число, показывающее, сколько ячеек, соседствующих с только что открытой, «заминировано»
      txt = str( self.grepSurroundingBombCount(button.row, button.col) )
      color = QtGui.QColor.fromRgb(0,0,255)

    button.revealed = True
    button.setText(txt)
    button.setFlat(True)
    button.setEnabled(False)
    
    button.setPalette(QtGui.QPalette(color))
    if txt == "0":
      for r,c in self.grepSurroundingLocation(button.row, button.col):
        if self.button[r][c].revealed == False:
          self.revealButton( self.button[r][c] )
#-----------------------------------------------------
  def grepSurroundingBombCount(self, row, col):
    count = 0
    tmp = self.grepSurroundingLocation(row,col)
    for r,c in self.grepSurroundingLocation(row,col):
      count = count + 1 if self.button[r][c].bomb == True else count
    return(count)
#-----------------------------------------------------
  def grepSurroundingLocation(self, row, col):
    """
    Если под соседними ячейками тоже нет мин, то открывается некоторая «не заминированная» область до ячеек, в которых есть цифры. 
    Получаем все соседние клетки и возвращаемся назад к списку [row,col]
    format. e.g:-
    [ [row,col], [r,c], [r,c] ....]
    """
    ret = []
    top = row-1
    bot = row+1
    left = col-1
    right = col+1
    ### Получить 3 клетки, если существуют
    if top > -1:
      ret.append( [top, col] )      # Сверху
    if bot < 16:
      ret.append( [bot, col] )      # Снизу
    if left > -1:
      ret.append( [row, left] )     # Слева
    if right < 16:
      ret.append( [row, right] )    # Справа
    if top > -1 and left > -1:
      ret.append( [top, left] )   # Сверху слева
    if top > -1 and right < 16:
      ret.append( [top, right] )  # Сверху справа
    if bot < 16 and left > -1:
      ret.append( [bot, left] )   # Снизу слева
    if bot < 16 and right < 16:
      ret.append( [bot, right] )  # Снизу справа
    return(ret)
#-----------------------------------------------------
  def populateBombs(self):
    bomblocation = random.sample(range(256), 40)
    x = 0
    for r in range(16):
      for c in range(16):
        self.button[r][c].bomb = True if x in bomblocation else False
        x = x + 1
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------

### Main script
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
#__________________________________________________________________________
#__________________________________________________________________________
```

создать свое всплывающее меню
-----------------------------
для этого требуется переопределять метлд contextMenuEvent нужного обьекта
main9.py
---------
```
#-----------------------------------------------------

class MyButton(QtGui.QPushButton):
  def __init__(self, parent=None):
    super(MyButton, self).__init__(parent)
  def contextMenuEvent(self, event):
    if self.text() == "?":
      self.setText("")
      # задаем цвет фона и символа
      self.setStyleSheet("background-color: rgb(255, 0, 0); color: rgb(0,255,0)")
      self.parent.marked -= 1
    else:
      self.setText("?")
      # задаем цвет фона и символа
      self.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255,0,255)")
      self.parent.marked += 1
    self.parent.bombcount.setText("%d/40" %self.parent.marked)

#__________________________________________________________________________
```
Задание
=======

1. Изменить цветовую палитру приложения

2. Содать 2 варианта игры

- По умолчанию 16 х 16
- Альтернативная версия 32 х 32
