from pymongo import MongoClient
import datetime

from datetime import datetime
import matplotlib.pyplot as plt

client = MongoClient()
db = client['test']
tempStats = db.tempStats
date= datetime.now()

def try_me_id():
    # date= datetime.now()
    c_day= str( date.day)
    c_month= str (date.month)
    c_year=str(date.year)
   # key=c_day+'/'+c_month+'/'+c_year+'@'+ str(date.second)
    key= c_year+'-'+c_month+'-'+c_day+'T'+str(date.hour)+':'+str(date.minute)+':'+str(date.second)+'.'
    return key
   
# def generate_hour():
#     date= datetime.now()
#     return date.hour

# def generate_minutes():
#     date= datetime.now()
#     return date.minute


def setTemp(temp):
    return temp
# def setTime(time):
#     return time
    
tempVal ={
    '_id' : try_me_id(),
   'Temperature': setTemp(26),
    'hour' : date.hour,
    'minute': date.minute,
    'day': date.day,
    'year': date.year
    }
value= try_me_id

def getValue(value):
    tempStats = tempStats.find({
        '_id' : value
    })

print(tempVal)




# year = [20,25,30,35,40,45,50,55,60,65,70,85,90,95,100,105,110,120]



result= tempStats.insert_one(tempVal)



