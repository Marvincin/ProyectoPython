# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtablero.ui'
#
# Created: Wed Jul 17 22:11:04 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(540, 120, 201, 281))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/0.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_6 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout.addWidget(self.pushButton_6)
        self.gridLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 511, 401))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(310, 440, 431, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(539, 10, 201, 71))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralWidget)
        self.lcdNumber.setGeometry(QtCore.QRect(563, 90, 141, 23))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
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

        self.retranslateUi(QTablero)
        QtCore.QMetaObject.connectSlotsByName(QTablero)

    def retranslateUi(self, QTablero):
        QTablero.setWindowTitle(_translate("QTablero", "QTablero", None))
        self.pushButton_2.setText(_translate("QTablero", "Juego Nuevo", None))
        self.pushButton.setText(_translate("QTablero", "Verificar", None))
        self.pushButton_4.setText(_translate("QTablero", "Guardar partida", None))
        self.pushButton_6.setText(_translate("QTablero", "Salir", None))
        self.menuFile.setTitle(_translate("QTablero", "File", None))
        self.actionQuit_2.setText(_translate("QTablero", "Quit", None))
        self.actionExit.setText(_translate("QTablero", "Exit", None))

#import images_rc




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QTablero = QtGui.QMainWindow()
    ui = Ui_QTablero()
    ui.setupUi(QTablero)
    QTablero.show()
    sys.exit(app.exec_())

