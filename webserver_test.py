from flask import Flask
from flask import request
import TemperatureGraphing
import accountAccess
import json

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_test():
	if request.method == 'GET':
		return 'Hello, World!'

@app.route('/post', methods=['POST'])
def post_test():
	if request.method == 'POST':
		data = json.loads(request.data)
		print(data['data'])
		return data['data']

# Specific graph wanted
@app.route('/get_singular_graph', methods=['POST'])
# Actually update this method to provide functionality
def get_singular_graph():
	if request.method == 'POST':
		data = json.loads(request.data)
		select = data['select']
		day = data['day']
		month = data['month']
		year = data['year']
		TemperatureGraphing.webserver_call_individual(select, day, month, year)
		print(data['data'])
		return data['data']
# Every graph wanted
@app.route('/get_every_graph', methods=['POST'])
# Actually update this method to provide functionality
def get_every_graph():
	if request.method == 'POST':
		data = json.loads(request.data)
		day = data['day']
		month = data['month']
		year = data['year']
		TemperatureGraphing.webserver_call_all(day, month, year)
		print(data['data'])
		return data['data']

# Update username and password for website login
@app.route('/update_user_passwd', methods=['POST'])
# Actually update this method to provide functionality
def update_user_passwd():
	if request.method == 'POST':
		data = json.loads(request.data)
		user = data['user']
		new_user = data['new_user']
		passwd = data['passwd']
		new_passwd = data['new_passwd']
		accountAccess.passChange(user, passwd, new_passwd)
		accountAccess.userChange(user, passwd, new_user)
		print(data['data'])

		return data['data']

# Update user defined temperature for house / room
@app.route('/update_desired_temperature', methods=['POST'])
# Actually update this method to provide functionality
def update_desired_temperature():
	if request.method == 'POST':
		data = json.loads(request.data)
		print(data['data'])
		return data['data']

# UNSURE IF THIS IS NEEDED
# Update user defined temperature for house / room
@app.route('/send_data', methods=['GET'])
# Actually update this method to provide functionality
def send_data():
	if request.method == 'GET':
		return 'Data Sent!!!'

# curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:5000/post' -d '{"data":"I am the data!"}'

