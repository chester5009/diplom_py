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
    drop=DboxControls(1)
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(w)
    
    control = Control(ui)
    
    w.show()
    
    
    
    sys.exit(app.exec_())
    
    pass

main()


