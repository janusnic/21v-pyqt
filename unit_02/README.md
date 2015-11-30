# 21v-pyqt 02


[![PyQt4](https://img.shields.io/badge/PyQt4-Requirements-yellowgreen.svg)](http://pyqt.sourceforge.net/Docs/PyQt4/index.html)
[![PyQt Books](https://img.shields.io/badge/PyQtBooks-Dep-brightgreen.svg)](https://wiki.python.org/moin/PyQt/Books)
[![PyQt wiki](https://img.shields.io/badge/PyQt-Wiki-orange.svg)](https://ru.wikipedia.org/wiki/PyQt)
[![devDependencies](https://img.shields.io/badge/JanusNic-Units-blue.svg)](https://github.com/janusnic/21v-pyqt)
[![MIT License](https://img.shields.io/cocoapods/l/AFNetworking.svg)](http://opensource.org/licenses/MIT)


grid1.py.  QGridLayout
----------------------
Самый универсальный класс раскладок это расположение таблицей. Эта раскладка делит пространство на строки и столбцы. Для её создания используется класс QgridLayout.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

В нашем примере, мы создаём таблицу кнопок.

"""
import sys, os
from PyQt4 import QtGui # подключает основные модули PyQt

# прототип главной формы
class Example(QtGui.QWidget):

    # конструктор
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QtGui.QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show() # даёт команду на отображение объекта формы и содержимого

def main():
    app = QtGui.QApplication(sys.argv) # создаёт основной объект программы
    ex = Example() # создаёт объект формы
    sys.exit(app.exec_()) # запускает приложение

if __name__ == '__main__':
    main()

```
В нашем примере, мы создаём таблицу кнопок. Одну ячейку оставляем пустой, добавляя один виджет QLabel.
```
grid = QtGui.QGridLayout()
```
Здесь мы создаём раскладку таблицей.
```
if j == 2:
    grid.addWidget(QtGui.QLabel(''), 0, 2)
else:
    grid.addWidget(button, pos[j][0], pos[j][1])
```
Чтобы добавить виджет в таблицу мы должны вызвать метод addWidget(), передав в качестве аргументов виджет, а также номера строки и столбца.


grid2.py Calculator
====================
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
from PyQt4 import QtGui, QtCore

# При добавлении действия на панель инструментов автоматически создается кнопка, реали­зуемая классом QToolButton.
class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)
        """
        Preferred- размер, возвращаемый методом sizeHint(), явлцется предпочтительным, но может быть как увеличен, так и уменьшен;
        Expanding - размер, возвращаемый методом sizeHint(), может быть как увеличен, так и уменьшен. Компоновщик должен предоставить компоненту столько пространства, сkолько возможно; 
        """
        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i)))

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text):
        button = Button(text)

        return button

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()

```

Клacc  QToolButton
--------------------
При добавлении действия на панель инструментов автоматически создается кнопка, реали­зуемая классом QToolButton.

QToolButton имеет следующий формат:
-------------------------------------
```
Объект= QToolButton([parent=Poдитeль])
```
Класс QToolВutton наследует все методы из базовых классов и содержит следующие доnол­нительные методы:

- setDefaultAction(QAction) - связывает объект действия с кноnкой. Метод является слотом с сигнатурой setDefaultAction(QAction *);
- defaultAction() - возвращает ссылку на объект действия (экземnляр класса QAction), связанный с кноnкой;
- setтoolButtonStyle (Стиль) - задает стиль кноnки. Метод является слотом с сигнату­рой setToolButtonstyle.

Доnустимые значения nараметра в оnисании метода setToolButtonStyle():
---------------------------------------------------------------------
- toolButtonStyle() - возвращает стиль кноnки;
- setMenu(QMenu) - добавляет меню;
- menu() - возвращает ссылку на меню (экземnляр класса QМenu) или значение None;
- showмenu() - отображает меню, связанное с кноnкой. Метод является слотом;
- setPopupMode(Режим) - задает режим отображения связанного с кноnкой меню. 

В ка­честве nараметра указываются следующие атрибуты из класса QToolВutton:
- DelayedPopup() - 0 - меню отображается nри удержании кноnки нажатой некоторый nромежуток времени;
- MenuButtonPopup - 1 - сnрава от кноnки отображается кноnка со стрелкой, нажaтие которой nриводит к немедленному отображению меню;
- InstantPopup - 2 - нажатие кноnки nриводит к немедленному отображению меню. Сигнал triggered() nри этом не генерируется;

- popupMode() - возвращает режим отображения связанного с кноnкой меню;
- setArrowType(Тип иконки) - nозволяет вместо стандартной иконки действия устано­вить иконку в виде стрелки, указывающей в заданном наnравлении. В качестве nарамет­ра указываются LeftArrow

- setAutoRaise(Флаг) - если в качестве nараметра указано значение False, то кноnка будет отображаться с рамкой. По умолчанию кноnка сливается с фоном, а nри наведе­нии указателя мыши становится выnуклой.
Класс QToolВutton содержит сигнал triggered(QAction *), который генерируется nри нажа­тии кноnки или комбинации клавиш, а также nри выборе nункта в связанном меню. Внутри обработчика через nараметр достуnен экземnляр класса QAction.


Класс QSizePolicy
------------------
Если в вертикальный контейнер большой высоты добавить надпись и кнопку, то под надпись будет выделено максимальное пространство, а кнопка займет пространство, доста­точное для рекомендуемых размеров, которые возвращает метод sizeHint(). 

Управление размерами компонентов внутри контейнера определяется правилами, установленными с помощью класса QSizePolicy. 

Установить правила для компонента можно с помощью ме­тода setSizePolicy(QSizePolicy) из класса QWidget, а получить значение с помощью ме­тода sizePolicy().

Создать экземпляр класса QSizePolicy можно следующим способом:
Объект = QSizePolicy([Пpaвилo для горизонтали, Правило для вертикали [,Тип компонента]])

Если параметры не заданы, то размер компонента должен точно соответствовать размерам, возвращаемым методом sizeHint().

В первом и втором параметрах указываются следую­щие атрибуты из класса QSizePolicy:

- Fixed - размер компонента должен точно соответствовать размерам, возвращаемым методом sizeHint();
- Minimum - размер, возвращаемый методом sizeHint(), является минимальным для ком­понента. Размер может быть увеличен компоновщиком;
- Maximum - размер, возвращаемый метоДом sizeHint (), является максимальным для компонента. Размер может быть уменьшен компоновщиком;
- Preferred- размер, возвращаемый методом sizeHint(), явлцется предпочтительным, но может быть как увеличен, так и уменьшен;
- Expanding - размер, возвращаемый методом sizeHint(), может быть как увеличен, так и уменьшен. Компоновщик должен предоставить компоненту столько пространства, сkолько возможно; 
- MinimumExpanding - размер, возвращаемый методом sizeHint(),является минимальным для компонента. Компоновщик должен предоставить компоненту столько пространства, сколько возможно;
- Ignored - размер, возвращаемый методом sizeHint (), игнорируется. Компонент получит столько пространства, сколько возможно.

Изменить значения уже после создания экземпляра класса QSizePolicy позволяют ме­тоды setHorizontalPolicy(Правило для горизонтали) И setVertica1Poliсу(Правило для вертикали)

компоненты, для которых установлена политика изме­нения размеров QSizePolicy.Expanding или QSizePolicy.MinimumExpanding, будут за­нимать всю доступную ширину. Размеры остальных компонентов будут соответство­вать рекомендуемым;


Получить размеры позволяют следующие методы:
--------------------------------------------
width() и height()
------------------
- возвращают текущую ширину и высоту соответственно:
```
window.resize(50, 70)
print(window.width(), window.height())
```
size()
-------
- возвращает экземпляр класса QSize, содержащий текущие размеры

sizeHint()
-----------
- возвращает экземпляр класса QSize, содержащий рекомендуемый размер компонента. Если возвращаемые размеры являются отрицательными, то считается, что нет рекомендуемого размера;

grid3.py sizeHint setHeight setWidth
------------------------------------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

```

Сигналы и слоты в PyQt4
=========================
События(events).
----------------
С помощью сигналов и слотов, в библиотеке PyQt4 происходит взаимодействие между объектами. Объектами могут выступать например, виджеты.

После запуска главного цикла app.exec_(), приложение начнет обрабатывать события. Например, когда будет нажата кнопка(QPushButton), то произойдет событие(сигнал) clicked(). События бывают пользовательские(например, нажатие кнопки) и системные.
Чтобы обработать событие(сигнал) объекта(например, QPushButton), необходимо его соединить с нужным слотом. Слотом является пользовательская или библиотечная функция.

slot1.py:
----------
```
import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
 
# ... insert the rest of the imports here
# Imports must precede all others ...
 
# Create a Qt app and a window
app = QApplication(sys.argv)
 
win = QWidget()
win.setWindowTitle('Test Window')
 
# Create a button in the window
btn = QPushButton('Test', win)
 
@pyqtSlot()
def on_click():
    ''' Tell when the button is clicked. '''
    print('clicked')
 
@pyqtSlot()
def on_press():
    ''' Tell when the button is pressed. '''
    print('pressed')
 
@pyqtSlot()
def on_release():
    ''' Tell when the button is released. '''
    print('released')
 
# connect the signals to the slots
btn.clicked.connect(on_click)
btn.pressed.connect(on_press)
btn.released.connect(on_release)
 
# Show the window and run the app
win.show()
app.exec_()
```

Переопределение событий slot2.py.
---------------------------------
В PyQt4 можно переопределять события, например:

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sys
from PyQt4 import QtGui, QtCore
 
class Escape(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
 
        self.setWindowTitle(self.trUtf8('Переопределение события'))
        self.resize(250, 150)
        self.connect(self, QtCore.SIGNAL('closeEmitApp()'), QtCore.SLOT('close()'))
 
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
 
app = QtGui.QApplication(sys.argv)
sigslot = Escape()
sigslot.show()
sys.exit(app.exec_())

```
мы переопределили событие keyPressEvent(QKeyEvent). Теперь при нажатии на кнопку «Esc», закрывается окно приложения.

Отправка сигналов(генерация событий).
--------------------------------------
Объекты унаследованные от QtCore.QObject, могут оправлять сигналы. Например, создадим приложение, в котором при клике мыши в области окна, будет отправлен наш собственный сигнал ourSignal(), и соединим его со слотом закрытия окна slot3.py:
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sys
from PyQt4 import QtGui, QtCore
 
class Emit(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
 
        self.setWindowTitle(self.trUtf8('Собственный сигнал'))
        self.resize(250, 150)
        self.connect(self, QtCore.SIGNAL('ourSignal()'), QtCore.SLOT('close()'))
 
    def mousePressEvent(self, event):
        self.emit(QtCore.SIGNAL('ourSignal()'))
 
app = QtGui.QApplication(sys.argv)
qb = Emit()
qb.show()
sys.exit(app.exec_())
```

- соединяем сигнал ourSignal() со слотом закрытия окна приложения.
- переопределяем событие mousePressEvent(QMouseEvent) и теперь при клике мышью в любой области окна, будет отправлен(сгенерирован) наш собственный сигнал ourSignal().

Создание своих слотов slot4.py.
-------------------------------
Так как слот это обычная функция, создадим приложение со своим слотом:
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sys, random
from PyQt4 import QtGui, QtCore
 
class withSlot(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
 
        self.setWindowTitle(self.trUtf8('Свой слот в PyQt'))
        self.resize(300, 50)
        self.button=QtGui.QPushButton('Get!', self)
        self.button.show()
 
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.button)
        self.setLayout(vbox)
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.getIt)
 
    def getIt(self):
        self.button.setText(str(random.randint(1, 10)))
 
app = QtGui.QApplication(sys.argv)
qb = withSlot()
qb.show()
sys.exit(app.exec_())

```
соединяем сигнал нажатия кнопки с нашим слотом getIt(), который рандомно меняет текст на кнопке.


grid4.py button.clicked.connect
--------------------------------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

button.clicked.connect

"""
import sys, os
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def digitClicked(self):
        pass

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()


```


События
========
Все приложения с графическим интерфейсом являются событийно-ориентированными. События вызываются главным образом пользователем приложения. Однако, они могут быть вызваны другими средствами, к примеру подключением к Интернету, диспетчером окон или таймером. Когда мы вызываем метод exec_(), приложение входит в главный цикл. Главный цикл получает события и отправляет их объектам.

В событийной модели имеются три участника:
--------------------------------------------
- Источник события;
- Объект события;
- Цель события.

Источник события – это объект, состояние которого меняется. Он вызывает события. Объект события (событие) внедряет состояние, которое меняется в источнике события. Цель события – это объект, которому требуется уведомление. Объект источника события поручает задачу обработки события цели события.

Чтобы начать работу с событиями, PyQt имеет уникальный механизм сигналов и слотов. Сигналы и слоты используют для связи между объектами. Сигнал срабатывает, когда происходит конкретное событие. Слот может быть чем-то, вызываемым средствами Python. Слот вызывается, когда срабатывает его сигнал.

Обработка сигналов и событий
-----------------------------
При взаимодействии пользователя с окном происходят события. В ответ на события система генерирует определенные сигналы. Сигналы — это своего рода извещения системы о том, что пользователь выполнил какое-либо действие или в самой системе возникло некоторое условие. Сигналы являются важнейшей составляющей приложения с графическим интерфейсом, поэтому необходимо знать, как назначить обработчик сигнала, как удалить обработчик, а также уметь правильно обработать событие. Какие сигналы генерирует тот или иной компонент мы будем рассматривать при изучении конкретного компонента.

Назначение обработчиков сигналов
---------------------------------
Чтобы обработать какой-либо сигнал необходимо сопоставить ему функцию или метод класса, которые будут вызваны при наступлении события. Назначить обработчик позволяет статический метод connect() из класса QObject. 
Форматы метода:
---------------
```
connect(<Объект>, <Сигнал>, <Обработчик>[, <ConnectionType>])
connect(<Объект1>, <Сигнал>, <Объект2>, <Слот>[, <ConnectionType>])
connect(<Объект1>, <Сигнал>, <Объект2>, <Сигнал>[, <ConnectionType>])
```
Кроме того, существует обычный (не статический) метод connect():
```
<Объект2>.connect(<Объект1>, <Сигнал>, <Слот>[, <ConnectionType>])
```
Первый формат позволяет назначить обработчик сигнала Сигнал, возникшего при изменении статуса объекта Объект. Если обработчик успешно назначен, то метод возвращает значение True. Для одного сигнала можно назначить несколько обработчиков, которые будут вызываться в порядке назначения в программе. 

В параметре Сигнал указывается результат выполнения функции SIGNAL(). 

Формат функции:
---------------
```
QtCore.SIGNAL("<Название сигнала>([Тип параметров])")
```
Каждый компонент имеет определенный набор сигналов, например, при щелчке на кнопке генерируется сигнал clicked(bool=0). Внутри круглых скобок могут быть указаны типы параметров, которые передаются в обработчик. Если параметров нет, то указываются только круглые скобки. Пример указания сигнала без параметров:
```
QtCore.SIGNAL("clicked()")
```
В этом случае обработчик не принимает никаких параметров. Указание сигнала с параметром выглядит следующим образом:
```
QtCore.SIGNAL("clicked(bool)")
```
В этом случае обработчик должен принимать один параметр, значение которого всегда будет равно 0 (False), так как это значение по умолчанию для сигнала clicked().

В параметре Обработчик можно указать:
--------------------------------------
- ссылку на пользовательскую функцию;
- ссылку на метод класса;
- ссылку на экземпляр класса. В этом случае внутри класса должен существовать метод __call__().

Пример обработки щелчка на кнопке con1.py
-----------------------------------------
```
# Варианты назначения пользовательского обработчика
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    print("Кнопка нажата. Функция on_clicked()")

class MyClass():
    def __init__(self, x=0):
        self.x = x
    def __call__(self):
        print("Кнопка нажата. Метод MyClass.__call__()")
        print("x =", self.x)
    def on_clicked(self):
        print("Кнопка нажата. Метод MyClass.on_clicked()")

obj = MyClass()
app = QtGui.QApplication(sys.argv)
button = QtGui.QPushButton(u"Нажми меня")

# Назначаем обработчиком функцию
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), on_clicked)

# Назначаем обработчиком метод класса
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), obj.on_clicked)

# Передача параметра в обработчик
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), MyClass(10))
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), MyClass(5))
button.show()
sys.exit(app.exec_())
```
Результат выполнения в окне консоли при одном щелчке на кнопке:
```
Кнопка нажата. Функция on_clicked()
Кнопка нажата. Метод MyClass.on_clicked()
Кнопка нажата. Метод MyClass.__call__()
x = 10
Кнопка нажата. Метод MyClass.__call__()
x = 5
```
Второй формат метода connect() назначает в качестве обработчика метод Qt-объекта Объект2. Обычно используется для назначения стандартного метода из класса, входящего в состав библиотеки Qt. В качестве примера при щелчке на кнопке завершим работу приложения.
```
# Завершение работы приложения при щелчке на кнопке con2.py
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys
app = QtGui.QApplication(sys.argv)
button = QtGui.QPushButton(u"Завершить работу")
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), app, QtCore.SLOT("quit()"))
button.show()
sys.exit(app.exec_())
```
в третьем параметре метода connect() указывается объект приложения, а в четвертом параметре в функцию SLOT() передается название метода quit() в виде строки. Благодаря гибкости языка Python данное назначение обработчика можно записать иначе:
```
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), app.quit)
```
Передача сигнала другому объекту
--------------------------------
Третий формат метода connect() позволяет передать сигнал другому объекту.
con3.py:
--------
```
# Передача сигнала другому объекту
##!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.button1 = QtGui.QPushButton(u"Кнопка 1. Нажми меня")
        self.button2 = QtGui.QPushButton(u"Кнопка 2")
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        self.setLayout(vbox)
        self.resize(300, 100)
        # Передача сигнала от кнопки 1 к кнопке 2
        self.connect(self.button1, QtCore.SIGNAL("clicked()"), self.button2, QtCore.SIGNAL('clicked()'))
        # Способ 1 (4 параметра)
        self.connect(self.button2, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("on_clicked_button2()"))
        # Способ 2 (3 параметра)
        self.connect(self.button2, QtCore.SIGNAL("clicked()"), QtCore.SLOT("on_clicked_button2()"))
    @QtCore.pyqtSlot()
    def on_clicked_button2(self):
        print("Сигнал получен кнопкой 2")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

В этом примере мы создали класс MyWindow, который наследует класс QtGui.QWidget.
В методе инициализации __init__() вначале вызывается конструктор базового класса и создаются две кнопки. Далее создается вертикальный контейнер и в него добавляются объекты кнопок с помощью метода addWidget(). С помощью метода setLayout() вертикальный контейнер добавляется в основное окно. Затем назначаются обработчики событий для кнопок. Обратите внимание на то, что метод connect() вызывается как метод нашего класса. Это возможно потому, что большинство PyQt-классов наследуют класс QObject, в котором определен метод connect(). Обработка нажатия кнопки производится с помощью метода on_clicked_button2(), который превращен декоратором @QtCore.pyqtSlot() в одноименный слот.
При нажатии первой кнопки производится вызов первого обработчика, который перенаправляет сигнал на вторую кнопку. Назначение перенаправления, соответствующее третьему формату метода connect(), выглядит так:
```
self.connect(self.button1, QtCore.SIGNAL("clicked()"), self.button2, QtCore.SIGNAL('clicked()'))
```
После перенаправления сигнала вызывается обработчик второй кнопки. Для второй кнопки мы назначили обработчик двумя способами. Первый способ соответствует второму формату метода connect():
```
self.connect(self.button2, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("on_clicked_button2()"))
```
Второй способ соответствует четвертому формату метода connect():
```
self.connect(self.button2, QtCore.SIGNAL("clicked()"), QtCore.SLOT("on_clicked_button2()"))
```
Необязательный параметр ConnectionType определяет тип соединения между сигналом и обработчиком. На этот параметр следует обратить особое внимание при использовании нескольких потоков в приложении, так как изменять GUI-поток из другого потока нельзя. 
В параметре можно указать одно из следующих атрибутов из класса QtCore.Qt:
--------------------------------------------------------------------------
- AutoConnection — 0 — значение по умолчанию. Если источник сигнала и обработчик находятся в одном потоке, то эквивалентно значению DirectConnection, а если в разных потоках — то QueuedConnection;
- DirectConnection — 1 — обработчик вызывается сразу после генерации сигнала. Обработчик выполняется в потоке источника сигнала;
- QueuedConnection — 2 — сигнал помещается в очередь обработки событий. Обработчик выполняется в потоке приемника сигнала;
- BlockingQueuedConnection — 4 — аналогично значению QueuedConnection, но пока сигнал не обработан поток будет заблокирован. Обратите внимание на то, что источник сигнала и обработчик должны быть обязательно расположены в разных потоках;
- UniqueConnection — 0x80 — аналогично значению AutoConnection, но обработчик можно назначить только если он не был назначен ранее. Например, если изменить способы назначения обработчика из предыдущего примера для кнопки button2 следующим образом, то второй обработчик назначен не будет:
```
st = self.connect(self.button2, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("on_clicked_button2()"), QtCore.Qt.UniqueConnection)
print(st)
st = self.connect(self.button2, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("on_clicked_button2()"), QtCore.Qt.UniqueConnection)
print(st)
```
Результат:
```
True
False
```
- AutoCompatConnection — 3 — значение использовалось по умолчанию в Qt.

```

def createButton(self, text, member):
        button = Button(text)
        # button.clicked.connect(member)
        QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), member)
        return button
```

Перегрузка QtCore.QObject.connect
---------------------------------
```
button.clicked.connect(member)

void clicked (bool = 0)
```

Отправитель события
--------------------
Отправитель – это объект, который посылает сигнал. Получатель – это объект, который получает сигнал. Слот – это метод, который реагирует на сигнал.

Иногда удобно знать, какой виджет является отправителем сигнала. Для этого, PyQt имеет метод sender().

Мы определяем источник сигнала путём вызова метода sender(). 
------------------------------------------------------------
```
    def digitClicked(self):
        
        clickedButton = self.sender()
        
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))
```

Срабатывание сигналов
----------------------

Объекты, создаваемые из QObject, могут имитировать сигналы. 

Мы создаём новый сигнал, именуемый SIGNAL("clicked()"). Этот сигнал испускается во время события нажатия кнопки мыши. Сигнал присоединяется к слоту quit() класса QApplication.
```
# Завершение работы приложения при щелчке на кнопке
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys
app = QtGui.QApplication(sys.argv)
button = QtGui.QPushButton("Завершить работу")
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), app, QtCore.SLOT("quit()"))
button.show()
sys.exit(app.exec_())
```

1.py
-----
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

class Calculator

"""
import sys, os
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size



class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton("\261",
                self.changeSignClicked)


        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 6)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text, member):
        button = Button(text)
        
        QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), member)
        return button

    def digitClicked(self):
        pass

    def multiplicativeOperatorClicked(self):
        pass

    def additiveOperatorClicked(self):
        pass

    def equalClicked(self):
        pass

    def pointClicked(self):
        pass

    def changeSignClicked(self):
        pass
        

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()

```
QLineEdit
-----------
QLineEdit – это виджет, который разрешает вводить и редактировать одну строку текста. 

Редактор строки позволяет пользователю вводить и редактировать одну строку простого текста с набором полезных функций редактирования, включая отмену, повтор, вырезание, вставку, а также перетаскивание с помощью механизма drag-and-drop.

Изменяя свойства echoMode() редактора, можно использовать его в качестве поля "только-для-записи" и для ввода паролей.
```
        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
```        

Длина текста может быть ограничена с помощью maxLength(). Для текста можно задать условия, используя validator() или inputMask(), либо оба их.
```
        
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)
```
QTextEdit - это подобный класс, но он позволяет редактировать многострочный форматированный текст.

Вы можете изменять текст с помощью setText() или insert(). Текст может быть получен с помощью text(); отображаемый текст (может отличаться от содержащегося текста) может быть получен с помощью displayText(). Текст может быть выделен с помощью setSelection() или selectAll(), а выделенный текст может быть вырезан с помощью cut(), скопирован с помощью copy() и вставлен с помощью paste(). Текст может быть выровнен с помощью setAlignment().

При изменении текста испускается сигнал textChanged(); при изменении текста с помощью setText(), испускается сигнал textEdited(); при перемещении курсора испускается сигнал cursorPositionChanged(); а при нажатии клавиш Return или Enter испускается сигнал returnPressed().

При окончании редактирования (редактор теряет фокус или нажата клавиша Return/Enter) испускается сигнал editingFinished().

Обратите внимание на то, что если установлено условие для текста (validator()), то сигналы returnPressed()/editingFinished() испускаются только в случае, если условие для текста возвращает QValidator::Acceptable.

По умолчанию, QLineEdits имеет рамку, определенную Windows или или стилем Motif; это может быть изменено с помощью setFrame(false).

Ниже приведены ключевые клавиши и сочетания клавиш и действия, вызываемые ими, определенные по умолчанию. Также редактор строки предоставляет контекстное меню (обычно вызываемое по нажатии правой кнопки мыши), в котором представлены некоторые из этих действий.

- Стрелка Влево   Перемещает курсор на один символ влево.
- Shift+Стрелка Влево Перемещает курсор на один символ влево с выделением текста.
- Стрелка Вправо  Перемещает курсор на один символ вправо.
- Shift+Стрелка Вправо    Перемещает курсор на один символ вправо с выделением текста.
- Home    Перемещает курсор в начало строки.
- End Перемещает курсор в конец строки.
- Backspace   Удаляет один символ, стоящий слева от курсора.
- Ctrl+Backspace  Удаляет одно слово, стоящее слева от курсора.
- Delete  Удаляет один символ, стоящий справа от курсора.
- Ctrl+Delete Удаляет одно слово, стоящее справа от курсора.
- Ctrl+A  Перемещает курсор в начало строки.
- Ctrl+B  Перемещает курсор в конец строки.
- Ctrl+C  Копирует выделенный текст в буфер обмена.
- Ctrl+Insert Копирует выделенный текст в буфер обмена.
- Ctrl+D  Удаляет один символ, стоящие справа от курсора.
- Ctrl+E  Перемещает курсор в конец строки.
- Ctrl+F  Перемещает курсор на один символ вправо.
- Ctrl+H  Удаляет один символ, стоящий слева от курсора.
- Ctrl+K  Удаляет все символы от курсора до конца строки.
- Ctrl+V  Вставляет текст в редактор из буфера обмена.
- Shift+Insert    Вставляет текст в редактор из буфера обмена.
- Ctrl+X  Удаляет выделенный текст и копирует его в буфер обмена.
- Shift+Delete    Удаляет выделенный текст и копирует его в буфер обмена.
- Ctrl+Z  Отменяет последнюю операцию.
- Ctrl+Y  Повторяет последнюю отмененную операцию.
Любые другие сочетания клавиш, имеющие символьное представление, приведут к вставке этого предаставления в строку.


Описание Типов Членов
----------------------

enum QLineEdit::EchoMode
------------------------
- QLineEdit::Normal   0   Отображаются те-же самые символы, что и введены. Это режим по умолчанию.
- QLineEdit::NoEcho   1   Не отображается вообще ничего. Этот режим может использоваться для ввода паролей там, где даже длинна пароля должна оставаться в секрете.
- QLineEdit::Password 2   Вместо фактически введенных символов отображаются звездочки.


acceptableInput : const bool
-----------------------------

Данное свойство сообщает, соответствует ли введенный текст маске ввода или условию, наложенному на текст.

Функции доступа:
----------------
bool hasAcceptableInput() const


alignment : Qt::Alignment
-------------------------

Данное свойство содержит выравнивание текста в редакторе.

Допускается только выравнивание по горизонтали, Qt::AlignJustify считается Qt::AlignLeft.
```
self.display.setAlignment(QtCore.Qt.AlignRight)
```

Функции доступа:
----------------
Qt::Alignment alignment() const
void setAlignment( Qt::Alignment flag )

cursorPosition : int
--------------------
Данное свойство содержит текущее положение курсора в редакторе.

Установка положения курсора приводит к перерисовке виджета, если необходимо.

Функции доступа:
-----------------
int cursorPosition() const
void setCursorPosition( int )

displayText : const QString
---------------------------
Данное свойство содержит отображаемый текст.

Если echoMode равно Normal, то возвращается тоже самое, что возвращается text(); если EchoMode равно Password, то возвращается строка, содержащаю звездочки, с длиной text().length() символов, например, "******"; если EchoMode равно NoEcho, то возвращается пустая строка, "".

Функции доступа:
----------------
QString displayText() const


dragEnabled : bool
---------------------
Данное свойство указывает, начинает ли редактор процесс перетаскивания, если пользователь начинает перемещать мышь с нажатой кнопкой над выделенным текстом.

По умолчанию перетаскивание запрещено.

Функции доступа:
----------------
bool dragEnabled() const
void setDragEnabled( bool b )

echoMode : EchoMode
--------------------
Данное свойство содержит режим отображения содержимого редактора.

Изначальное значение - это Normal, но QLineEdit также поддерживает режимы NoEcho и Password.

Это свойство влияет на отображение содержимого текста, возможность копирования и перетаскивания текста.

Функции доступа:
----------------
EchoMode echoMode() const
void setEchoMode( EchoMode )

frame : bool
------------
Данное свойство указывает, отображается ли рамка редактора.

Если рамка доступна (по умолчанию), то редактор рисуется внутри рамки, в противном случае редактор отображается без рамки.

Функции доступа:
----------------
bool hasFrame() const
void setFrame( bool )

hasSelectedText : const bool
----------------------------
Данное свойство сообщает, выделен ли какой либо текст в редакторе.

hasSelectedText() возвращает true, если пользователем выделена часть текста или весь текст; в противном случае возвращает false.

Функции доступа:
----------------
bool hasSelectedText () const

inputMask : QString
-------------------
Данное свойство содержит маску ввода.

Если маска не установлена, то inputMask() возвращает пустую строку.

Устанавливает маску ввода QLineEdit. Условие для текста может использоваться вместо маски или вместе с ней; 

Сброс маски в возвращение обычной работы QLineEdit производится с помощью передачи пустой строки ("") или с помощью вызова setInputMask() без аргументов.

Формат маски предусматривает следующие символы:
-----------------------------------------------

- A   Требуется алфавитный символ ASCII. A-Z, a-z.
- a   Разрешен, но не обязателен алфавитный симовл ASCII.
- N   Требуется алфавитный символ или цифра ASCII. A-Z, a-z, 0-9.
- n   Разрешен, но не обязателен алфавитный символ или цифра ASCII.
- X   Требуется любой символ.
- x   Разрешен, но не обязателен любой символ.
- 9   Требуется цифра ASCII. 0-9.
- 0   Разрешена, но не обязательна цифра ASCII.
- D   Требуется цифра ASCII не равная нулю. 1-9.
- d   Разрешена, но не обязательна цифра ASCII не равная нулю (1-9).
- #   Разрешена, но не обязательна цифра или знак плюс/минус ASCII.
- H   Требуется шестнадцатиричный символ. A-F, a-f, 0-9.
- h   Разрешен, но не обязателен шестнадцатиричный символ.
- B   Требуется двоичный символ. 0-1.
- b   Разрешен, но не обязателен двоичный символ.
- >   Все следующие алфавитный символы переводятся в верхний регистр.
- <   Все следующие алфавитный символы переводятся в нижний регистр.
- !   Изменение регистра отключается.
- \   Используйте \ для того, чтобы отменить действие вышеприведенных знаков, как специальных символов, и использовать их в качестве разделителей.
Маска состоит из строки символов маски и разделителей, иногда сопровождается точкой с запятой и символом, используемым для обозначения пробелов: символы пробелов всегда удаляются из строки после окончания редактирования. По умолчанию, символы пробела, соответствуют обычному пробелу.

Примеры:
-----------
- 000.000.000.000;_   IP-адрес; пробелы обозначаются символом _.
- HH:HH:HH:HH:HH:HH;_ MAC-адрес
- 0000-00-00  Дата ISO; пробелы обозначаются символом пробел
- >AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#    Лицензионный номер; пробелы обозначаются символом - и все (алфавитные) символы приводятся к верхнему регистру.
Для контроля диапазона символов (например, при вводе IP-адреса) используйте маску с условием для текста.

Функции доступа:
----------------
QString inputMask() const
void setInputMask( const QString & inputMask )


maxLength : int
----------------
Данное свойство содержит максимальную разрешенную длину текста.

Если текст очень длинный, то он обрезается по установленному пределу.

Если происходит обрезание текста, то текст становится не выделенным (если раньше что либо было выделено), курсор помещается в позицию 0 и отображается первая часть текста.

Если для редактора установлена маска ввода, то эта маска определяет максимальную длину текста.

Функции доступа:
----------------
int maxLength () const
void setMaxLength ( int )


modified : bool
---------------
Данное свойство указывает, было ли изменено содержимое редактора пользователем.

QLineEdit никогда не читает флаг изменения; по умолчанию флаг имеет значение false и изменяется на true всякий раз, когда пользователь изменяет содержимое редактора.

Это удобно в случаях, когда приложение предоставляет значение по умолчанию, но не знает, что такое значение есть (возможно, значение по умолчанию зависит от других полей формы). Сначала редактор не отображает значение по умолчанию, но при значет о нем, и только если modified() возвращает false (пользователь не ввел текст), вставляет значение по умолчанию.

Вызов setText() устанавливает флаг модификации в false.

Функции доступа:
-----------------
bool isModified() const
void setModified( bool )

readOnly : bool
---------------
Данное свойство указывает, позволяет ли редактор вводить текст или только читать.

В режиме только-для-чтения пользователь все еще может копировать в буфер обмена и перетаскивать текст (если echoMode() равно Normal), но не может редактировать его.

В режиме только-для-чтения, QLineEdit не отображает курсор.

Функции доступа:
-----------------
bool isReadOnly() const
void setReadOnly( bool )

redoAvailable : const bool
--------------------------
Данное свойство сообщает, доступен ли повтор последнего отмененного действия.

Функции доступа:
----------------
bool isRedoAvailable() const

selectedText : const QString
------------------------------
Данное свойство содержит выделенный текст.

Если ни какой текст не выделен, то значением свойства является пустая строка.

Функции доступа:
----------------
QString selectedText() const

text : QString
----------------
Данное свойство содержит редактируемый текст.

Установка данного свойства отменяет выделение текста, очищает историю отмены/повтора, устанавливает курсор в конец строки и устанавливает свойство modified в false. При вставке текста с помощью setText() не проверяется соответствие устанавливаемого текста заданному условию не текст.

Текст обрезается в соответствии с maxLength().

Функции доступа:
-----------------
QString text() const
void setText( const QString & )


undoAvailable : const bool
---------------------------
Данное свойство сообщает, доступна ли отмена последнего действия.

Функции доступа:
----------------
bool isUndoAvailable() const

Описание Функций-Членов
-----------------------
- QLineEdit::QLineEdit( QWidget * parent = 0 )

Создает не заполненный текстом редактор.

Максимальная длина текста установлена равной 32767 символам.

Аргумент parent передается в конструктор QWidget.


- QLineEdit::QLineEdit( const QString & contents, QWidget * parent = 0 )

Создает редактор, содержащий текст contents.

Курсор устанавливается в конец строки, а максимальная длина текста устанавливается равной 32767 символам.

Аргумент parent передается в конструктор QWidget.


- QLineEdit::~QLineEdit()

Разрушает редактор.

- void QLineEdit::backspace()

Если никакой текст не выделен, но символ, стоящий слева от курсора, удаляется, а курсор перемещается на одну позицию левее. Если есть выделенный текст, то курсор перемещается в начало выделенного текста, а выделенный текст удаляется.

- void QLineEdit::clear()   [slot]

Удаляет текст, содрежащийся в редакторе.

- void QLineEdit::contextMenuEvent ( QContextMenuEvent * event )   [virtual protected]

Отображает стандартное контекстное меню, созданное с помощью createStandardContextMenu().

Если Вы не хотите, чтобы редактор имел контекстное меню, то можете установить contextMenuPolicy в Qt::NoContextMenu. Если Вы хотите настроить контекстное меню, то должны заново реализовать данную функцию. Если Вы хотите расширить стандартное контекстное меню заново реализовав данную функцию, то вызовите createStandardContextMenu() и дополните возвращенное меню.
```
    void LineEdit::contextMenuEvent(QContextMenuEvent *event)
    {
        QMenu *menu = createStandardContextMenu();
        menu->addAction(tr("My Menu Item"));
        //...
        menu->exec(event->globalPos());
        delete menu;
    }
```
Параметр event используется для определения позиции, в которой находится указатель мыши во время создания сообщения контестного меню.

Заново реализовано по отношению к QWidget.

- void QLineEdit::copy () const   [slot]

Копирует выделенный текст, если таковой есть и если echoMode() равно Normal, в буфер обмена.

- QMenu * QLineEdit::createStandardContextMenu ()

Данная функция создает стандартное контекстное меню отображаемое при щелчке на редакторе правой кнопкой мыши. По умолчанию вызывается обработчиком сообщений contextMenuEvent(). Всплывающее меню передается вызывающему по значению.

- void QLineEdit::cursorBackward ( bool mark, int steps = 1 )

Перемещает курсор назад на steps символов. Если mark равно true, то каждый символ, через который перемещается курсор, выделяется; если mark равно false то выделение с текста снимается.

- void QLineEdit::cursorForward ( bool mark, int steps = 1 )

Перемещает курсор вперед на steps символов. Если mark равно true, то каждый символ, через который перемещается курсор, выделяется; если mark равно false то выделение с текста снимается.

- int QLineEdit::cursorPositionAt ( const QPoint & pos )

Возвращает позицию, которую мог бы занимать курсор, находясь в точке pos.

- void QLineEdit::cursorPositionChanged ( int old, int new )   [signal]

Данный сигнал испускается всякий раз при перемещении курсора. Предыдущая позиция курсора помещается в old, а новая позиция - в new.

- void QLineEdit::cursorWordBackward ( bool mark )

Перемещает курсор на одно слово назад. Если mark равно true, то слово выделяется.


- void QLineEdit::cursorWordForward ( bool mark )

Перемещает курсор на одно слово вперед. Если mark равно true, то слово выделяется.


- void QLineEdit::cut ()   [slot]

Копирует выделенный текст, если таковой имеется и если echoMode() равно Normal, в буфер обмена и удаляет его.

Если текущее условие на текст отвергает удаление выделенного текста, то cut() будет скопирован, но не удален.


- void QLineEdit::del ()

Если нет выделенного текста, то удаляется символ, стоящий справа от курсора. Если есть выделенный текст, то курсор перемещается в начало выделенного текста, а выделенный текст удаляется.


- void QLineEdit::deselect ()

Снимает выделение с выделенным текстом.


- void QLineEdit::editingFinished ()   [signal]

Данный сигнал испускается при нажатии клавиши Return или Enter или когда редактор теряет фокус. Обратите внимание, что если для редактора установлены validator() или inputMask() и нажата клавиша enter/return, то сигнал editingFinished() будет испущен только в том случае, если inputMask() и validator() для введенног текста возвратят QValidator::Acceptable.

- void QLineEdit::end ( bool mark )

Перемещает курсор в конец редактируемой строки (если он уже не там). Если mark равно true, то текст от текущего положения до конца строки добавляется к выделенному; в противном случае, выделение с выделенного текста снимается (если курсор перемещается).


- void QLineEdit::home ( bool mark )

Перемещает курсор в начало редактируемой строки (если он уже не там). Если mark равно true, то текст от начала строки до текущего положения добавляется к выделенному; в противном случае, выделение с выделенного текста снимается (если курсор перемещается).


- void QLineEdit::insert ( const QString & newText )

Удаляет выделенный текст, вставляет новый текст newText и проверяет соответствие результата на соответствие установленному условию. Если новый текст соответствует условию, то он становится новым содержимым редактора.


- void QLineEdit::keyPressEvent ( QKeyEvent * event )   [virtual protected]

Преобразует полученное сообщение клавиатуры event в действие редактора.

Если нажата клавиша Return или Enter и текущий текст соответствует установленному условию (или может быть сделан соответствующим объектом условия), то испускается сигнал returnPressed().

Список ействий клавиш, заданные по умолчанию, приведен в подробном описании класса.

Повторно реализовано по отношению к QWidget.

- QSize QLineEdit::minimumSizeHint () const   [virtual]

Возвращает минимальный размер редактора.

Ширина в возвращаемом значении достаточна для размещения по крайней мере одного символа.

Повторно реализовано по отношению к QWidget.

- void QLineEdit::paste ()   [slot]

Вставляет текст из буфера обмена в позицию курсора, удаляет выделенный текст. Поддреживается редактором, если он находится не в режиме только-для-чтения.

Если полученный результат не соответствует установленному условию (validator), ничего не происходит.


- void QLineEdit::redo ()   [slot]

Повторяет последнюю отмененную операцию если это возможно (свойство redoАvailable).

- void QLineEdit::returnPressed ()   [signal]

Данный сигнал испускается при нажатии клавиши Return или Enter. Обратите внимание, что если для редактора установлены validator() или inputMask(), то сигнал returnPressed() испускается только в том случае, если inputMask() и validator() для введенного текста возвращают QValidator::Acceptable.

- void QLineEdit::selectAll ()   [slot]

Выделяет весь текст (т.е. подсвечивает его) и перемещает курсор в конец строки. Это полезно при вставке значения по умолчанию, так как, если пользователь станет вводить текст в виджет, выделенный текст будет удален.


- void QLineEdit::selectionChanged ()   [signal]

Данный сигнал испускается всякий раз, когда изменяется выделение текста в редакторе.


- int QLineEdit::selectionStart () const

selectionStart() возвращает индекс первого выделенного символа или, если никакой текст не выделен, -1.


- void QLineEdit::setSelection ( int start, int length )

Выделяет фрагмент текста начинающийся в позиции start и имеющий длину length символов. Допускается отрицательное значение длины.


- void QLineEdit::setValidator ( const QValidator * v )

Устанавливает для редактора условие на вводимый текст v. Это позволяет устанавливать любые ограничения на вводимый текст.

Если v == 0, то setValidator() удаляет установленное условие на текст. Изначально для редактора не установлено никакое условие на текст (т.е. позволяется вводить любой текст длиной не более maxLength() символов).


- QSize QLineEdit::sizeHint () const   [virtual]

Возвращает рекомендуемый виджету размер.

Ширина, возвращаемая в пикселях, обычно достаточна для размещения 15-20 символам.

Повторно реализовано по отношению к QWidget.

- void QLineEdit::textChanged ( const QString & text )   [signal]

Данный сигнал испускается всякий раз при изменении текста. Аргумент text содержит новый текст.

В отличие от textEdited(), данный сигнал испускается даже тогда, когда текст в редакторе устанавливается программно, с помощью setText().

- void QLineEdit::textEdited ( const QString & text )   [signal]

Данный сигнал испускается всякий раз при редактировании текста. Аргумент text содрежит новый текст.

В отличие от textChanged(), данный сигнал не испускается при программной установке текста с помощью setText().

- void QLineEdit::undo ()   [slot]

Отменяет последнюю операцию, если отмена возможна (свойство undoAvailable. Снимает выделение текста и переносит начало выделения текста к текущему положению курсора.

- const QValidator * QLineEdit::validator () const

Возвращает указатель на текущее условие на вводимый текст или, если таковое условие на установлено, 0.

Этот пример показывает виджет строки редактирования и метку.
--------------------------------------------------------------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Example, self).__init__(parent)

        self.initUI()


    def initUI(self):

        self.lbl = QtGui.QLabel(self)
        qle = QtGui.QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()


    def onChanged(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```
Текст, который мы вбиваем в строку редактирования, немедленно отображается в виджете метки.
```
qle = QLineEdit(self)
```
Создается виджет QLineEdit.
```
qle.textChanged[str].connect(self.onChanged)
```
Если текст в виджете редактирования строки меняется, мы вызываем метод onChanged().
```
def onChanged(self, text):

    self.lbl.setText(text)
    self.lbl.adjustSize()
```
Внутри метода onChanged, мы устанавливаем напечатанный текст в виджет метки. Мы вызываем метод adjustSize(), чтобы менять размер метки соответственно длине текста.


### setText
```
    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False
```
### text

```

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)
```
2.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

"""
import sys, os
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        
        self.waitingForOperand = True

        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton("\261",
                self.changeSignClicked)


        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 6)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def multiplicativeOperatorClicked(self):
        pass

    def additiveOperatorClicked(self):
        pass

    def equalClicked(self):
        pass

    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()

```

## def calculate(self, rightOperand, pendingOperator)
```
    def abortOperation(self):
        self.clearAll()
        self.display.setText("####")

    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True
```

pending
-------
```
    self.pendingAdditiveOperator = ''
    self.pendingMultiplicativeOperator = ''
```
additiveOperatorClicked
-----------------------
```
    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True
```
def calculate
-------------
```

    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == "\327":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "\367":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True
```
3.py

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

"""
import sys, os
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size



class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''

        
        self.waitingForOperand = True

        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton("\261",
                self.changeSignClicked)


        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 6)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def multiplicativeOperatorClicked(self):
        pass

    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True


    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True

    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)

    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == "\327":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "\367":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()

```

4.py def multiplicativeOperatorClicked
-----------------------------------------

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

"""
import sys, os
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size



class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''

        
        self.waitingForOperand = True

        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton("\261",
                self.changeSignClicked)


        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 6)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def multiplicativeOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
        else:
            self.factorSoFar = operand

        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True

    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True


    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True

    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)

    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == "\327":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "\367":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()

```

Backspace Clear "Clear All
--------------------------
```
        self.backspaceButton = self.createButton("Backspace",
                self.backspaceClicked)
        self.clearButton = self.createButton("Clear", self.clear)
        self.clearAllButton = self.createButton("Clear All", self.clearAll)


        mainLayout.addWidget(self.backspaceButton, 1, 0, 1, 2)
        mainLayout.addWidget(self.clearButton, 1, 2, 1, 2)
        mainLayout.addWidget(self.clearAllButton, 1, 4, 1, 2)

        def backspaceClicked(self):
        if self.waitingForOperand:
            return

        text = self.display.text()[:-1]
        if not text:
            text = '0'
            self.waitingForOperand = True

        self.display.setText(text)

    def clear(self):
        if self.waitingForOperand:
            return

        self.display.setText('0')
        self.waitingForOperand = True

    def clearAll(self):
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        self.display.setText('0')
        self.waitingForOperand = True

```
5.py
-----
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

"""
import sys, os
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size



class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''

     
        self.waitingForOperand = True

        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton("\261",
                self.changeSignClicked)

        self.backspaceButton = self.createButton("Backspace",
                self.backspaceClicked)
        self.clearButton = self.createButton("Clear", self.clear)
        self.clearAllButton = self.createButton("Clear All", self.clearAll)


        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 6)
        mainLayout.addWidget(self.backspaceButton, 1, 0, 1, 2)
        mainLayout.addWidget(self.clearButton, 1, 2, 1, 2)
        mainLayout.addWidget(self.clearAllButton, 1, 4, 1, 2)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def multiplicativeOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
        else:
            self.factorSoFar = operand

        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True

    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True


    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True

    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)

    def backspaceClicked(self):
        if self.waitingForOperand:
            return

        text = self.display.text()[:-1]
        if not text:
            text = '0'
            self.waitingForOperand = True

        self.display.setText(text)

    def clear(self):
        if self.waitingForOperand:
            return

        self.display.setText('0')
        self.waitingForOperand = True

    def clearAll(self):
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        self.display.setText('0')
        self.waitingForOperand = True

    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == "\327":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "\367":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()

```
unaryOperatorClicked
---------------------
```
        self.squareRootButton = self.createButton("Sqrt",
                self.unaryOperatorClicked)
        self.powerButton = self.createButton("x\262",
                self.unaryOperatorClicked)
        self.reciprocalButton = self.createButton("1/x",
                self.unaryOperatorClicked)
        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout.addWidget(self.squareRootButton, 2, 5)
        mainLayout.addWidget(self.powerButton, 3, 5)
        mainLayout.addWidget(self.reciprocalButton, 4, 5)
        mainLayout.addWidget(self.equalButton, 5, 5)

    def unaryOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if clickedOperator == "Sqrt":
            if operand < 0.0:
                self.abortOperation()
                return

            result = math.sqrt(operand)
        elif clickedOperator == "x\262":
            result = math.pow(operand, 2.0)
        elif clickedOperator == "1/x":
            if operand == 0.0:
                self.abortOperation()
                return

            result = 1.0 / operand

        self.display.setText(str(result))
        self.waitingForOperand = True

mport math
```
6.py
------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

""" # Хорошо написанная документация на модуль, может быть отображена при help(имя_модуля).

import sys, os
import math
from PyQt4 import QtGui, QtCore # Из модуля PyQt4 импортируем подмодуль QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size



class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''

        self.waitingForOperand = True

        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton("\261",
                self.changeSignClicked)

        self.backspaceButton = self.createButton("Backspace",
                self.backspaceClicked)
        self.clearButton = self.createButton("Clear", self.clear)
        self.clearAllButton = self.createButton("Clear All", self.clearAll)


        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        self.squareRootButton = self.createButton("Sqrt",
                self.unaryOperatorClicked)
        self.powerButton = self.createButton("x\262",
                self.unaryOperatorClicked)
        self.reciprocalButton = self.createButton("1/x",
                self.unaryOperatorClicked)
        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        # Создаём виждет.
        mainLayout.addWidget(self.display, 0, 0, 1, 6)
        mainLayout.addWidget(self.backspaceButton, 1, 0, 1, 2)
        mainLayout.addWidget(self.clearButton, 1, 2, 1, 2)
        mainLayout.addWidget(self.clearAllButton, 1, 4, 1, 2)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        
        mainLayout.addWidget(self.squareRootButton, 2, 5)
        mainLayout.addWidget(self.powerButton, 3, 5)
        mainLayout.addWidget(self.reciprocalButton, 4, 5)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")
        # Заголовок окна, отображается в рамке и панели задач.
    
    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def unaryOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if clickedOperator == "Sqrt":
            if operand < 0.0:
                self.abortOperation()
                return

            result = math.sqrt(operand)
        elif clickedOperator == "x\262":
            result = math.pow(operand, 2.0)
        elif clickedOperator == "1/x":
            if operand == 0.0:
                self.abortOperation()
                return

            result = 1.0 / operand

        self.display.setText(str(result))
        self.waitingForOperand = True

    def multiplicativeOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
        else:
            self.factorSoFar = operand

        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True

    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True


    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True

    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)

    def backspaceClicked(self):
        if self.waitingForOperand:
            return

        text = self.display.text()[:-1]
        if not text:
            text = '0'
            self.waitingForOperand = True

        self.display.setText(text)

    def clear(self):
        if self.waitingForOperand:
            return

        self.display.setText('0')
        self.waitingForOperand = True

    def clearAll(self):
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        self.display.setText('0')
        self.waitingForOperand = True

    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == "\327":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "\367":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True

def main():
    # Для удобства работы, определим главную функцию нашего примера:
    app = QtGui.QApplication(sys.argv)
    # Создаём класс QApplication, который управляет
    # всем приложением на PyQt4.
    calc = Calculator()
    sys.exit(calc.exec_())
    # app.exec_() содержит в себе главный цикл обработки событий бибиотеки
    # PyQt4, который завершится, когда пользователь закроет окно или мы
    # своей программе вызовем функцию завершения этого цикла. Только после
    # этого прозойдёт выход из питона с помощью функции sys.exit.


if __name__ == '__main__':
    # Если файл запущен как программа (а не импортирован как модуль),
    main()                 # вызовем фукнцийю main.
    

```
clearMemoryButton

```
        self.clearMemoryButton = self.createButton("MC", self.clearMemory)
        self.readMemoryButton = self.createButton("MR", self.readMemory)
        self.setMemoryButton = self.createButton("MS", self.setMemory)
        self.addToMemoryButton = self.createButton("M+", self.addToMemory)


        mainLayout.addWidget(self.clearMemoryButton, 2, 0)
        mainLayout.addWidget(self.readMemoryButton, 3, 0)
        mainLayout.addWidget(self.setMemoryButton, 4, 0)
        mainLayout.addWidget(self.addToMemoryButton, 5, 0)


   def clearMemory(self):
        self.sumInMemory = 0.0

    def readMemory(self):
        self.display.setText(str(self.sumInMemory))
        self.waitingForOperand = True

    def setMemory(self):
        self.equalClicked()
        self.sumInMemory = float(self.display.text())

    def addToMemory(self):
        self.equalClicked()
        self.sumInMemory += float(self.display.text())

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def abortOperation(self):
        self.clearAll()
        self.display.setText("####")
```
7.py
------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

"""
import sys, os
import math
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size



class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''

        self.sumInMemory = 0.0
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.waitingForOperand = True

        self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton("\261",
                self.changeSignClicked)

        self.backspaceButton = self.createButton("Backspace",
                self.backspaceClicked)
        self.clearButton = self.createButton("Clear", self.clear)
        self.clearAllButton = self.createButton("Clear All", self.clearAll)


        self.clearMemoryButton = self.createButton("MC", self.clearMemory)
        self.readMemoryButton = self.createButton("MR", self.readMemory)
        self.setMemoryButton = self.createButton("MS", self.setMemory)
        self.addToMemoryButton = self.createButton("M+", self.addToMemory)

        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        self.squareRootButton = self.createButton("Sqrt",
                self.unaryOperatorClicked)
        self.powerButton = self.createButton("x\262",
                self.unaryOperatorClicked)
        self.reciprocalButton = self.createButton("1/x",
                self.unaryOperatorClicked)
        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 6)
        mainLayout.addWidget(self.backspaceButton, 1, 0, 1, 2)
        mainLayout.addWidget(self.clearButton, 1, 2, 1, 2)
        mainLayout.addWidget(self.clearAllButton, 1, 4, 1, 2)

        mainLayout.addWidget(self.clearMemoryButton, 2, 0)
        mainLayout.addWidget(self.readMemoryButton, 3, 0)
        mainLayout.addWidget(self.setMemoryButton, 4, 0)
        mainLayout.addWidget(self.addToMemoryButton, 5, 0)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        
        mainLayout.addWidget(self.squareRootButton, 2, 5)
        mainLayout.addWidget(self.powerButton, 3, 5)
        mainLayout.addWidget(self.reciprocalButton, 4, 5)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def unaryOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if clickedOperator == "Sqrt":
            if operand < 0.0:
                self.abortOperation()
                return

            result = math.sqrt(operand)
        elif clickedOperator == "x\262":
            result = math.pow(operand, 2.0)
        elif clickedOperator == "1/x":
            if operand == 0.0:
                self.abortOperation()
                return

            result = 1.0 / operand

        self.display.setText(str(result))
        self.waitingForOperand = True

    def multiplicativeOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
        else:
            self.factorSoFar = operand

        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True

    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True


    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True

    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)

    def backspaceClicked(self):
        if self.waitingForOperand:
            return

        text = self.display.text()[:-1]
        if not text:
            text = '0'
            self.waitingForOperand = True

        self.display.setText(text)

    def clear(self):
        if self.waitingForOperand:
            return

        self.display.setText('0')
        self.waitingForOperand = True

    def clearAll(self):
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        self.display.setText('0')
        self.waitingForOperand = True

    def clearMemory(self):
        self.sumInMemory = 0.0

    def readMemory(self):
        self.display.setText(str(self.sumInMemory))
        self.waitingForOperand = True

    def setMemory(self):
        self.equalClicked()
        self.sumInMemory = float(self.display.text())

    def addToMemory(self):
        self.equalClicked()
        self.sumInMemory += float(self.display.text())

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def abortOperation(self):
        self.clearAll()
        self.display.setText("####")


    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == "\327":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "\367":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()

```
Задание
=======
1. разделить визуальное представление и логику программы.
- main.py - главный файл, запускающий программу;
- mainform.py — файл описания главного окна.

2. дополнить программу вычислением функций sin, cos и log
