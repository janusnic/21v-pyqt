# 21v-pyqt

Tetris
=======


#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, random
from PyQt4 import QtCore, QtGui

Фигуры перемещаются по принципу «кубик за кубиком» (не «пиксель за пикселем»).

Математически, доска – это просто список чисел.

Код содержит четыре класса: Tetris, Board, Tetrominoe и Shape. 

Класс Tetris организовывает игру.
---------------------------------
Игра начинается сразу же после её запуска. Мы можем приостановить игру, нажимая клавишу p. Клавиша Space будет немедленно бросать блок тетриса на дно. Игра идёт на постоянной скорости, ускорение не реализуется. 
```
class Tetris(QtGui.QMainWindow):
    
    def __init__(self):
        super(Tetris, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):    
        
        # Экземпляр класса Board создаётся и устанавливается так, чтобы быть центральным виджетом приложения.
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        # создаём строку состояния, где мы будем отображать сообщения. Мы будем отображать три возможных сообщения: количество уже удалённых линий, сообщение паузы, или сообщение «Игра окончена». msgStatusbar – это пользовательский сигнал, который реализуется в классе Board. showMessage() – это встроенный метод, который отображает сообщение в строке состояния.

        self.statusbar = self.statusBar()        
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        
        # Эта строка инициирует игру.
        self.tboard.start()
        
        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')        
        self.show()
        

    def center(self):
        
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)
```

Класс Board – это то, где пишется игровая логика. 
-------------------------------------------------
```
class Board(QtGui.QFrame):
    
    # Создаётся пользовательский сигнал. msgStatusbar – это сигнал, который срабатывает, когда мы хотим написать сообщение или очки в строку состояния.

    msg2Statusbar = QtCore.pyqtSignal(str)
    
    # Это переменные класса Board. BoardWidth и BoardHeight определяют размер доски в блоках. Speed определяет скорость игры. Каждые 300 мс будет начинаться цикл новой игры.

    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        super(Board, self).__init__(parent)
        
        self.initBoard()
        
        
    def initBoard(self):     

        # используем QtCore.QBasicTimer(), чтобы создать игровой цикл.
        self.timer = QtCore.QBasicTimer()
        self.isWaitingAfterLine = False
        
        # В методе initBoard() мы инициализируем несколько важных переменных. Переменная self.board – это список чисел от 0 до 7. Она представляет местоположение различных фигур и оставляет фигуры на доске.

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()
        
        
    # Метод shapeAt() определяет тип фигуры в данном блоке.


    def shapeAt(self, x, y):
        return self.board[(y * Board.BoardWidth) + x]

        
    def setShapeAt(self, x, y, shape):
        self.board[(y * Board.BoardWidth) + x] = shape
        

    # Доска может динамически менять размер. Как следствие, размер блока может меняться. squareWidth() вычисляет ширину простого квадратика в пикселях и возвращает её. Board.BoardWidth – это размер доски в блоках.

    def squareWidth(self):
        return self.contentsRect().width() / Board.BoardWidth
        

    def squareHeight(self):
        return self.contentsRect().height() / Board.BoardHeight
        

    def start(self):
        
        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.newPiece()
        self.timer.start(Board.Speed, self)

        
    def pause(self):
        
        if not self.isStarted:
            return

        self.isPaused = not self.isPaused
        
        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("paused")
            
        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.update()

        
    def paintEvent(self, event):
        
        painter = QtGui.QPainter(self)
        rect = self.contentsRect()

        
        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        # Рисование игры разделяется на два шага. Первым шагом, мы рисуем все фигуры, или оставляем фигуры, которые были сброшены на дно доски. Все квадратики запоминаются в списке переменных self.board. Доступ к переменной получают, используя метод shapeAt().

        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)
                
                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,
                        rect.left() + j * self.squareWidth(),
                        boardTop + i * self.squareHeight(), shape)

        # Следующий шаг – это рисование упавших вниз частей.
        if self.curPiece.shape() != Tetrominoe.NoShape:
            
            for i in range(4):
                
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                    boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                    self.curPiece.shape())

                    
    # В методе keyPressEvent(), мы проверяем нажатые клавиши. Если мы нажали клавишу правой стрелки, мы пробуем передвинуть часть вправо. Мы говорим «пробуем», поскольку часть может быть не способна перемещаться.

    def keyPressEvent(self, event):
        
        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()
        
        if key == QtCore.Qt.Key_P:
            self.pause()
            return
            
        if self.isPaused:
            return
                
        elif key == QtCore.Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)
            
        elif key == QtCore.Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)
            
        elif key == QtCore.Qt.Key_Down:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
            
        # Клавиша стрелки вверх будет поворачивать падающую часть влево.
        elif key == QtCore.Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
            
        # Клавиша «Пробел» будет немедленно бросать падающую часть на дно.
        elif key == QtCore.Qt.Key_Space:
            self.dropDown()
            
        # Нажимая клавишу «d», часть спустится вниз на один блок. Это может быть использовано, чтобы слегка ускорить падение части.

        elif key == QtCore.Qt.Key_D:
            self.oneLineDown()
            
        else:
            super(Board, self).keyPressEvent(event)
                

    # В событии таймера, мы либо создаём новую часть после предыдущей части, что упала на дно, либо мы передвигаем падающую часть на одну линию вниз.

    def timerEvent(self, event):
        
        if event.timerId() == self.timer.timerId():
            
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()
                
        else:
            super(Board, self).timerEvent(event)

            
    # Метод clearBoard() очищает доску путём установки Tetrominoe.Noshape на каждый блок доски.


    def clearBoard(self):
        
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)

        
    def dropDown(self):
        
        newY = self.curY
        
        while newY > 0:
            
            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break
                
            newY -= 1

        self.pieceDropped()
        

    def oneLineDown(self):
        
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()
            

    def pieceDropped(self):
        
        for i in range(4):
            
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()
            

    # Если часть ударяет дно, мы вызываем метод removeFullLines(). Мы обнаруживаем все полные линии и удаляем их. Мы делаем это, передвигая все линии выше на текущую полную линию, что удаляется на одну линию вниз. Обратите внимание, что мы развернули порядок удаляемых линий. В противном случае, это не будет работать правильно. В нашем случае, мы используем нехитрую гравитацию. Это означает, что части могут парить над пустыми промежутками.

    def removeFullLines(self):
        
        numFullLines = 0
        rowsToRemove = []

        for i in range(Board.BoardHeight):
            
            n = 0
            for j in range(Board.BoardWidth):
                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1

            if n == 10:
                rowsToRemove.append(i)

        rowsToRemove.reverse()
        

        for m in rowsToRemove:
            
            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                        self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:
            
            self.numLinesRemoved = self.numLinesRemoved + numFullLines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))
                
            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.update()
            

    # Метод newPiece() случайным образом создаёт новую часть тетриса. Если часть не может прийти в свою начальную позицию, игра заканчивается.

    def newPiece(self):
        
        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth / 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()
        
        #print self.curY

        if not self.tryMove(self.curPiece, self.curX, self.curY):
            
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")



    # В методе tryMove(), мы пробуем переместить наши фигуры. Если фигура находится на краю доски или примыкает к некоторой другой части, мы возвращаем значение «Ложь». В противном случае, мы перемещаем текущую падающую часть в новую позицию.

    def tryMove(self, newPiece, newX, newY):
        
        for i in range(4):
            
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)
            
            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False
                
            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()
        
        return True
        

    def drawSquare(self, painter, x, y, shape):
        
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QtGui.QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, 
            self.squareHeight() - 2, color)

        painter.setPen(color.light())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.dark())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
            x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1, 
            y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)

```
Класс Tetrominoe содержит имена всех частей тетриса
---------------------------------------------------
Класс Tetrominoe содержит в себе имена всех возможных фигур. Мы также имеем NoShape для пустого пространства. 

```
class Tetrominoe(object):
    
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7
```
Класс Shape содержит код для частей тетриса.
--------------------------------------------
![Рисунок: Координаты](coordinates.png)
Format: ![Рисунок: Координаты](url)
Для примера, набор (0, -1), (0, 0), (-1, 0), (-1, -1) представляет Z-фигуру. Схема иллюстрирует фигуру.

```
# Набор coordsTable содержит в себе все возможные значения координат наших частей тетриса. Это шаблон, из которого все части берут свои значения координат.

class Shape(object):
    
    coordsTable = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
    )

    def __init__(self):
        
        # После создания, мы создаём пустой список координат. Список будет хранить координаты частей тетриса.

        self.coords = [[0,0] for i in range(4)]
        self.pieceShape = Tetrominoe.NoShape

        self.setShape(Tetrominoe.NoShape)
        

    def shape(self):
        return self.pieceShape
        

    def setShape(self, shape):
        
        table = Shape.coordsTable[shape]
        
        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.pieceShape = shape
        

    def setRandomShape(self):
        self.setShape(random.randint(1, 7))

        
    def x(self, index):
        return self.coords[index][0]

        
    def y(self, index):
        return self.coords[index][1]

        
    def setX(self, index, x):
        self.coords[index][0] = x

        
    def setY(self, index, y):
        self.coords[index][1] = y

        
    def minX(self):
        
        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m

        
    def maxX(self):
        
        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m

        
    def minY(self):
        
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m

        
    def maxY(self):
        
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m

        
    # Метод rotateLeft() поворачивает часть влево. Квадрат не должен поворачиваться. Вот почему мы просто возвращаем ссылку на текущий объект. Новая часть создаётся и её координаты устанавливаются в одну из повернутых частей.

    def rotateLeft(self):
        
        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape
        
        for i in range(4):
            
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result

        
    def rotateRight(self):
        
        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape
        
        for i in range(4):
            
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result


def main():
    
    app = QtGui.QApplication([])
    tetris = Tetris()    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```