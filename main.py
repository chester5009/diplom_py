# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from form import Ui_Form
from control import Control
from db_controls import DboxControls

method = 0;  # 1-mann 2-kolm

def clicked(ui):
    method = 1;
    pass

def main():
    print sys.getdefaultencoding()
    
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(w)
    
    control = Control(ui)
    msg=QtGui.QMessageBox()
    msg.setText(u'Результаты помещены в файл res.txt и загружены в облако DropBox')
    msg.exec_()
    w.show()
    
    
    
    sys.exit(app.exec_())
    
    pass

main()


