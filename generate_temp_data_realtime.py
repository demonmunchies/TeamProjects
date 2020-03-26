from random import gauss
import math
import os
import datetime

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


f = open(os.path.abspath(__file__)+"tempdata.dat", "w")

for x in range(minutes_in_year):
	minute += 1
	delta = gauss(0, .1)
	temperature = temperature + delta
	if temperature < 60 or temperature > 80:
		temperature = (temperature - delta) - delta
	temp_time = last_year+datetime.timedelta(minutes=minute)

	json_str = """{"_id":{"$numberInt":%d},"Temperature":{"$numberInt":%d},"hour":{"$numberInt":%d},"minute":{"$numberInt":%d},"day":{"$numberInt":%d},"month":{"$numberInt":%d},"year":{"$numberInt":%d},"isoyear":{"$numberInt":%d},"week":{"$numberInt":%d},"weekday":{"$numberInt":%d}}\n""" % (id, temperature,int(temp_time.hour),int(temp_time.minute), int(temp_time.day),int(temp_time.month),int(temp_time.year), int(temp_time.strftime("%G")), int(temp_time.strftime("%V")), int(temp_time.strftime("%u")))

	f.write(json_str)