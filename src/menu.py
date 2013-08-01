'''
Created on 24/07/2013

@author: xtreme
'''

import sys 
from PyQt4 import QtGui
from principal import Ui_principal

def main():
    aplicacion = QtGui.QApplication(sys.argv)
    principal = QtGui.QMainWindow()
    ui = Ui_principal()
    ui.setupUi(principal)
    principal.show()
    sys.exit(aplicacion.exec_())


if __name__ == '__main__':
    main()