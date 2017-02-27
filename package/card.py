# Developer  : ILYAS KERBAL
# Github: https://github.com/ilyasKerbal
# Email: kerbalsc@gmail.com

from PyQt4 import QtGui
import time
class Card(QtGui.QLabel):
    default = ":package/assets/img/cards/default.png"

    def __init__(self,number, cat, flip = False):
        super(Card,self).__init__()
        self.number = number
        self.cat = cat
        self.img = ":package/assets/img/cards/{}/{}.png".format(cat,number)
        self.flip = flip

        if flip:
            self.setPixmap(QtGui.QPixmap(Card.default))
        else:
            self.setPixmap(QtGui.QPixmap(self.img))

    def mouseReleaseEvent(self, event):
            self.parent().cardClicked(self)
    def flipCard(self):
        if(self.flip):
            self.setPixmap(QtGui.QPixmap(self.img))
            self.flip = False
        else:
            self.setPixmap(QtGui.QPixmap(Card.default))
            self.flip = True