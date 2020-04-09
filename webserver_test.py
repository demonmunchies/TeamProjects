from flask import Flask
from flask import request
from flask import jsonify
import TemperatureGraphing
import ScheduleData
import accountAccess
from flask_cors import CORS
from flask_socketio import SocketIO
import json
app = Flask(__name__)
cors = CORS(app)
socketio = SocketIO(app)


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

@app.route('/get_schedule', methods=['GET'])
def get_schedule():
	if request.method == 'GET':
		return jsonify(ScheduleData.getSchedule())

@app.route('/update_schedule', methods=['POST'])
def update_schedule():
	if request.method == 'POST':
		data = json.loads(request.data)
		schedule = data['schedule']
		ScheduleData.updateSchedule(schedule)
		print(data)
		return data

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
		TemperatureGraphing.main(select, day, month, year)
		print(data)
		return data
# Every graph wanted
# @app.route('/get_every_graph', methods=['POST'])
# # Actually update this method to provide functionality
# def get_every_graph():
# 	if request.method == 'POST':
# 		data = json.loads(request.data)
# 		day = data['day']
# 		month = data['month']
# 		year = data['year']
# 		#TemperatureGraphing.webserver_call_all(day, month, year)
# 		print(data['data'])
# 		return data['data']

# Update username and password for website
@app.route('/update_passwd', methods=['POST'])
# Actually update this method to provide functionality
def update_user_passwd():
	if request.method == 'POST':
		data = json.loads(request.data)
		user = data['user']
		passwd = data['passwd']
		new_passwd = data['new_passwd']
		sucessful = accountAccess.passChange(user, passwd, new_passwd)
		print(data)
		print(sucessful)

		return jsonify(sucessful)

@app.route('/login', methods=['POST'])
def login():
	if request.method == 'POST':
		data = json.loads(request.data)
		user = data['user']
		passwd = data['passwd']
		sucessful = accountAccess.login(user, passwd)
		print(data)
		print(sucessful)
		
		return jsonify(sucessful)

# Update user defined temperature for house / room
@app.route('/update_desired_temperature', methods=['POST'])
# Actually update this method to provide functionality
def update_desired_temperature():
	if request.method == 'POST':
		data = json.loads(request.data)
		temp = data['data']
		print(data)
		return data

# UNSURE IF THIS IS NEEDED
# Get current temperature
@app.route('/get_temperature', methods=['GET'])
# Actually update this method to provide functionality
def send_data():
	if request.method == 'GET':
		return '72'

if __name__ == '__main__':
    socketio.run(app)

# curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:5000/post' -d '{"data":"I am the data!"}'

