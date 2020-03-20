from pymongo import MongoClient
import datetime

from datetime import datetime
from datetime import date
import matplotlib.pyplot as plt

client = MongoClient()
db = client['test']
tempStats = db.tempStats
date= datetime.now()

def getValue(year, month, day, hour, minute):
    tempVal = tempStats.find_one({
        'year': year,
        'month': month,
        'day': day,
        'hour': hour,
        'minute': minute
    })
    if(tempVal != None):
        temperature = tempVal['Temperature']
    else:
        temperature = 0
    return temperature


def insertValue(temp):
    tempVal ={
    #'_id' : try_me_id(),
    '_id' :db.tempStats.find().count()+1,
    'Temperature': temp,
    'hour' : date.hour,
    'minute': date.minute,
    'day': date.day,
    'month': date.month,
    'year': date.year,
    'isoyear': date.isocalendar()[0],
    'week': date.isocalendar()[1],
    'weekday': date.isocalendar()[2]
    }
    tempStats.insert_one(tempVal)

# def insertTemperature(year,day,hour,minute):
#     mydate = date.fromordinal(date(year, 1, 1).toordinal() + day - 1)
#     print(mydate)

# insertTemperature(2020,20,1,50)
insertValue(70)