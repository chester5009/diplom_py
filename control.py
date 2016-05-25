# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from mannwhithney import MannWhithney
class Control:

    def __init__(self, ui):
        self.ui = ui
        self.infoString = ""
        self.current_method = 0
        self.setSignalsButtons()
        self.ui.stackedWidget.setCurrentIndex(0)
    
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
        self.initTable(self.ui.tableWidget, 2, 2)
        pass
    
    def AddButton1Click(self):
        rowCount = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowCount)
        pass
    
    def DeleteButton1Click(self):
        self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())
        pass
    
    def getInfo(self, method):
        file = open("assets/info.txt", 'r')
        return file.read()
        pass
    
    def CalculateButtonclick(self):
        data=self.getDataFromTable(0, 1)
        self.CalculateAction(data)
        pass
    
    def CalculateAction(self,data):
        if self.current_method==1:
            mann=MannWhithney(data)
            mann.makeEntyties(mann.data)
            mann.sort()
            mann.setRanks()
            mann.showEnts()
            
            #print "Mann!",data
        pass
    
    def initTable(self, t, rows, cols):
        t.clear()
        t.clearContents()
        t.setRowCount(rows)
        t.setColumnCount(cols)
        t.setHorizontalHeaderLabels([u"Контрольная", u"Экспериментальная"])
        pass
    
    def getDataFromTable(self, startCol, finishCol):
        data = []
        countRow = self.ui.tableWidget.rowCount()
        maxCol=finishCol - startCol + 1;
        print "size ",startCol," ",maxCol
        for startCol in range(maxCol):
            oneCol = []
            for j in range(countRow): 
                
                if self.ui.tableWidget.item(j, startCol) :
                    value = self.ui.tableWidget.item(j, startCol).text()
                    oneCol.append(value)
                    print value.toUtf8()
                else:
                    print "Error read item"
            data.append(oneCol)
            # print "one col ", oneCol[0].toInt()
        
        return data
        
                    
    
    # signals
    def setSignalsButtons(self):
        self.ui.pushButton_2.clicked.connect(self.mannClick)
        self.ui.pushButton_5.clicked.connect(self.backButton1Click)
        self.ui.pushButton_4.clicked.connect(self.nextButton1Click)
        self.ui.pushButton_7.clicked.connect(self.nextButton2Click)
        self.ui.pushButton_6.clicked.connect(self.backButton2Click)
        self.ui.pushButton_8.clicked.connect(self.AddButton1Click)
        self.ui.pushButton_9.clicked.connect(self.DeleteButton1Click)
        self.ui.pushButton_10.clicked.connect(self.CalculateButtonclick)
        pass
    
    pass
