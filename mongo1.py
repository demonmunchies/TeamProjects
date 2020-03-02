from pymongo import MongoClient
import datetime

from datetime import datetime
import matplotlib.pyplot as plt

client = MongoClient()
db = client['test']
tempStats = db.tempStats
date= datetime.now()

def getValue(value):
    tempVal = tempStats.find({
        '_id' : value
    })
    return tempVal

def insertValue(temp):
    tempVal ={
    #'_id' : try_me_id(),
    '_id' :db.tempStats.find().count()+1,
   'Temperature': temp,
    'hour' : date.hour,
    'minute': date.minute,
    'day': date.day,
    'year': date.year
    }
    tempStats.insert_one(tempVal)

insertValue(99)
print(getValue(2))
