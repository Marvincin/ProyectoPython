# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cargar.ui'
#
# Created: Tue Jul 30 23:14:45 2013
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(390, 292)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./images/Sudoku.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./images/Sudoku.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./images/Sudoku.png")), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./images/Sudoku.png")), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(407, 159))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 221, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 301, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS PGothic"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 230, 81, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./images/visto1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 230, 81, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/x.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(0, -10, 401, 311))
        self.pushButton_3.setText(_fromUtf8(""))
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.comboBox.setItemText(0, _translate("Dialog", "New Item", None))
        self.comboBox.setItemText(1, _translate("Dialog", "New Item2", None))
        self.label.setText(_translate("Dialog", "Partidas guardadas", None))
        self.label_2.setText(_translate("Dialog", "Seleccione su partida guardada", None))
        self.pushButton.setText(_translate("Dialog", "Aceptar", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

