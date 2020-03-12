
import sys
from pymongo import MongoClient

Client = MongoClient()
db = Client["userAccounts"]
collection = db["Accounts"]

users = collection.find()


def login(username, password):
    login_attempt = False
    for user in users:
        if user['username'] == username and user['password'] == password:
            login_attempt = True
    return login_attempt

if __name__ == '__main__':
    attempt = login(sys.argv[1],sys.argv[2])
    print(attempt)