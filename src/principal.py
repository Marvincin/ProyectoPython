
# -*- coding: utf-8 -*-
'''
Created on 24/07/2013

@author: xtreme
'''


# Form implementation generated from reading ui file 'principal.ui'
#
# Created: Fri Jul 19 08:41:26 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui
from qtablero import Ui_nivel
from cargar import Ui_Dialog
import sys
#import images 




try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_principal(QtGui.QMainWindow):
    def setupUi(self, principal):
        principal.setObjectName("principal")
        principal.resize(400, 300)
        self.imagen = QtGui.QPushButton(principal)
        self.imagen.setGeometry(QtCore.QRect(-6, -8, 411, 311))
        self.imagen.setText("")
        icon = QtGui.QIcon("./images/ININ.png")
        icon.addPixmap(QtGui.QPixmap("./images/ININ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imagen.setIcon(icon)
        self.imagen.setIconSize(QtCore.QSize(400, 300))
        self.imagen.setObjectName("imagen")
        self.pushButton = QtGui.QPushButton(principal)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 91, 51))
        
        
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(principal)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 60, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtGui.QPushButton(principal)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 240, 121, 41))
    
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4 = QtGui.QPushButton(principal)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 150, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.retranslateUi(principal)
        QtCore.QMetaObject.connectSlotsByName(principal)
        self.connect(self.pushButton_3,QtCore.SIGNAL('clicked()'),QtGui.qApp, QtCore.SLOT('quit()'))
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.abrirEntrar)
        self.connect(self.pushButton_2,  QtCore.SIGNAL("clicked()"), self.cargarpartida)
        #self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.close)
        
        
     
        
    def abrirEntrar(self):
        nivel = QtGui.QMainWindow()
        ui1 = Ui_nivel()
        ui1.setupUi(nivel)
        principal.setVisible(False)
        nivel.show()
        ui1.exec_() 
        
    def cargarpartida(self):
        cargar = QtGui.QMainWindow()
        ui2 = Ui_Dialog()
        ui2.setupUi(cargar)
        principal.setVisible(False)
        cargar.show()
        ui2.exec_() 
        
    def retranslateUi(self, principal):
        principal.setWindowTitle(_translate("principal", "sudoku", None))
        self.pushButton.setText(_translate("principal", "Jugar", None))
        self.pushButton_2.setText(_translate("principal", "Cargar Partida", None))
        self.pushButton_3.setText(_translate("principal", "Salir", None))
        self.pushButton_4.setText(_translate("principal", "Mejores Puntajes", None))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    principal = QtGui.QMainWindow()
    ui = Ui_principal()
    ui.setupUi(principal)
    principal.show()
    sys.exit(app.exec_())

