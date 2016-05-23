import sys
from PyQt4 import QtGui,QtCore
from form import Ui_Form

def main():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    ui=Ui_Form()
    ui.setupUi(w)
    w.show()
    
    sys.exit(app.exec_())
    
    pass

main()


