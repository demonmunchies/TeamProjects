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

# curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:5000/post' -d '{"data":"I am the data!"}'

