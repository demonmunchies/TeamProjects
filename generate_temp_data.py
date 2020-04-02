<<<<<<< HEAD
from random import gauss
import math

id = 1
hour = 0
minute = 0
day = 1
month = 1
year = 2020
isoyear = 2020
week = 1
weekday = 1

temperature = 70

minutes_in_year = 525600

f = open("tempdata.dat", "w")

for x in range(minutes_in_year):
	minute += 1
	delta = gauss(0, .1)
	temperature = temperature + delta
	if temperature < 60 or temperature > 80:
		temperature = (temperature - delta) - delta
	if hour > 23:
		hour = 0
		day += 1
	if minute > 59:
		minute = 0
		hour += 1
	if day > 30:
		day = 1
		month += 1
	if weekday > 7:
		weekday = 0
		week += 1

	json_str = """{"_id":{"$numberInt":%d},"Temperature":{"$numberInt":%d},"hour":{"$numberInt":%d},"minute":{"$numberInt":%d},"day":{"$numberInt":%d},"month":{"$numberInt":%d},"year":{"$numberInt":%d},"isoyear":{"$numberInt":%d},"week":{"$numberInt":%d},"weekday":{"$numberInt":%d}}\n""" % (id, temperature, hour, minute, day, month, year, isoyear, week, weekday)

	f.write(json_str)
f.close()
=======
from random import gauss
import math
import datetime
from pymongo import MongoClient

client = MongoClient()
db = client['test']
tempStats = db.tempStats

id = 1
hour = 0
minute = 0
day = 0
month = 1
year = 2020
isoyear = 2020
week = 1
weekday = 1

temperature = 70

minutes_in_year = 525600
current = datetime.datetime.now()
last_year = current-datetime.timedelta(days=365)

for x in range(minutes_in_year):

	delta = gauss(0, .1)
	temperature = temperature + delta
	if temperature < 60 or temperature > 80:
		temperature = (temperature - delta) - delta
	temp_time = last_year+datetime.timedelta(minutes=minute)
	d = {}
	d['Temperature'] = temperature
	d['hour'] = int(temp_time.hour)
	d['minute'] = int(temp_time.minute)
	d['day'] = int(temp_time.day)
	d['month'] = int(temp_time.month)
	d['year'] = int(temp_time.year)
	d['isoyear'] = int(temp_time.strftime("%G"))
	d['week'] = int(temp_time.strftime("%V"))
	d['weekday'] = int(temp_time.strftime("%u"))
	tempStats.insert_one(d)
	id += 1
	minute += 1


>>>>>>> origin/central-unit
