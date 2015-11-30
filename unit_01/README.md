# 21v-pyqt
# PyQt4 - тулкит для разработки GUI приложений.
Он представляет из себя смесь языка программирование Pythonи библиотеки Qt. Qt – одна из наиболее мощных библиотек. Официальный сайт PyQt www.riverbankcomputing.co.uk разработан Филом Томпсоном.
PyQt4 представляет из себя набор модулей Пайтон. Она содержит более 300 классов и почти 6000 функций и методов. Это мультиплатформенный тулкит. Он работает на всех основных операционных системах, включая Unix, Windows и MacOS. Начиная с версии PyQt4 GPL доступна для всех поддерживаемых платформ.

- Так как тулкит содержит большое количество классов, они распределены в несколько модулей.
1. Модуль QtCore содержит ядро не-gui функциональности. Этот модуль используется для работы со временем, файлами и папками, различными типами даных, потоками, адресами URL, mime типами, потоками процессов.
2. Модуль QtGui содержит графические компоненты и связанные классы. Сюда включены, например, кнопки, окна, строки состояния, панели инструментов, полосы прокрутки, изображения (bitmap), цвета, шрифты и др.
3. МодульQtNetwork содержит классы для сетевого программирования. Эти классы позволяют писать TCP/IP и UDP клиенты и серверы. Они делают сетевое программирование легче и более доступным.
4. Модуль QtXml содержит классы для работы с xml файлами. Он предоставляет реализации API SAX и DOM.
5. Модуль QtSvg предоставляет классы для отображения содержимого SVG файлов. Масштабируемая векторная графика (SVG) – это язык описания двумерной графики и графических приложений на языке XML.
6. МодульQtOpenGL используется для построения 3D и 2D графики с помощью библиотеки OpenGL. Модуль дает возможность бесшовной интеграции библиотек QtGui и OpenGL.
7. Модуль QtSql содержит классы для работы с базами данных.

Простой пример 1.py
----------------------
Он отображает небольшое окошко. Мы сможем изменить его размеры. Распахнуть на весь экран. Минимизировать.

```

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

Он отображает небольшое окошко. 
Мы сможем изменить его размеры. 
Распахнуть на весь экран. 
Минимизировать.

"""

import sys
from PyQt4 import QtGui


def main():

    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
Подключаем необходимые модули.
------------------------------
-  Основные GUI виджеты находятся в библиотеке QtGui.
```
import sys
from PyQt4 import QtGui

```
Каждое приложение PyQt4 должно создать объект Qapplication.
-----------------------------------------------------------
```
app = QtGui.QApplication(sys.argv)
```
- Этот объект находится в модуле QtGui. Параметр sys.argv это список аргументов командной строки. Скрипты на Пайтон могут быть запущены из консоли, и с помощью аргументов мы можем контролировать запуск приложения.

```
Qwidget
--------
widget = QtGui.QWidget()
```
- Qwidget это базовый класс для всех объектов интерфейса пользователя для PyQt4. Мы используем стандартный конструктор для Qwidget, который не имеет родителя. Виджет у которого нет родительского является окном.

Изменение и получение размеров окна
------------------------------------

изменяет текущий размер окна. Если содержимое окна не nомещается в установленный размер, то размер будет выбран так, чтобы комnоненты nоместились без искажения, nри условии, что исnользуются менеджеры геометрии. Сле­довательно, заданный размер может не соответствовать реальному размеру окна. Если исnользуется абсолютное nозиционирование, то комnоненты могут оказаться наnолови­ну или nолностью за nределами видимой части окна. В качестве nараметра можно также указать экземnляр класса QSize. 
Метод resize()
--------------
- Метод resize() изменяет размеры виджета. В данном случае 250 пикселей по ширине и 150 по высоте.
```
widget.resize(250, 150)
```

- Здесь мы устанавлиаем заголовок окна на simple.
```
widget.setWindowTitle('simple')
```
Метод show()
------------
- Метод show() отображает окно на экране.
```
widget.show()
```
метод exit()
------------
```
sys.exit(app.exec())
```
В конце мы запускаем основной цикл приложения. Отсюда начинается обработка событий. Приложение получает события от оконной системы и распределяет их по виджетам. Когда цикл заканчивается, и если мы вызовем метод exit(), то наше окно (главный виджет) будет уничтожено. Метод sys.exit() гарантирует чистый выход. Окружение будет проинформировано о том, как приложение завершилось.


2. создать класс и конструктор для этого класса.
------------------------------------------------
setGeometry(X,У,Ширина,Высота)
-------------------------------
изменяет одновременно nоложение комnонента и его текущий размер. Первые два nараметра задают координаты левого верхнего угла (относительно родительского комnонента), а третий и четвертый nарамет­ры - ширину и высоту. В качестве nараметра можно также указать экземnляр класса QRect.

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4
Первое GUI-приложение

"""

import sys
from PyQt4 import QtGui, QtCore
        
class Example(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
 
        self.setGeometry(600, 300, 500, 150)
        self.setWindowTitle(u"Первое GUI-приложение")

app = QtGui.QApplication(sys.argv)

ex = Example()

ex.show()

sys.exit(app.exec_())


```

Пайтон поддерживает как процедурный, так и объекто-ориентированные стили программирования. Программирование на PyQt4 предполагает ООП программирование.

2.1. создать класс и конструктор для этого класса.
--------------------------------------------------

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4
Первое GUI-приложение

"""

import sys
from PyQt4 import QtGui, QtCore
        
class Example(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
 
        self.setGeometry(600, 300, 500, 150)
        self.setWindowTitle(u"Первое GUI-приложение")

def main():

    app = QtGui.QApplication(sys.argv)

    ex = Example()

    ex.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```

3. Всплывающая подсказка
-------------------------
Мы можем создать всплывающую подсказку для любого виджета.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
- В этом примере, мы показываем подсказку для виджета Qwidget.
self.setToolTip('This is a QWidget widget')

- Для создания подсказки вызываем метод setToolTip(). Можно использовать html тэги для форматирования.
QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))

4. Закрытие окна
-----------------
QPushButton(string text, QWidget parent = None)

- Это конструктор QPushButton, который мы будем использовать в нашем примере. Параметр text – это текст, который будет отображаться на кнопке, parent – тот виджет, на который мы поместим кнопку. В нашем случае это Qwidget.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
Мы создаём кнопку и распологаем её на виджете также, как мы размещали виджет на экране.
```
self.connect(quit, QtCore.SIGNAL('clicked()'),
QtGui.qApp, QtCore.SLOT('quit()'))
```
Система обработки событий в PyQt4 построена на механизме сигналов и слотов. Если мы щёлкнем на кнопке, то будет послан сигнал clicked(). Слот может быть как слотом PyQt4 так и любым возможным для языка Пайтон. Метод QtCore.QObject.connect() соединяет сигнал и слот. В нашем случае слот является предопределённым слотов PyQt4.

5.  Окно сообщений
-------------------
Обычно, при щелчке на кнопке закрытия в заголовке окна виджет закрывается. Иногда нам нужно изменить это действие. Например, если у нас открыт файл в редакторе с которым мы сделали какие-то изменения. В этом случае мы показываем пользователю сообщение для подтверждения выбранного действия.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()


    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

```
Когда мы закрываем виджет, генерируется событие QCloseEvent. Для изменения поведения виджета нам нужно изменить обработчик события QCloseEvent.
```
reply = QtGui.QMessageBox.question(self, 'Message',

    "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
```
Мы выводим сообщение с двумя кнопками “Да” и “Нет”. Первая строка ('Message') выводится в заголовке окна, вторая – текст сообщения. Возвращаемое значение хранится в переменной reply.
```
if reply == QtGui.QMessageBox.Yes:
    event.accept()
else:
    event.ignore()
```
Здесь мы проверяем возвращаемое значение: если щелкнули по кнопке “yes”, то мы принимаем стандартный обработчик, иначе – игнорируем закрытие.

# Управление расположением виджетов
 Управление расположением это то, как мы размещаем виджеты на форме. Тут есть два пути: использование абсолютного позиционирования (absolute positioning) или же использование классов расположения (layout classes).

6. Абсолютное позиционирование
-------------------------------
Программист указывает положение и размер каждого виджета в пикселях. Когда вы используете абсолютное расположение вы должны понимать несколько вещей:
- размер и положение виджета не изменяется при изменении размеров окна
- приложение может выглядеть различно на разных платформах
- изменение шрифта в вашем приложении может испортить расположение
- если вы решаете изменить раскладку, вы должны полностью повторить её, что отнимает много времени

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```
Мы просто вызываем метод move() для изменения положения виджетов, в нашем случае это QLabel. Мы располагаем их согласно координатам X и Y. Начало системы координат находится в левом верхнем углу окна. Координата X растёт справа налево, а Y сверху вниз. 

# Меню и панели инструментов

7. Строка состояния
--------------------
Строка состояния это виджет, который используется для отображения статусной информации.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```
8. Font
--------

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        fntMyFont = QtGui.QFont(self)
        fntMyFont.setBold(True)
        fntMyFont.setPixelSize(18)
        self.statusBar().setFont(fntMyFont)
        self.color = QtGui.QColor(255, 0, 0)
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

```

9.  color
----------

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        fntMyFont = QtGui.QFont(self)
        fntMyFont.setBold(True)
        fntMyFont.setPixelSize(18)
        self.statusBar().setFont(fntMyFont)
        
        
        self.button = QtGui.QPushButton('Dialog', self)
        self.button.setStyleSheet("background-color: red")

        palette = QtGui.QPalette(self.button.palette()) # make a copy of the palette
        palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor('blue'))
        self.button.setPalette(palette) # assign new palette

        self.button.move(20, 20)
  
        self.label = QtGui.QLineEdit(self)
        self.label.move(130, 22)

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

```

10. Box Layout
--------------
Управление расположением с помощью классов раскладки является более гибким и практичным. Это предпочтительный способ расположения виджетов. Простые классы раскладки это QHBoxLayout и QVBoxLayout. Они располагают виджеты горизонтально и вертикально.
Представим, что мы хотим разместить две кнопки в правом нижнем углу формы. Чтобы создать такую раскладку мы будем использовать один горизонтальный и один вертикальный box. Необходимое пространство мы получим добавив фактор растяжения (stretch factor).
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys, os
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
11.  QGridLayout
-----------------
Самый универсальный класс раскладок это расположение таблицей. Эта раскладка делит пространство на строки и столбцы. Для её создания используется класс QgridLayout.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys, os
from PyQt4 import QtGui

class Example(QtGui.QWidget):

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
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

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


12. Calculator
-----------------
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

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

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

13. sizeHint setHeight setWidth
-------------------------------
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

13. Operations
--------------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

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

        self.divisionButton = self.createButton("\367",
                self.multiplicativeOperatorClicked)
        self.multiplicatButton = self.createButton("\327",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)


        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.multiplicatButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def digitClicked(self):
        pass

    def multiplicativeOperatorClicked(self):
        pass

    def additiveOperatorClicked(self):
        pass

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()


```
## 15 Сигналы и слоты в PyQt4
События(events).
----------------
С помощью сигналов и слотов, в библиотеке PyQt4 происходит взаимодействие между объектами. Объектами могут выступать например, виджеты.

После запуска главного цикла app.exec_(), приложение начнет обрабатывать события. Например, когда будет нажата кнопка(QPushButton), то произойдет событие(сигнал) clicked(). События бывают пользовательские(например, нажатие кнопки) и системные.
Чтобы обработать событие(сигнал) объекта(например, QPushButton), необходимо его соединить с нужным слотом. Слотом является пользовательская или библиотечная функция.

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

## Переопределение событий 15_1.
В PyQt4 можно переопределять события, например:
-----------------------------------------------
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

## Отправка сигналов(генерация событий).
Объекты унаследованные от QtCore.QObject, могут оправлять сигналы. Например, создадим приложение, в котором при клике мыши в области окна, будет отправлен наш собственный сигнал ourSignal(), и соединим его со слотом закрытия окна 15-2:
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

## Создание своих слотов 15_3.
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

17.PY
-----
```
self.display = QtGui.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

mainLayout.addWidget(self.display, 0, 0, 1, 6)

```
## digitClicked(self):
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
