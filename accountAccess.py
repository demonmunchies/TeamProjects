
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

def passChange(username,password,newpass):
    change = False
    for user in users:
        if user['username'] == username and user['password'] == password:
            user['password'] = newpass
            change = True
    return change

def userChange(username,password,newuser):
    change = False
    for user in users:
        if user['username'] == username and user['password'] == password:
            user['username'] = newuser
            change = True
    return change

if __name__ == '__main__':
    attempt = login(sys.argv[1],sys.argv[2])
    print(attempt)

