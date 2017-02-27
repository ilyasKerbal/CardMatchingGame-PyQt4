import sys
from PyQt4 import QtCore, QtGui
from .about import About
from .level import Level
from .interfaceUI import InterfaceUI
from random import shuffle
import time
from images import *
#to solve the problem of the missing QString
try:
    from PyQt4.QtCore import QString
except ImportError:
    QString = str



class MainInterface(QtGui.QMainWindow):
    def __init__(self):
        super(MainInterface,self).__init__()
        self.tb = self.addToolBar("Main")

        #Game Properties
        self.cardCategories = ["celebs", "cities", "football", "tennis"]
        shuffle(self.cardCategories)
        shuffle(self.cardCategories)
        self.category = self.cardCategories[0]
        self.level = "Hard"  # Easy Or Hard

        #Interface UI
        self.interface = InterfaceUI(self.level,self.category)

        #Init Action
        self.restart =  QtGui.QAction(QtGui.QIcon(":package/assets/img/restart.png"), "New", self)
        self.settings = QtGui.QAction(QtGui.QIcon(":package/assets/img/settings.png"), "Settings", self)
        self.about = QtGui.QAction(QtGui.QIcon(":package/assets/img/about.png"), "About", self)
        self.exit = QtGui.QAction(QtGui.QIcon(":package/assets/img/exit.png"), "Exit", self)

        self.setUI()

    def setUI(self):
        self.center() #center the screen
        self.setWindowIcon(QtGui.QIcon(":package/assets/img/logo.png")) #Set Window Icon

        #Set Actions
        self.tb.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tb.addAction(self.restart)
        self.tb.addAction(self.settings)
        self.tb.addAction(self.about)
        self.tb.addAction(self.exit)

        #Set Signals and Slots
        self.tb.actionTriggered[QtGui.QAction].connect(self.tbAction)

        self.setWindowTitle("Card Matching") #Set Window Title
        self.setCentralWidget(self.interface)
        self.setFixedSize(QtCore.QSize(732, 557))

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self,"Message","Are you sure you want to exit the game?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def tbAction(self,a):
        if a.text() == "Exit":
            self.close() #close the window
        elif a.text() == "About":
            about = About()
            about.close()
        elif a.text() == "Settings":
            settings = Level(self.level)

            if settings.level != self.level:
                self.level = settings.level
                shuffle(self.cardCategories)
                self.category = self.cardCategories[0]
                self.interface.stop(None)
                self.interface.setLevel(self.level, self.category)
            settings.close()
        elif a.text() == "New":
            shuffle(self.cardCategories)
            self.interface.stop(None)
            self.category = self.cardCategories[0]
            self.interface.setLevel(self.level, self.category)



def run():
    app = QtGui.QApplication(sys.argv)
    QtGui.QApplication.setApplicationName("Card Matching")
    QtGui.QApplication.setApplicationVersion("1.0")
    start = time.time()

    #SplashScreen
    splash = QtGui.QSplashScreen(QtGui.QPixmap(":package/assets/img/splashScreen.png"), QtCore.Qt.WindowStaysOnTopHint)
    splash.show()
    while time.time() - start < 4:
        time.sleep(0.001)
        app.processEvents()

    interface = MainInterface()
    interface.show()

    splash.finish(interface)

    sys.exit(app.exec_())