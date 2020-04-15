import sys
import Adafruit_DHT
import os

humidity, temperature = Adafruit_DHT.read_retry(11, 4)
print('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))
os.system("""curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:5000/post' -d '{"temp":"{}"}'""".format(temperature))

