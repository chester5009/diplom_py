# -*- coding: utf-8 -*-
class Control:

    def __init__(self, ui):
        self.ui = ui
        self.infoString = ""
        self.current_method = 0
        self.setSignalsButtons()
    
    def mannClick(self):
        self.current_method = 1
        self.infoString = self.getInfo(self.current_method).decode('utf-8')
        self.ui.textBrowser.setText(self.infoString)
        self.ui.stackedWidget.setCurrentIndex(1)
        
        pass
    
    def backButton1Click(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        pass
    
    def backButton2Click(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        pass
    
    def nextButton1Click(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        pass
    
    def nextButton2Click(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        pass
    
    def getInfo(self, method):
        file = open("assets/info.txt", 'r')
        return file.read()
        pass
    
    
    # signals
    def setSignalsButtons(self):
        self.ui.pushButton_2.clicked.connect(self.mannClick)
        self.ui.pushButton_5.clicked.connect(self.backButton1Click)
        self.ui.pushButton_4.clicked.connect(self.nextButton1Click)
        self.ui.pushButton_7.clicked.connect(self.nextButton2Click)
        self.ui.pushButton_6.clicked.connect(self.backButton2Click)
        pass
    
    pass
