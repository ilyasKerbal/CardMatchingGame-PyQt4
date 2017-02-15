from PyQt4 import QtCore
from PyQt4 import QtGui

class Level(QtGui.QDialog):
    def __init__(self, level):
        super(Level, self).__init__()
        self.img = QtGui.QLabel()
        self.msg = QtGui.QLabel("Please, Choose your level ?")
        self.btn = QtGui.QPushButton("Go Back")
        self.box = QtGui.QVBoxLayout()
        self.cb = QtGui.QComboBox()
        self.level = level

        self.setUI()

    def setUI(self):
        self.cb.addItems(["Easy", "Hard"])
        if(self.level == "Easy"):
            self.cb.setCurrentIndex(0)
        else:
            self.cb.setCurrentIndex(1)

        self.cb.currentIndexChanged.connect(self.selectionChanged)
        self.setWindowIcon(QtGui.QIcon(":package/assets/img/settings2.png"))
        self.setWindowTitle("About")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.img.setPixmap(QtGui.QPixmap(":package/assets/img/settings2.png"))
        self.box.addWidget(self.img)
        self.box.addWidget(self.msg)
        self.box.addWidget(self.cb)
        self.box.addWidget(self.btn)
        self.box.setAlignment(QtCore.Qt.AlignCenter)
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.btn.clicked.connect(self.close)
        self.setLayout(self.box)
        self.setFixedSize(300,200)
        self.center()
        self.exec_()
    def selectionChanged(self,i):
        if i == 0:
            self.level = "Easy"
        else:
            self.level = "Hard"
    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())