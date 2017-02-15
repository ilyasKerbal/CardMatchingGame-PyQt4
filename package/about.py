from PyQt4 import QtCore
from PyQt4 import QtGui

class About(QtGui.QDialog):
    def __init__(self):
        super(About, self).__init__()
        self.img = QtGui.QLabel()
        self.devName = QtGui.QLabel("ILYAS KERBAL")
        self.devEmail = QtGui.QLabel("<a href='mailto:kerbalsc@gmail.com'>kerbalsc@gmail.com</a>")
        self.devHub = QtGui.QLabel("<a href='https://github.com/ik1730'>Github: https://github.com/ik1730</a>")
        self.btn = QtGui.QPushButton("Go Back")
        self.box = QtGui.QVBoxLayout()
        self.palette = QtGui.QPalette()
        self.setUI()


    def setUI(self):
        self.setWindowIcon(QtGui.QIcon(":package/assets/img/about2.png"))
        self.setWindowTitle("About")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.img.setPixmap(QtGui.QPixmap(":package/assets/img/profile.png"))
        self.box.addWidget(self.img)
        self.box.addWidget(self.devName)
        self.box.addWidget(self.devEmail)
        self.box.addWidget(self.devHub)
        self.box.addWidget(self.btn)
        self.box.setAlignment(QtCore.Qt.AlignCenter)
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.devName.setAlignment(QtCore.Qt.AlignCenter)
        self.devEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.devHub.setAlignment(QtCore.Qt.AlignCenter)
        self.btn.clicked.connect(self.close)
        self.setLayout(self.box)
        self.setFixedSize(350,250)
        self.palette.setColor(self.backgroundRole(), QtCore.Qt.white)
        self.setPalette(self.palette)
        self.center()
        self.exec_()
    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())