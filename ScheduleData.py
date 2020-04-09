import datetime
from pymongo import MongoClient

client = MongoClient()
db = client['test']
currentSchedule = db.Schedule

def updateSchedule(schedule):
    currentSchedule.remove( { } )
    id = 1
    for x in schedule:
        d = {}
        d['temperature'] = x['temperature']
        d['time'] = x['time']
        currentSchedule.insert_one(d)
        id += 1

def getSchedule():
    s = []
    for doc in currentSchedule.find():
        s.append({'time': doc['time'], 'temperature': doc['temperature']})
    return s