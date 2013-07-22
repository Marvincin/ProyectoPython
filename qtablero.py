# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtablero.ui'
#
# Created: Fri Jul 19 08:20:15 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from tkinter import *
import random
from copy import deepcopy
import time


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

class Ui_QTablero(object):





    def setupUi(self, QTablero):
        QTablero.setObjectName(_fromUtf8("QTablero"))
        QTablero.resize(750, 522)
        QTablero.setAcceptDrops(True)
        self.centralWidget = QtGui.QWidget(QTablero)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 151, 121))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.celda1 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.celda1.setMargin(0)
        self.celda1.setObjectName(_fromUtf8("celda1"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(310, 440, 431, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(540, 0, 201, 71))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(190, 20, 151, 121))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.celda2 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.celda2.setMargin(0)
        self.celda2.setObjectName(_fromUtf8("celda2"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(360, 20, 151, 121))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.celda3 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.celda3.setMargin(0)
        self.celda3.setObjectName(_fromUtf8("celda3"))
        self.gridLayoutWidget_5 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(20, 160, 151, 121))
        self.gridLayoutWidget_5.setObjectName(_fromUtf8("gridLayoutWidget_5"))
        self.celda4 = QtGui.QGridLayout(self.gridLayoutWidget_5)
        self.celda4.setMargin(0)
        self.celda4.setObjectName(_fromUtf8("celda4"))
        self.gridLayoutWidget_6 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(190, 160, 151, 121))
        self.gridLayoutWidget_6.setObjectName(_fromUtf8("gridLayoutWidget_6"))
        self.celda5 = QtGui.QGridLayout(self.gridLayoutWidget_6)
        self.celda5.setMargin(0)
        self.celda5.setObjectName(_fromUtf8("celda5"))
        self.gridLayoutWidget_7 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(360, 160, 151, 121))
        self.gridLayoutWidget_7.setObjectName(_fromUtf8("gridLayoutWidget_7"))
        self.celda6 = QtGui.QGridLayout(self.gridLayoutWidget_7)
        self.celda6.setMargin(0)
        self.celda6.setObjectName(_fromUtf8("celda6"))
        self.gridLayoutWidget_8 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(20, 300, 151, 121))
        self.gridLayoutWidget_8.setObjectName(_fromUtf8("gridLayoutWidget_8"))
        self.celda7 = QtGui.QGridLayout(self.gridLayoutWidget_8)
        self.celda7.setMargin(0)
        self.celda7.setObjectName(_fromUtf8("celda7"))
        self.gridLayoutWidget_9 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(190, 300, 151, 121))
        self.gridLayoutWidget_9.setObjectName(_fromUtf8("gridLayoutWidget_9"))
        self.celda8 = QtGui.QGridLayout(self.gridLayoutWidget_9)
        self.celda8.setMargin(0)
        self.celda8.setObjectName(_fromUtf8("celda8"))
        self.gridLayoutWidget_10 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(360, 300, 151, 121))
        self.gridLayoutWidget_10.setObjectName(_fromUtf8("gridLayoutWidget_10"))
        self.celda9 = QtGui.QGridLayout(self.gridLayoutWidget_10)
        self.celda9.setMargin(0)
        self.celda9.setObjectName(_fromUtf8("celda9"))
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(20, 141, 491, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(20, 281, 491, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralWidget)
        self.line_3.setGeometry(QtCore.QRect(173, 20, 16, 401))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralWidget)
        self.line_4.setGeometry(QtCore.QRect(343, 20, 16, 401))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.lcdNumber = QtGui. QLCDNumber(self.centralWidget)
        self.lcdNumber.setGeometry(QtCore.QRect(580, 80, 138, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 140, 51, 51))
        self.pushButton_2.setText(_fromUtf8(""))
        pixmap = QtGui.QPixmap("./images/visto1.png")
        icon = QtGui.QIcon()
        icon.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 210, 51, 51))
        self.pushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./images/ayuda.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_4 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 290, 51, 51))
        self.pushButton_4.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./images/guardar.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_6 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(610, 370, 51, 51))
        self.pushButton_6.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./images/exit.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        QtCore.QObject.connect(self.pushButton_6,QtCore.SIGNAL('clicked()'),QtGui.qApp, QtCore.SLOT('quit()'))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(540, 120, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(540, 190, 161, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(540, 270, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(550, 353, 51, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        QTablero.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(QTablero)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        QTablero.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(QTablero)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        QTablero.setMenuBar(self.menuBar)
        self.actionQuit_2 = QtGui.QAction(QTablero)
        self.actionQuit_2.setObjectName(_fromUtf8("actionQuit_2"))
        self.actionExit = QtGui.QAction(QTablero)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.partidanueva(1)
        self.retranslateUi(QTablero)
        QtCore.QMetaObject.connectSlotsByName(QTablero)
        self.ll= QtGui.QLineEdit()




    def partidanueva(self, d):
        self.a =33
        if d==1:
          self.a=33
        if d==2:
          self.a=25
        if d==3:
          self.a=19


        self.gridLayout_2.addWidget(QtGui.QLabel("Jugador:"),1,0)
        self.gridLayout_2.addWidget(QtGui.QLabel("jugado"),1,1)
        self.gridLayout_2.addWidget(QtGui.QLabel("Puntaje:"),2,0)
        self.gridLayout_2.addWidget(QtGui.QLabel("puntos"),2,1)

#carga el archivo
        f=open("ola k ase.txt","r")
        i=0
        tablero=[]
        tablero_original=[]
        habilitados=[]
        tableroresuelto=[]
        for line in f:
            linea=line.split(',')
            tableroresuelto.append(linea)
            i=i+1
            print ("\n")
        i=0
        j=0



#ingresa 0 los numeros aleatoriamente

        k=0
        tablero=deepcopy(tableroresuelto)
        habilitados= deepcopy(tableroresuelto)
        tablero_original= deepcopy(tableroresuelto)

        while k<self.a:
            x = random.randrange(0, 9)
            y= random.randrange(0, 9)
            if int(tablero[x][y])!=0 :
               habilitados[x][y]="0"
               tablero[x][y]="0"
            k=k+1


#ingresa las fichas al tablero
        ind=QtGui.QDoubleValidator(1, 9, 0, QTablero)

        while i<9:
          j=0
          while j<9:
             if int( habilitados[i][j])!=0:
                 habilitados[i][j]="1"
             print ( habilitados[i][j])
             print ( tablero_original[i][j])
             print (tablero[i][j])
             line=QtGui.QLineEdit(tablero[i][j])

             if int(habilitados[i][j])==1:
                 line.setEnabled(False)
             if int(tablero[i][j])==0:
                 line.setText("")
                 line.setMaxLength(1)
                 line.setValidator(ind)


             if i>=0 and i<=2 and j>=0 and j<=2:
                self.celda1.addWidget(line,i,j)
             if i>=0 and i<=2 and j>=3 and j<=5:
                    self.celda2.addWidget(line,i,j)
             if i>=0 and i<=2 and j>=6 and j<=8:
                   self.celda3.addWidget(line,i,j)
             if i>=3 and i<=5 and j>=0 and j<=2:
                   self.celda4.addWidget(line,i,j)
             if i>=3 and i<=5 and j>=3 and j<=5:
                   self.celda5.addWidget(line,i,j)
             if i>=3 and i<=5 and j>=6 and j<=8:
                   self.celda6.addWidget(line,i,j)
             if i>=6 and i<=8 and j>=0 and j<=2:
                   self.celda7.addWidget(line,i,j)
             if i>=6 and i<=8 and j>=3 and j<=5:
                   self.celda8.addWidget(line,i,j)
             if i>=6 and i<=8 and j>=6 and j<=8:
                   self.celda9.addWidget(line,i,j)
             j=j+1
          i=i+1





    def verificar_fila(self,ficha,m):
        num=0
        b=0
        j=0
        while j<9:
            if   int(self.tablero[j][m])!=0:
              b=b+1
            if num>1:
                return 0
            j=j+1
        #if b==9:
            ##aqui van los puntajes para q valla aumentando
        return 1


    def verificar_columna(self,B,l,m):
        num=0
        b=0
        j=0
        while j<9:
            if int(self.tablero[l][j])!=0:
               b=b+1
            j=j+1
        if int(self.tablero[l][j])==B:
          num=num+1
        if num>1:
            return 0
            #if b==9
            #aqui van las lineas para cambiar el puntaje
        return 1


    def verificarsubcuadricula(ficha,l,m):
        if l<=2 and m<=2:
           b=0
           num=0
           i=0
           j=0
           while i<3:
             while j<3:
               if int(self.tablero[i][j]) !=0:
                  b=b+1
               if(b==9):
                   ##aumentan puntaje y setea los puntos
                   a=0
               if int(self.tablero[i][j])==ficha:
                   num=num+1
               j=j+1
             i=i+1
             if num>1:
                 return 0




        if l<=2 and m<=3 and m<=5:
           b=0
           num=0
           i=0
           j=3
           while i<3:
             while j<6:
               if int(self.tablero[i][j]) !=0:
                  b=b+1
               if(b==9):
                   ##aumentan puntaje y setea los puntos
                   a=0
               if int(self.tablero[i][j])==ficha:
                   num=num+1
               j=j+1
             i=i+1
             if num>1:
                 return 0




        if l<=2 and m<=6 and m<=8:
           b=0
           num=0
           i=0
           j=6
           while i<3:
             while j<9:
               if int(self.tablero[i][j]) !=0:
                  b=b+1
               if(b==9):
                   ##aumentan puntaje y setea los puntos
                   a=0
               if int(self.tablero[i][j])==ficha:
                   num=num+1
               j=j+1
             i=i+1
             if num>1:
                 return 0





        if l<=3 and l<=5  and m<=2:
           b=0
           num=0
           i=3
           j=0
           while i<6:
             while j<3:
               if int(self.tablero[i][j]) !=0:
                  b=b+1
               if(b==9):
                   ##aumentan puntaje y setea los puntos  a no vale XD
                   a=0
               if int(self.tablero[i][j])==ficha:
                   num=num+1
               j=j+1
             i=i+1
             if num>1:
                 return 0




        if l<=3 and l<=5 and m<=3 and m<=5:
           b=0
           num=0
           i=3
           j=3
           while i<6:
             while j<6:
               if int(self.tablero[i][j]) !=0:
                  b=b+1
               if(b==9):
                   ##aumentan puntaje y setea los puntos
                   a=0
               if int(self.tablero[i][j])==ficha:
                   num=num+1
               j=j+1
             i=i+1
             if num>1:
                 return 0





        if l<=3 and l<=5 and m<=6 and m<=8:
           b=0
           num=0
           i=3
           j=6
           while i<6:
             while j<9:
               if int(self.tablero[i][j]) !=0:
                  b=b+1
               if(b==9):
                   ##aumentan puntaje y setea los puntos
                   a=0
               if int(self.tablero[i][j])==ficha:
                   num=num+1
               j=j+1
             i=i+1
             if num>1:
                 return 0




        if l<=6 and l<=8 and m<=2:
           b=0
           num=0
           i=6
           j=0
           while i<9:
             while j<3:
               if int(self.tablero[i][j]) !=0:
                  b=b+1
               if(b==9):
                   ##aumentan puntaje y setea los puntos
                   a=0
               if int(self.tablero[i][j])==ficha:
                   num=num+1
               j=j+1
             i=i+1
             if num>1:
                 return 0




        if l<=6 and l<=8 and m<=3 and m<=5:
           b=0
           num=0
           i=6
           j=3
           while i<9:
             while j<6:
               if int(self.tablero[i][j]) !=0:
                  b=b+1
               if(b==9):
                   ##aumentan puntaje y setea los puntos
                   a=0
               if int(self.tablero[i][j])==ficha:
                   num=num+1
               j=j+1
             i=i+1
             if num>1:
                 return 0



        if l<=6 and l<=8 and m<=6 and m<=8:
           b=0
           num=0
           i=6
           j=6
           while i<9:
             while j<9:
               if int(self.tablero[i][j]) !=0:
                  b=b+1
               if(b==9):
                   ##aumentan puntaje y setea los puntos
                   a=0
               if int(self.tablero[i][j])==ficha:
                   num=num+1
               j=j+1
             i=i+1
             if num>1:
                 return 0
        return 1


    def verificarficha(self):
        b=0
        i=0
        j=0
        while i<9:
          while j<9:
            if int(self.tablero[i][j])==0:
                  b=b+1
            j=j+1
          i=i+1
        if b==0:
            ##aqui van los puntajes
              QtGui.QMessageBox.information( QTablero,"sudoku message","Felicitaciones has terminado el sudoku",QtGui.QMessageBox.Ok)


    def control_ingreso_ficha():
        i=0
        j=0
        while i<9:
          while j<9:
              if int( tablero_original[i][j])!= int( tablero[i][j]):
                k=0
                if  verificar_fila(int( tablero[i][j]),j)==0:
                    QtGui.QMessageBox.information( QTablero,"sudoku message","número "+tablero[i][j]+" repetido en fila",QtGui.QMessageBox.Ok)
                if verificar_fila(int( tablero[i][j]),j)!=0:
                    k=k+1
                if  verificar_columna(int( tablero[i][j]),i,j)==0:
                    QtGui.QMessageBox.information( QTablero,"sudoku message","número "+tablero[i][j]+" repetido en columna",QtGui.QMessageBox.Ok)
                if  verificar_columna(int( tablero[i][j]),i,j)!=0:
                    k=k+1
                if   verificarsubcuadricula(int( tablero[i][j]),i,j)==0:
                    QtGui.QMessageBox.information( QTablero,"sudoku message","número "+tablero[i][j]+" repetido en subcuadricula",QtGui.QMessageBox.Ok)
                if   verificarsubcuadricula(int( tablero[i][j]),i,j)==0:
                    k=k+1
                if k==3:
                   tablero_original[i][j]= tablero[i][j]
                   #aqui debe ir aumentando puntaje y seteando


    def ayudaboton():
      i=0
      while i<1:
        x = random.randrange(0, 9)
        y= random.randrange(0, 9)
        if int(tablero[x][y])!=0 and int(habilitados[x][y])==0:
             tablero[x][y]=tablero_original[x][y]
        if int(tablero[x][y])==0 or int(habilitados[x][y])==1:
           i=i+1



    def retranslateUi(self, QTablero):
        QTablero.setWindowTitle(_translate("QTablero", "Sudoku", None))
        self.label.setText(_translate("QTablero", "Verificar Número Ingresado", None))
        self.label_2.setText(_translate("QTablero", "Ayuda ", None))
        self.label_3.setText(_translate("QTablero", "Guardar Partida", None))
        self.label_4.setText(_translate("QTablero", "Salir", None))
        self.menuFile.setTitle(_translate("QTablero", "File", None))
        self.actionQuit_2.setText(_translate("QTablero", "Quit", None))
        self.actionExit.setText(_translate("QTablero", "Exit", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QTablero = QtGui.QMainWindow()
    ui = Ui_QTablero()
    ui.setupUi(QTablero)
    QTablero.show()
    sys.exit(app.exec_())

