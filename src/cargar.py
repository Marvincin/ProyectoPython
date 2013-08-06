# -*- coding: utf-8 -*-
'''
Created on 30/07/2013

@author: xtreme
'''


# Form implementation generated from reading ui file 'cargar.ui'
#
# Created: Tue Jul 30 23:14:45 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import base64
from qtablero import Ui_QTablero





try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
    


class Ui_Dialog(QtGui.QMainWindow):
    
            
    def setupUi(self, Dialog):
        self.list=[]
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 292)
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(0, -10, 401, 311))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/Sudoku.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("./images/Sudoku.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("./images/Sudoku.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("./images/Sudoku.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(407, 159))
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 221, 30))
        self.comboBox.setObjectName("comboBox")
        list=[]
        self.cargar(list)
        self.comboBox.clear()
        i=0
        while i < len(list):
            self.comboBox.addItem(list[i])
            i=i+1  
        
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 301, 31))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 230, 81, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/visto1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"),self.abrirEntrar)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 230, 81, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.puntaje=0
        self.Min=0
        self.Seg=0
        self.connect(self.pushButton_2,QtCore.SIGNAL('clicked()'),QtGui.qApp, QtCore.SLOT('quit()'))
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        
    def abrirEntrar(self):
        Nombre=self.comboBox.currentText()
        ListaCom=[]
        ListaU=[]
        
        habilitados=[]
        self.desencriptar(Nombre, ListaCom, ListaU, habilitados)
        qtablero = QtGui.QMainWindow()
        ui1 = Ui_QTablero()
        print( Nombre, self.Min, self.Seg, self.puntaje)
        ui1.setupUiCargar(qtablero, Nombre, ListaCom, ListaU, self.Min, self.Seg, self.puntaje, habilitados)
        self.setVisible(False)
        qtablero.show()
        ui1.exec_() 
        
        
    def cargar(self,lista):
        f=open("./save/jugadores.txt","r")

        for line in f:
            lista.append(line)

            
    def desencriptar(self,Nombre, ListaCom, ListaU, habilitados):
            Nombre = Nombre.split('\n')
            f=open("./save/"+Nombre[0]+".txt","r")
            bandera=0
            bandera2=0
            j=9
            contador=0
            for line in f:
                if contador==0:
                    Nombre = base64.decodestring(line)
                   
                if contador==1:
                    self.puntaje = line
                    
                if contador==2:
                    self.Min = line
                    
                if contador==3:
                    self.Seg = line
                   
                if contador>3 and contador < 85:
                    if j==9:
                        list2=[]
                        j=0
                    numero = base64.decodestring(line)
                    list2.append(numero)
                    if j==8:
                        ListaCom.append(list2)
                    j=j+1
                if contador>84 and contador<166:
                
                    
                    if contador==166:
                        h=0
                        while h<9:
                            i=0
                            while i<9:
                                valor=ListaU[h][i]
                                print valor.text()
                                i=i+1
                            h=h+1
                    
                    if j==9:
                        list2=[]
                        j=0
                    numero = base64.decodestring(line)
                    list2.append(str(numero))
                    if j==8:
                        habilitados.append(list2)
                    j=j+1
                if contador>165: 
                    if j==9:
                        list2=[]
                        j=0
                    numero = base64.decodestring(line)
                    numeronew = QtGui.QLineEdit(numero)
                    list2.append(numeronew)
                    if j==8:
                        ListaU.append(list2)
                    j=j+1
                contador=contador+1
            
    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Partidas guardadas", None))
        self.label_2.setText(_translate("Dialog", "Seleccione su partida guardada", None))
        self.pushButton.setText(_translate("Dialog", "Aceptar", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar", None))
        
        



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

