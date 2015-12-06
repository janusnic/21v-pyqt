# 21v-pyqt unit 04

Стандартные диалоги
====================
QInputDialog представляет собой стандартный диалог, чтобы получить одно значения от пользователя. Значение может быть целым числом, строкой или элементом списка.
```
#!/usr/bin/python
# inputdialog.py

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class InputDialog(QtGui.QWidget):
   def __init__(self, parent=None):
       QtGui.QWidget.__init__(self, parent)
       self.setGeometry(300, 300, 350, 80)
       self.setWindowTitle('InputDialog')
       self.button = QtGui.QPushButton('Dialog', self)
       self.button.setFocusPolicy(QtCore.Qt.NoFocus)
       self.button.move(20, 20)
       self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
       self.setFocus()
       self.label = QtGui.QLineEdit(self)
       self.label.move(130, 22)

   def showDialog(self):
       text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
       if ok:
           self.label.setText(unicode(text))
           
app = QtGui.QApplication(sys.argv)
icon = InputDialog()
icon.show()
app.exec_()
```
В этом примере у нас имеется виджет с кнопкой и строкой для редактирования. При нажатии на кнопку мы увидим диалоговое окно, куда можем ввести значение. После того как мы ввели текст и нажали кнопку ввода, мы получим в строке редактирования виждета введенное значение.


```
   text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
```
Эта строка отображает диалогове окно. Первое значение - это название диалогового окна, второе значение - сообщение в диалоговом окне. Диалог возвращает введенный текст и булево значение. Если Вы нажали кнопку Ок, то мы получим булево значение True, в противном случае - False.


QColorDialog
=============

QColorDialog предоставляет виджет в виде диалоговго окна, где пользователь может выбрать цвет.
```
#!/usr/bin/python
# colordialog.py

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class ColorDialog(QtGui.QWidget):
   def __init__(self, parent=None):
       QtGui.QWidget.__init__(self, parent)
       color = QtGui.QColor(0, 0, 0)
       self.setGeometry(300, 300, 250, 180)
       self.setWindowTitle('ColorDialog')
       self.button = QtGui.QPushButton('Dialog', self)
       self.button.setFocusPolicy(QtCore.Qt.NoFocus)
       self.button.move(20, 20)
       self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
       self.setFocus()
       self.widget = QtGui.QWidget(self)
       self.widget.setStyleSheet("QWidget { background-color: %s }" % color.name())
       self.widget.setGeometry(130, 22, 100, 100)

   def showDialog(self):
       color = QtGui.QColorDialog.getColor()
       self.widget.setStyleSheet("QWidget { background-color: %s }" % color.name())

app = QtGui.QApplication(sys.argv)
cd = ColorDialog()
cd.show()
app.exec_()
```
Пример отображает кнопку и пустой виджет. Цвет вижета по умолчанию устанавливается в черный цвет. Используя QColorDialog, мы можем изменить его фон.
```
    color = QtGui.QColorDialog.getColor()
```
Эта строчка вызывает диалоговое окно QColorDialog.
```
 self.widget.setStyleSheet("QWidget { background-color: %s }"
     % color.name())
```
Тут мы изменяем фоновый цвет нашего виджета.

QFontDialog
============

Диалоговое окно QFontDialog предназначенно для выбора шрифта.
```

#!/usr/bin/python
# fontdialog.py

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class FontDialog(QtGui.QWidget):
   def __init__(self, parent=None):
       QtGui.QWidget.__init__(self, parent)
       hbox = QtGui.QHBoxLayout()
       self.setGeometry(300, 300, 250, 110)
       self.setWindowTitle('FontDialog')
       button = QtGui.QPushButton('Dialog', self)
       button.setFocusPolicy(QtCore.Qt.NoFocus)
       button.move(20, 20)
       hbox.addWidget(button)
       self.connect(button, QtCore.SIGNAL('clicked()'), self.showDialog)
       self.label = QtGui.QLabel('Knowledge only matters', self)
       self.label.move(130, 20)
       hbox.addWidget(self.label, 1)
       self.setLayout(hbox)

   def showDialog(self):
       font, ok = QtGui.QFontDialog.getFont()
       if ok:
           self.label.setFont(font)

app = QtGui.QApplication(sys.argv)
cd = FontDialog()
cd.show()
app.exec_()

```
В этом примере у нас есть метка и строчка. С помощью QFontDialog мы можеи изменить тип шрифта метки.
```
    hbox.addWidget(self.label, 1)
```
Мы создали метку с изменяемым размером. Это необходимо, так как при изменении шрифта ширина надписи может измениться. В случае если ширина станет больше, то весь тект может не поместиться в ней.
```
   font, ok = QtGui.QFontDialog.getFont()
```
Здесь мы вызываем диалоговое окно для выбора шрифта.

```
    if ok:
         self.label.setFont(font)
```
Если мы нажали Ok, то изменяем тип шрифта метки.


QFileDialog
===========
QFileDialog - диалоговое окно, которое позволяет пользователю выбирать файлы или директории. Выбранный файл может быть выбран для его открытия.
```
#!/usr/bin/python
# openfiledialog.py

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class OpenFile(QtGui.QMainWindow):
   def __init__(self, parent=None):
       QtGui.QMainWindow.__init__(self, parent)
       self.setGeometry(300, 300, 350, 300)
       self.setWindowTitle('OpenFile')
       self.textEdit = QtGui.QTextEdit()
       self.setCentralWidget(self.textEdit)
       self.statusBar()
       self.setFocus()
       exit = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
       exit.setShortcut('Ctrl+O')
       exit.setStatusTip('Open new File')
       self.connect(exit, QtCore.SIGNAL('triggered()'), self.showDialog)

       menubar = self.menuBar()
       file = menubar.addMenu('&File')
       file.addAction(exit)

   def showDialog(self):
       filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
       file=open(filename)
       data = file.read()
       self.textEdit.setText(data)
       
app = QtGui.QApplication(sys.argv)
cd = OpenFile()
cd.show()
app.exec_()
```
В этом примере мы создаем меню - виджет, где можно вводить текст, и строку состояния. В строке состояния отображается подсказка над каким действием в меню находится курсор. При выборе действия в меню, вызывается диалоговое окно QFileDialog, где мы можем выбрать файл. Содержимое файла загружается в виджет редактирования текста.

```
    class OpenFile(QtGui.QMainWindow):
    ...
            self.textEdit = QtGui.QTextEdit()
            self.setCentralWidget(self.textEdit)
```
Этот пример построен на базе виджета QMainWindow, потому что нам надо расположить централизованно текстовый редактор. Это удобно сделать с помощью QMainWindow не прибегая к помощи менеджера компоновки.

```
   filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                       '/home')
```
Мы открываем диалогове окно QFileDialog. Первый параметр метода getOpenFileName() - название окна. Второй параметр определяет рабочую директорию (дирктория которая по умолчанию будет выбрана). По умолчанию, фильтр показывает все файлы (*).

```
    file=open(filename)
    data = file.read()
    self.textEdit.setText(data)
```
Читаем выбранный файл и передаем его содержимое в виджет для редактирования текста.


Виджеты
========
Виджеты являются кубиками для построения графического приложения. В PyQt4 предоставлен широкий выбор виджетов. Кнопки, флажки, ползунки, выпадающий список и т.д. Таким образом програмист может удовлетворить все свои потребности. 

QCheckBox
-----------
QCheckBox - это переключатель, который может быть в двух состояниях: включен и выключен. Внешне он представляет собой переключатель с текстовой меткой. Когда вы включаете или выключаете переключатель, то генерируется сигнал stateChanged().


```
#!/usr/bin/python
# -*- coding: utf-8 -*-
# checkbox.py

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        cb = QtGui.QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QtGui.QCheckBox')
        self.show()
        
    def changeTitle(self, state):
      
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('QtGui.QCheckBox')
        else:
            self.setWindowTitle('')
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


```
В этом примере мы создаем переключатель, который в зависимости от того включен он или выключен, влияет на отображение заголовка окна.

```
   cb = QtGui.QCheckBox('Show title', self)
```
Это конструктор переключателя.

```
   self.cb.setFocusPolicy(QtCore.Qt.NoFocus)
```
По умолчанию, фокус наводится на переключатель. Он представляет собой тонкую линию прямоугольника вокруг переключателя. 

```
   cb.stateChanged.connect(self.changeTitle)
```
Мы соединяем наш метод changeTitle() с сигналом stateChanged(). Метод changeTitle() изменяет нам заголовок окна.

```
    self.cb.toggle();
```
По умолчанию переключатель находится в выключенном положении. Для того что бы его включить мы используем метод toggle().


ToggleButton
------------
В PyQt4 нет виджета с названием ToggleButton. Для создания этого виджета мы используем QPushButton в специальном формате. ToggleButton это кнопка которая может находиться в двух состояниях: нажата и не нажата. Вы можете переключаться кнопку из положения в положения просто щелкнув по ней. 
```

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In this example, we create three toggle buttons.
They will control the background color of a 
QtGui.QFrame. 

"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.col = QtGui.QColor(0, 0, 0)       

        redb = QtGui.QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)

        greenb = QtGui.QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QtGui.QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QtGui.QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  
            self.col.name())
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()
        
        
    def setColor(self, pressed):
        
        source = self.sender()
        
        if pressed:
            val = 255
        else: val = 0
                        
        if source.text() == "Red":
            self.col.setRed(val)                
        elif source.text() == "Green":
            self.col.setGreen(val)             
        else:
            self.col.setBlue(val) 
            
        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())  
            
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    

```

В этом примере мы создали три ToggleButton. Мы также создали QWidget. Мы сделали его фон черным. Соответственно, цвет фона меняется в зависимости от нажатия или отжатия кнопки.


```
    self.color = QtGui.QColor(0, 0, 0)
```
Это строчка инициализирует начальное значение фона. Отсуствие красного, зеленого и голубого цвета приводит к тому, что мы видим черный квадрат. Теоритически говоря, черный цвет - это отсуствие всех цветов.
```
    self.red = QtGui.QPushButton('Red', self)
    self.red.setCheckable(True)
```
Тут мы создаем togglebutton и включаем режим переключение состояния кнопки с помощью метода setCheckable().

```
   redb.clicked[bool].connect(self.setColor)

```
Связываем сигнал clicked() с нашим методом setColor.

```
         if source.text() == "Red":
            self.col.setRed(val)                
        elif source.text() == "Green":
            self.col.setGreen(val)             
        else:
            self.col.setBlue(val) 
```  
Мы проверяем, нажата или отжата кнопка, и в зависимости от этого добавляем цвет или убавляем.
```
 self.square.setStyleSheet("QWidget { background-color: %s }" % self.color.name())
```
Для изменения цвета фона, мы используем таблицу стилей.


QSlider, QLabel
---------------
QSlider - это виджет, который имеет ползунок для управления. Передвигая ползунок мы можем менять значение в большую или меньшую сторону. Таким образом мы можем задавать значения. В ряде случаев использование ползунка для определения значения является более удобным, чем установка значения вручную или с помощью списка значений. QLabel является просто текстовой или графической меткой.

В нашем примере, мы создадим один ползунок и одну графическую метку. Значение полученное через ползунок будет влиять на метку.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

This example shows a QtGui.QSlider widget.

"""

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        
        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('mute.png'))
        self.label.setGeometry(160, 40, 80, 30)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QtGui.QSlider')
        self.show()
        
    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QtGui.QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QtGui.QPixmap('min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QtGui.QPixmap('med.png'))
        else:
            self.label.setPixmap(QtGui.QPixmap('max.png'))
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
```

В этом примере мы моделируем работу регулятора громкости. Передвигая ползунок, мы меняем метку.

```
   sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
```
Мы создали горизонтальный ползунок.

```
    self.label = QtGui.QLabel(self)
    self.label.setPixmap(QtGui.QPixmap('mute.png'))
```
Мы создали QLabel. И установили значение по умолчанию файл mute.png.

```
   sld.valueChanged[int].connect(self.changeValue)
```
Мы связали сигнал valueChanged(int) с нашей функцией self.changeValue.

```
    def changeValue(self, value):
```
Мы получаем значение ползунка вызвав метод value(). В зависимости от значения меняем изображение метки.


QProgressBar
-------------
QProgressBar - это виджет, который используется, когда необходимо показать уровень выполнения задачи. Это анимированный виджет, позволяющий видеть пользователю, что задача выполняется. QProgressBar можно сделать как вертикальным, так и горизонтальным. При создании этого виджета программист должен задать минимальное и максимальное значение. По умолчанию, эти значения равны 0 и 99 соотвественно.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

This example shows a QtGui.QProgressBar widget.

"""

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QtGui.QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QtCore.QBasicTimer()
        self.step = 0
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QtGui.QProgressBar')
        self.show()
        
    def timerEvent(self, e):
      
        if self.step >= 100:
        
            self.timer.stop()
            self.btn.setText('Finished')
            return
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
      
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
            
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
```

В этом примере мы создали горизонтальный уровень выполнения задачи и кнопку. Кнопка запускает и останавливает работу уровня выполнения задачи.

```
    self.pbar = QtGui.QProgressBar(self)
```
Конструктор QProgressBar.
-------------------------

```
   self.timer = QtCore.QBasicTimer()
```
Создали объект таймера, который будет влиять на уровень выполнения задачи.

```
   self.timer.start(100, self)
```
Для запуска таймера необходимо вызвать метод start(). Этот метод получает два параметра: тайм-аут и объект, который будет получать событие о его срабатывании.

```
   def timerEvent(self, e):
      
        if self.step >= 100:
        
            self.timer.stop()
            self.btn.setText('Finished')
            return
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)
```
Каждый потомок QObject имеет обработчик события timerEvent. Для того что бы мы могли отреагировать на это событие, нам надо его переопределить в нашем объекте.

QCalendarWidget
----------------
QCalendarWidget позволяет работать с календарем. Благодаря ему пользователь может выбрать дату интуитивно понятным способом.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This example shows a QtGui.QCalendarWidget widget.

"""

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
    
    
    def initUI(self):      

        cal = QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QtCore.QDate].connect(self.showDate)
        
        self.lbl = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()
        
    def showDate(self, date):     
    
        self.lbl.setText(date.toString())
    
    
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```

В этом примере мы создали календарь и метку. Выбирая дату, мы отображаем ее в метке.

```
    cal = QtGui.QCalendarWidget(self)
```
Конструктор QCalendar.
----------------------
```
   cal.clicked[QtCore.QDate].connect(self.showDate)
```
Если пользователь выбрал дату, то посылается сигнал clicked(). Мы соединяем его с нашим методом showDate.


```
    def showDate(self, date):     
    
        self.lbl.setText(date.toString())
```
Мы получаем выбранную дату с помощью метода date.toString(). Следующим нашим шагом будет преобразование ее в строку и затем передача в метод который определяет значение метки.

Виджеты могут занимать несколько строк или столбцов и в следующем примере мы покажем это.
```
#!/usr/bin/python

import sys
from PyQt4 import QtGui

class GridLayout2(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('grid layout')

        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)
        self.resize(350, 300)

app = QtGui.QApplication(sys.argv)
qb = GridLayout2()
qb.show()
sys.exit(app.exec_())

grid = QtGui.QGridLayout()
grid.setSpacing(10)
```
Создаём раскладку таблицей и указываем расстояние между виджетами.
```
grid.addWidget(reviewEdit, 3, 1, 5, 1)
```
Если мы добавляем виджет в раскладку, мы можем указать сколько строк или столбцов он объединяет. В нашем случае reviewEdit объединяет 5 строк.

Главное окно
-------------
Класс QMainWindow представляет собой главное окно приложения. С его помощью можно создавать классический вид со строкой состояния, панелями инструментов и меню.

Строка состояния
----------------
Строка состояния это виджет, который используется для отображения статусной информации.
```
#!/usr/bin/python

import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('statusbar')

        self.statusBar().showMessage('Ready')

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())


self.statusBar().showMessage('Ready')
```
Чтобы создать строку состояния мы вызываем метод statusBar() класса QApplication. ShowMessage() показывает сообщение на строке состояния.

Меню
====
Меню это один из самых видных частей GUI приложения. Это группа команд расположенных в различных меню. Тогда как в консольных приложениях вам необходимо помнить все тайные команды, здесь вам доступно большинство команд сгруппированных логически. Это принятый стандарт, который уменьшает время на изучение нового приложения.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
menu.py

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

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    

```
self.statusBar().showMessage('Ready')

Во-первых, мы создаём меню c помощью метода menuBar() класса QMainWindow. Затем, используя метод addMenu(), добавляем пункт меню File, после чего подключаем объект exit к созданному пункту.

Панель инструментов
====================
Меню объединяет все команды, которые мы можем использовать в приложении. Панели инструментов, в свою очередь, предоставляют быстрый доступ к наиболее часто употребляемым командам.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
toolbar.py

In this example, we create a simple
window in PyQt4.

"""
import sys, os
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        exitAction = QtGui.QAction(QtGui.QIcon(os.getcwd() + "/icons/web.png"), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

```
GUI приложения управляются командами, и эти команды могут быть запущены из меню, контекстного меню, панели инструментов или с помощью горячих клавиш. PyQt упрощает разработку с введением действий (actions). Объект action может иметь текст меню, иконку, ярлык (клавиатурное сочетание), статусный текст, текст «What's This?» и всплывающую подсказку. В нашем примере мы определим объект action с иконкой, ярлыком и всплывающей подсказкой.
self.connect(self.exit, QtCore.SIGNAL('triggered()'),
QtCore.SLOT('close()'))

Здесь мы соединяем сигнал triggered() объекта action с предопределённым сигналом close().
self.toolbar = self.addToolBar('Exit')
self.toolbar.addAction(self.exit)

Создаём панель инструментов и устанавливаем на неё объект action.
# Панель инструментов

# Совмещаем вместе
В поседнем примере, мы создадим окно и расположим на нём меню, панель инструментов и статусную строку, а также добавим центральный виджет.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
mainw.py
"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys, os
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QtGui.QAction(QtGui.QIcon(os.getcwd() + "/icons/close.png"), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

```
Здесь мы создаём виджет QtextEdit, который устанавливаем центральным на QMainWindow. Центральный виджет занимает все свободное пространство.

edit.py
```
import sys, time
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore

class Prog(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setWindowTitle('grid layout')

        #Craete line and text area
        self.Line = QtGui.QLabel('Line')
        self.Text = QtGui.QLabel('Text')

        self.LineEdit = QtGui.QLineEdit()
        self.TextEdit = QtGui.QTextEdit()
        
        #checkered layout, 5 - cell spacing
        grid = QtGui.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.Line, 1, 0) #1 and 0 - coordinates
        grid.addWidget(self.LineEdit, 1, 1)

        grid.addWidget(self.Text, 3, 0)
        grid.addWidget(self.TextEdit, 3, 1, 5, 1) # 5,1 - number of columns and cells

        self.setLayout(grid)
        
        #dialog window
        self.button = QtGui.QPushButton('editLine', self)
        grid.addWidget(self.button, 12, 1)
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.editLine)
        
        self.resize(350, 300)
    

    def editLine(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input in line', 'Enter string:')

        if ok:
            self.LineEdit.setText(text)
    
app = QtGui.QApplication(sys.argv)
prog = Prog()
prog.show()
sys.exit(app.exec_())
```
