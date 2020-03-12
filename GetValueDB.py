import pymongo
import json
import matplotlib.pyplot as plt 
from pymongo import MongoClient


class myClass():
    connection =MongoClient('mongodb://localhost:27017')
    db = connection.stest
    data=db.tempStats
    #arraylist
    
    def getValue(self,key): 
        cursor=myClass.data.find({"_id": key},{"Temperature":"number", "_id": 0})
        domains = [datum['Temperature'] for datum in cursor ]
        res=str(domains)[1:-1]
        record=int(res)
        return record

    def getLastValue(self):
        cursor=myClass.data.find().sort([('_id', -1)]).limit(1)
        domains = [datum['_id'] for datum in cursor ]
        res=str(domains)[1:-1]
        record=int(res)
        #print(record)
        return record

    def lastHalfHour(self):
        count=10
        myHalfH=[]
        lastIndex=myClass.getLastValue(self)
        while(count!=0):
            value=myClass.getValue(self,lastIndex)
            lastIndex-=1
            count-=1
            myHalfH.append(value)
        myHalfH.reverse()
        return myHalfH


    def lastHour(self):
        count=20
        myHour=[]
        lastIndex=myClass.getLastValue(self) 
        while(count!=0):
            value=myClass.getValue(self,lastIndex)
            lastIndex-=1
            count-=1
            myHour.append(value)
        myHour.reverse()
        return myHour
            
    def last12Hour(self):
        count=24
        ave=0
        myHour=[]
        lastIndex=myClass.getLastValue(self) 
        while(count!=0):
            totaltemp=0
            for x in range(10):
                value1=myClass.getValue(self,lastIndex)
                totaltemp=totaltemp+value1
                lastIndex-=1
            ave=totaltemp/10
            count-=1
            myHour.append(ave)
        myHour.reverse()
        return myHour

    def last24Hour(self):
        count=24
        ave=0
        myHour=[]
        lastIndex=myClass.getLastValue(self)
        while(count!=0):
            totaltemp=0
            for x in range(20):
                value1=myClass.getValue(self,lastIndex)
                totaltemp=totaltemp+value1
                lastIndex-=1
            ave=totaltemp/20
            count-=1
            myHour.append(ave)
        myHour.reverse()
        return myHour

    def last30Days(self):
        count=30
        ave=0
        myHour=[]
        lastIndex=myClass.getLastValue(self)
        while(count!=0):
            totaltemp=0
            for x in range(480):
                value1=myClass.getValue(self,lastIndex)
                totaltemp=totaltemp+value1
                lastIndex-=1
            ave=totaltemp/480
            count-=1
            myHour.append(ave)
        myHour.reverse()
        return myHour   
      
def main(select):       
    c=myClass()
    if(select==1):
        x = [0,3,6,9,12,15,18,21,24,27]    # x axis values 
        y = c.lastHalfHour()     # corresponding y axis values 
        fig = plt.figure()
        plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)         # setting x and y axis range 
        plt.ylim(0,100) 
        plt.xlim(0,33) 
        plt.xlabel('Last 30-min')         # naming the x axis 
        plt.ylabel('Temperature')         # naming the y axis 
        plt.title('Temperature visualization')         # giving a title to my graph 
        plt.show()        # function to show the plot 
        fig.savefig('plot.png')
    if(select==2):
        x = [0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57]
        y = c.lastHour()     # corresponding y axis values 
        fig = plt.figure()
        plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)         # setting x and y axis range 
        plt.ylim(0,100) 
        plt.xlim(0,60) 
        plt.xlabel('Last 60-min')         # naming the x axis 
        plt.ylabel('Temperature')         # naming the y axis 
        plt.title('Temperature visualization')         # giving a title to my graph 
        plt.show()        # function to show the plot 
        fig.savefig('plot.png')
    if(select==3):
        x = [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12]
        y = c.last12Hour()   # corresponding y axis values 
        fig = plt.figure()
        plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)         # setting x and y axis range 
        plt.ylim(0,100) 
        plt.xlim(0,12) 
        plt.xlabel('Last 12-hour')         # naming the x axis 
        plt.ylabel('Temperature')         # naming the y axis 
        plt.title('Temperature visualization')         # giving a title to my graph 
        plt.show()        # function to show the plot 
        fig.savefig('plot.png')
    if(select==4):
        x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        y = c.last24Hour()   # corresponding y axis values 
        fig = plt.figure()
        plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)         # setting x and y axis range 
        plt.ylim(0,100) 
        plt.xlim(0,24) 
        plt.xlabel('Last 24-hour')         # naming the x axis 
        plt.ylabel('Temperature')         # naming the y axis 
        plt.title('Temperature visualization')         # giving a title to my graph 
        plt.show()        # function to show the plot 
        fig.savefig('plot.png')

    
    if(select==5):
        x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        y = c.last30Days()   # corresponding y axis values 
        fig = plt.figure()
        plt.plot(x, y)         # setting x and y axis range 
        plt.ylim(0,100) 
        plt.xlim(0,30) 
        plt.xlabel('Last 30 days')         # naming the x axis 
        plt.ylabel('Temperature')         # naming the y axis 
        plt.title('Temperature visualization')         # giving a title to my graph 
        plt.show()        # function to show the plot
        fig.savefig('plot.png')
if __name__== "__main__":
  main(4)
