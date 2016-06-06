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
        self.n1=None
        self.n2=None
        self.Tx=None
        self.nx=None
        self.result=None
        self.data001=None
        self.data005=None
        self.emp001=None
        self.emp005=None
        
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
            if i == 0:
                rate = (i + 1) * 1.0
                count += 1
                print "Rate i=0 " + str(rate)
            elif i > 0 and i < len(self.entyties) - 1:
                if self.entyties[i - 1].scores != self.entyties[i].scores:
                    for m in range(count):
                        self.entyties[i - (m + 1)].rate = rate / count * 1.0
                    count = 1
                    rate = (i + 1) * 1.0
                else:
                    rate += (i + 1) * 1.0
                    count += 1
            elif i == len(self.entyties) - 1:
                if self.entyties[i - 1].scores != self.entyties[i].scores:
                    for m in range(count):
                        self.entyties[i - (m + 1)].rate = rate / count * 1.0
                    count = 1
                    rate = (i + 1) * 1.0
                    self.entyties[i].rate=rate/count*1.0
                else:
                    for m in range(count):
                        self.entyties[i - (m + 1)].rate = rate / count * 1.0
                    self.entyties[i ].rate = rate / count * 1.0
        pass
    
    def calculate(self):
        self.n1=self.getN(0)
        self.n2=self.getN(1)
        self.Tx=self.getHigherRankedSum()
        self.nx=self.getHigherGroup()
        self.result=self.n1*self.n2+self.nx*(self.nx+1)/2-self.Tx
        self.emp001=self.data001[self.n1-5][self.n2-2]
        self.emp005=self.data005[self.n1-3][self.n2-2]
    def getN(self,number):
        count=0
        for i in range(len(self.entyties)):
            if self.entyties[i].group==number:
                count+=1
        return count
    def getRankSum(self,group):
        sum=0;
        for i in range(len(self.entyties)):
            if self.entyties[i].group==group:
                sum+=self.entyties[i].rate
        return sum
    
    def getHigherRankedSum(self):
        sum1=0
        sum2=0
        for i in range(len(self.entyties)):
            if self.entyties[i].group==0:
                sum1+=self.entyties[i].rate
            else: sum2+=self.entyties[i].rate
        
        if sum1>sum2: return sum1 
        else: return sum2
    def getHigherGroup(self):
        sum1=self.getRankSum(0)
        sum2=self.getRankSum(1)
        if sum1>sum2:
            return self.getN(0)
        else:return self.getN(1)
    
    def setTable(self,tab001,tab005):
        self.data001=tab001
        self.data005=tab005
        
    def getHipotese(self):
        itog=' ';
        itog+="n1 "+str(self.n1)+" n2 "+str(self.n2)+" nx "+str(self.nx)+" Tx "+str(self.Tx)+" Koeff "+str(self.result)+" E001 "+str(self.emp001)+" E005 "+str(self.emp005)
        if self.result<self.emp001 or self.result>self.emp005:
            itog+=u''' Экспериментальная группа не превосходит контрольную группу по уровню невербального интеллекта.'''
        else: itog+=u''' Экспериментальная группа превосходит контрольную группу
                    по уровню невербального интеллекта.'''
        return itog
    def printResult(self):
        print "n1 "+str(self.n1)+" n2 "+str(self.n2)+" nx "+str(self.nx)+" Tx "+str(self.Tx)
        print "Koeff "+str(self.result)
        print "E001 "+str(self.emp001)
        print "E005 "+str(self.emp005)
        print "EHEHE "+str(self.data005[14-3][12-2])
    def printTable(self,table):
        for i in table:
            print i
        print ""    
