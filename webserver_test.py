from flask import Flask
from flask import request
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
@app.route('/get_singular_graph', methods='[POST]')
# Actually update this method to provide functionality
def get_singular_graph():
	if request.method == 'POST':
		data = json.loads(request.data)
		print(data['data'])
		return data['data']
# Every graph wanted
@app.route('/get_every_graph', methods='[GET]')
# Actually update this method to provide functionality
def get_every_graph():
	if request.method == 'GET':
		return 'WE BE ALL THE GRAPHS!!!'

# Update username and password for website login
@app.route('/update_user_passwd', methods=['POST'])
# Actually update this method to provide functionality
def update_user_passwd():
	if request.method == 'POST':
		data = json.loads(request.data)
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
@app.route('/send_data?', methods=['GET'])
# Actually update this method to provide functionality
def send_data?():
	if request.method == 'GET':
		return 'Data Sent!!!'

# curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:5000/post' -d '{"data":"I am the data!"}'

