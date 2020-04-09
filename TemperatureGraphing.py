import pymongo
import json
import os
import numpy as np
import matplotlib.pyplot as plt 
from pymongo import MongoClient 
 
client = MongoClient()
db = client['test']
tempStats = db.tempStats


def getValue(key): 
    cursor=tempStats.find({"_id": key},{"Temperature":"number", "_id": 0})
    domains = [datum['Temperature'] for datum in cursor ]
    res=str(domains)[1:-1]
    record=int(res)
    return record


def getLastValue():
    cursor=tempStats.find().sort([('_id', -1)]).limit(1)
    domains = [datum['_id'] for datum in cursor ]
    res=str(domains)[1:-1]
    record=int(res)
    #print(record)
    return record


def Day(day,month,year):
    temps = np.zeros(24)
    for x in range(0,24):

        # Aggregates all the data from the hour
        # Then pipes that output into a group to get an average temperature and the lowest ID
        agr = [ { "$match": {"year": year,
                             "month": month,
                             "day": day,
                             "hour":x}},
                { "$group": { "_id": x,
                              "avgTemp": {"$avg": "$Temperature"}}}]
        val = list(tempStats.aggregate(agr))
        avgTemp = 0
        for each in val:
            avgTemp = each['avgTemp']
        temps[x] = avgTemp
            
    x_values = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    x_labels = [0,3,6,9,12,15,18,21]
    my_x_ticks = ['12AM','3AM','6AM','9AM','12PM','3PM','6PM','9PM']

    i = 0
    j = 0
    for temperature in temps:
        if temperature < 40 or temperature > 100 :
            temps = np.delete(temps,i-j)
            x_values = np.delete(x_values,i-j)
            j += 1
        i += 1
    y = temps
    
    fig = plt.figure()
    plt.plot(x_values, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)         # setting x and y axis range 
    plt.ylim(40,100) 
    plt.xlim(0,24)
    plt.xticks(x_labels,my_x_ticks)
    plt.xlabel("Day %d/%d/%d" % (month,day,year))          # naming the x axis 
    plt.ylabel('Temperature')         # naming the y axis 
    plt.title('Temperature visualization')         # giving a title to my graph 
    #plt.show()        # function to show the plot 
    filepath = os.path.abspath(__file__)
    filepath = os.path.dirname(filepath)
    fig.savefig(filepath+'\\website-test-mccain\\src\\assets\\plot.png')  
    return None

def Week(day, month, year):
    temps = np.zeros(7)
    entry = tempStats.find_one({'day':day,'month':month,'year':year})
    week = entry['week']
    isoyear = entry['isoyear']

    for x in range(0,7):

        # Aggregates all the data from the day
        # Then pipes that output into a group to get an average temperature and the lowest ID
        agr = [ { "$match": {"isoyear": isoyear,
                             "week": week,
                             "weekday": x+1}},
                { "$group": { "_id": x,
                              "avgTemp": {"$avg": "$Temperature"}}}]
        val = list(tempStats.aggregate(agr))
        avgTemp = 0
        for each in val:
            avgTemp = each['avgTemp']
        temps[x] = avgTemp

    x_values = [0,1,2,3,4,5,6]
    x_ticks = x_values
    my_x_ticks = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

    i = 0
    j = 0
    for temperature in temps:
        if temperature < 50 or temperature > 90 :
            temps = np.delete(temps,i-j)
            x_values = np.delete(x_values,i-j)
            j += 1
        i += 1

    y = temps   # corresponding y axis values 
    fig = plt.figure()
    plt.plot(x_values, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)         # setting x and y axis range 
    plt.ylim(50,90) 
    plt.xlim(0,6)
    plt.xticks(x_ticks,my_x_ticks)
    plt.xlabel("Week of %d/%d/%d" % (month,day,year))         # naming the x axis 
    plt.ylabel('Temperature')         # naming the y axis 
    plt.title('Temperature visualization')         # giving a title to my graph 
    #plt.show()        # function to show the plot 
    filepath = os.path.abspath(__file__)
    filepath = os.path.dirname(filepath)
    fig.savefig(filepath+'\\website-test-mccain\\src\\assets\\plot.png')  
    return temps

def Month(month, year):
    temps = np.zeros(31)

    for x in range(0,31):
        # Aggregates all the data from each day
        # Then pipes that output into a group to get an average temperature and the lowest ID
        agr = [ { "$match": {"year":year,
                             "month":month,
                             "day": x+1}},
                { "$group": { "_id": x,
                              "avgTemp": {"$avg": "$Temperature"}}}]
        val = list(tempStats.aggregate(agr))
        avgTemp = 0
        for each in val:
            avgTemp = each['avgTemp']
        temps[x] = avgTemp

    x_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    my_x_ticks = [1,4,7,10,13,16,19,22,25,28,31]
    i = 0
    j = 0
    for temperature in temps:
        if temperature < 50 or temperature > 90 :
            temps = np.delete(temps,i-j)
            x_values = np.delete(x_values,i-j)
            j += 1
        i += 1

    month_label = getMonth(month)

    y = temps   # corresponding y axis values 
    fig = plt.figure()
    plt.plot(x_values, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)         # setting x and y axis range 
    plt.ylim(50,90) 
    plt.xlim(1,31)
    plt.xticks(my_x_ticks)
    plt.xlabel("%s %d" % (month_label,year))         # naming the x axis 
    plt.ylabel('Temperature')         # naming the y axis 
    plt.title('Temperature visualization')         # giving a title to my graph 
    #plt.show()        # function to show the plot 
    filepath = os.path.abspath(__file__)
    filepath = os.path.dirname(filepath)
    fig.savefig(filepath+'\\website-test-mccain\\src\\assets\\plot.png')  
    return temps

def getMonth(month):
    return {
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'
    }[month]

def Year(year):
    temps = np.zeros(12)

    for x in range(0,12):
        # Aggregates all the data from each day
        # Then pipes that output into a group to get an average temperature and the lowest ID
        agr = [ { "$match": {"year":year,
                             "month":x+1,}},
                { "$group": { "_id": x,
                              "avgTemp": {"$avg": "$Temperature"}}}]
        val = list(tempStats.aggregate(agr))
        avgTemp = 0
        for each in val:
            avgTemp = each['avgTemp']
        temps[x] = avgTemp


    x_values = [1,2,3,4,5,6,7,8,9,10,11,12]
    x_ticks = x_values
    x_ticks_labels = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    i = 0
    j = 0
    for temperature in temps:
        if temperature < 50 or temperature > 90 :
            temps = np.delete(temps,i-j)
            x_values = np.delete(x_values,i-j)
            j += 1
        i += 1

    y = temps   # corresponding y axis values 
    fig = plt.figure()
    plt.plot(x_values, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)         # setting x and y axis range 
    plt.ylim(50,90) 
    plt.xlim(1,12)
    plt.xticks(x_ticks,x_ticks_labels)
    plt.xlabel("Year %d" % year)         # naming the x axis 
    plt.ylabel('Temperature')         # naming the y axis 
    plt.title('Temperature visualization')         # giving a title to my graph 
    #plt.show()        # function to show the plot 
    filepath = os.path.abspath(__file__)
    filepath = os.path.dirname(filepath)
    fig.savefig(filepath+'\\website-test-mccain\\src\\assets\\plot.png')  
    return temps



def main(select,day,month,year):       
    if(select==1): # 1 Day selection
        Day(day,month,year)
  
    if(select==2): # 1 Week
        Week(day, month, year)
    
    if(select==3): # 1 Month
        Month(month,year)
    
    if(select==4): # 1 Year
        Year(year)

