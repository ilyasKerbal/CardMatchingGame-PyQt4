# Developer  : ILYAS KERBAL
# Github: https://github.com/ilyasKerbal
# Email: kerbalsc@gmail.com

from PyQt4 import QtGui, QtCore
from.cardgroup import CardGroup
import datetime
import time

class InterfaceUI(QtGui.QWidget):
    def __init__(self, level, cat):
        super(InterfaceUI,self).__init__()
        self.level = level
        self.cat = cat
        self.gameStart = False
        self.gameOver = False
        self.updateLayout()

        self.cardCouple = []

        self.startTime = datetime.datetime(2016,1,11,0,0,0,0)
        self.delta = datetime.timedelta(seconds=1)
        self.qtimer =  QtCore.QTimer()
        self.qtimer.timeout.connect(self.updateTimer)

    def setLevel(self, level2, cat):
        self.level = level2
        self.clearLayout(self.mediumLayout0)
        self.clearLayout(self.mediumLayout1)
        self.clearLayout(self.mediumLayout2)
        self.clearLayout(self.finalLayout)
        self.cat = cat
        QtGui.QWidget().setLayout(self.layout())
        self.updateLayout()

    def updateLayout(self):
        #Interface Components
        self.startBtn = QtGui.QPushButton("Start")
        self.stopBtn = QtGui.QPushButton("Stop")
        self.stopBtn.setEnabled(False)
        self.gameOver = False

        self.gameStart = False
        self.cardCouple = []

        #Start and Stop Buttons
        self.startBtn.clicked.connect(self.start)
        self.stopBtn.clicked.connect(self.stop)

        self.timer = QtGui.QLabel("Timer: 00:00:00")
        self.timer.setFont(QtGui.QFont("SansSerif",20))

        self.successfulHints = QtGui.QLabel("Successful: 0")
        self.successfulHints.setFont(QtGui.QFont("SansSerif", 20))
        self.successful = 0

        self.unsuccessfulHints = QtGui.QLabel("Hints: 0")
        self.unsuccessfulHints.setFont(QtGui.QFont("SansSerif", 20))
        self.unsuccessful = 0

        self.finalLayout = QtGui.QVBoxLayout(self)
        self.mediumLayout0 = QtGui.QHBoxLayout()
        self.mediumLayout1 = QtGui.QVBoxLayout()
        self.mediumLayout2 = QtGui.QHBoxLayout()

        if self.level == "Easy":
            self.endGame = 6
        else:
            self.endGame = 9

        #Game Grid
        self.grid = CardGroup(self.cat,self.level)

        #Init Components
        self.startBtn.setIcon(QtGui.QIcon(":package/assets/img/timer.png"))
        self.stopBtn.setIcon(QtGui.QIcon(":package/assets/img/stop.png"))
        self.mediumLayout1.addStretch()
        self.mediumLayout1.addWidget(self.startBtn)
        self.mediumLayout1.addWidget(self.stopBtn)
        self.mediumLayout1.addStretch()
        self.timer.setStyleSheet('color: blue')
        self.successfulHints.setStyleSheet('color: green')
        self.unsuccessfulHints.setStyleSheet('color: red')
        self.mediumLayout2.addWidget(self.timer)
        self.mediumLayout2.addStretch()
        self.mediumLayout2.addWidget(self.successfulHints)
        self.mediumLayout2.addStretch()
        self.mediumLayout2.addWidget(self.unsuccessfulHints)

        self.mediumLayout0.addLayout(self.mediumLayout1)
        self.mediumLayout0.addLayout(self.grid)
        self.finalLayout.addLayout(self.mediumLayout0)
        self.finalLayout.addLayout(self.mediumLayout2)
        self.setLayout(self.finalLayout)

    def clearLayout(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)

            if isinstance(item, QtGui.QWidgetItem):
                item.widget().close()
                # or
                # item.widget().setParent(None)
            elif isinstance(item, QtGui.QSpacerItem):
                pass
                # no need to do extra stuff
            else:
                self.clearLayout(item.layout())

            # remove the item from layout
            layout.removeItem(item)
    def start(self, evnet):
        if not(self.gameStart) and not self.gameOver:
            self.gameStart = True
            self.stopBtn.setEnabled(True)
            self.timer.setText("Timer: 00:00:00")
            self.successfulHints.setText("Successful: 0")
            self.unsuccessfulHints.setText("Hints: 0")
            self.deltaTime = datetime.time(0, 0, 0)
            self.qtimer.start(1000)
            self.startBtn.setEnabled(False)
            self.gameStart = True
    def stop(self, event):
        if self.gameStart:
            self.gameStart = False
            self.stopBtn.setEnabled(False)
            self.startBtn.setEnabled(True)
            self.startTime = datetime.datetime(2016, 1, 11, 0, 0, 0, 0)
            self.qtimer.stop()
            self.gameStart = False
            self.gameOver = True
    def updateTimer(self):
        if self.gameStart:
            self.startTime += self.delta
            self.timer.setText("Timer: {}".format(self.startTime.time()))
    def cardClicked(self, card):
        if (not self.gameOver) and self.gameStart and card.flip:
            card.setPixmap(QtGui.QPixmap(card.img))
            card.flip = False
            if(len(self.cardCouple) == 0):
                self.cardCouple.append(card)
                card.setEnabled(False)
            else:
                if((card.number == self.cardCouple[0].number) and not card is self.cardCouple[0] ):
                    card.setEnabled(False)
                    self.cardCouple[0].setEnabled(False)
                    self.successful += 1
                    del self.cardCouple[:]
                    self.updateResult()
                elif card.number != self.cardCouple[0].number:
                    card.flipCard()
                    self.cardCouple[0].flipCard()
                    if not card is self.cardCouple[0]:
                        self.unsuccessful += 1
                    self.updateResult()
                    card.setEnabled(True)
                    self.cardCouple[0].setEnabled(True)
                    del self.cardCouple[:]
    def updateResult(self):
        self.successfulHints.setText("Successful: {}".format(self.successful))
        self.unsuccessfulHints.setText("Hints: {}".format(self.unsuccessful))

        if(self.successful == self.endGame):
            self.gameOver = True
            self.stop(None)
            self.grid.showAll()

