'''
Created on 24/07/2013

@author: xtreme
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nivel.ui'
#
# Created: Fri Jul 19 12:14:27 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui
from qtablero import Ui_QTablero

#import images
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_nivel(QtGui.QMainWindow):
    def setupUi(self, nivel):
        nivel.setObjectName(_fromUtf8("nivel"))
        nivel.resize(400, 295)
        self.pushButton = QtGui.QPushButton(nivel)
        self.pushButton.setGeometry(QtCore.QRect(50, 210, 60, 60))
        self.pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./images/visto.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(nivel)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 210, 60, 60))
        self.pushButton_2.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./images/x.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.facil = QtGui.QRadioButton(nivel)
        self.facil.setGeometry(QtCore.QRect(200, 120, 82, 17))
        self.facil.setChecked(True)
        self.facil.setObjectName(_fromUtf8("facil"))
        self.medio = QtGui.QRadioButton(nivel)
        self.medio.setGeometry(QtCore.QRect(200, 150, 82, 17))
        self.medio.setObjectName(_fromUtf8("medio"))
        self.dificil = QtGui.QRadioButton(nivel)
        self.dificil.setGeometry(QtCore.QRect(200, 180, 82, 17))
        self.dificil.setObjectName(_fromUtf8("dificil"))
        self.label = QtGui.QLabel(nivel)
        self.label.setGeometry(QtCore.QRect(60, 60, 71, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.nombretexto = QtGui.QLineEdit(nivel)
        self.nombretexto.setGeometry(QtCore.QRect(160, 60, 191, 20))
        self.nombretexto.setObjectName(_fromUtf8("nombretexto"))
        self.label_2 = QtGui.QLabel(nivel)
        self.label_2.setGeometry(QtCore.QRect(60, 122, 101, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.abrirEntrar) 
        self.retranslateUi(nivel)
        QtCore.QMetaObject.connectSlotsByName(nivel)
        
    def abrirEntrar(self):
        d=1
        if self.facil.isChecked():
            d=1
        if self.medio.isChecked():
            d=2
        if self.dificil.isChecked():
            d=3
        qtablero = QtGui.QMainWindow()
        ui1 = Ui_QTablero()
        ui1.dif=d
        ui1.nombre=self.nombretexto.text()
        ui1.setupUi(qtablero)
        nivel.setVisible(False)
        qtablero.show()
        ui1.exec_() 

    def retranslateUi(self, nivel):
        nivel.setWindowTitle(_translate("nivel", "Juego Nuevo", None))
        self.facil.setText(_translate("nivel", "facil", None))
        self.medio.setText(_translate("nivel", "medio", None))
        self.dificil.setText(_translate("nivel", "dificikl", None))
        self.label.setText(_translate("nivel", "<html><head/><body><p><span style=\" font-size:12pt;\">Jugador:</span></p></body></html>", None))
        self.nombretexto.setText(_translate("nivel", "nombre del jugador", None))
        self.label_2.setText(_translate("nivel", "<html><head/><body><p><span style=\" font-size:12pt;\">Dificultad</span></p></body></html>", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    nivel = QtGui.QMainWindow()
    ui = Ui_nivel()
    ui.setupUi(nivel)
    nivel.show()
    sys.exit(app.exec_())

