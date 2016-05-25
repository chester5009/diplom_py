# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
class Entity:

    def __init__(self, scores, rate, group):
        self.scores = scores
        self.rate = rate
        self.group = group

    
    
class MannWhithney:

    def __init__(self, data):
        self.data = data
        self.entyties = []
        
    def showEnts(self):
        for i in range(len(self.entyties)):
            print self.entyties[i].scores, " ", self.entyties[i].rate, " ", self.entyties[i].group
        pass   
        
    def makeEntyties(self, data):
        self.entyties = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                oneEnt = Entity(data[i][j].toInt(), -1, i)
                self.entyties.append(oneEnt)
        print data
        print self.entyties    
    
    def sort(self):
        a = self.entyties
        for i in reversed(range(len(a))):
            for j in range(1, i + 1):
                if a[j - 1].scores > a[j].scores:
                    a[j], a[j - 1] = a[j - 1], a[j]
        pass
    
    def setRanks(self):
        rate = 0.0
        count = 0
        for i in range(len(self.entyties)):
            if i<len(self.entyties) and i>0:
                if self.entyties[i].scores !=self.entyties[i-1].scores:
                    rate+=i*1.0
                    count+=1
                    
                        
                
        pass
    
    
   
