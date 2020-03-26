import pymongo
import json
import os
import numpy as np
import matplotlib.pyplot as plt 
from pymongo import MongoClient 
 
client = MongoClient()
db = client['test']
tempStats = db.tempStats


def hotOrCold(desiredTemp):
    cursor=tempStats.find().sort([('_id', -1)]).limit(1)
    domains = [datum['_id'] for datum in cursor ]
    res=str(domains)[1:-1]
    record=int(res)
    #print(record)
    if(record >= desiredTemp):
        return "H"
    else:
        return "C"


def getLastValue():
    cursor=tempStats.find().sort([('_id', -1)]).limit(1)
    domains = [datum['_id'] for datum in cursor ]
    res=str(domains)[1:-1]
    record=int(res)
    #print(record)
    return record

