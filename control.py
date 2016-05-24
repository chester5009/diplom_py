
class Control:

    def __init__(self, ui):
        self.ui = ui
        self.current_method=0
        self.setSignalsButtons()
    
    def mannClick(self):
        self.current_method=1
        self.ui.stackedWidget.setCurrentIndex(1)
        pass
    
    def setSignalsButtons(self):
        self.ui.pushButton_2.clicked.connect(self.mannClick)
        pass
    
    pass