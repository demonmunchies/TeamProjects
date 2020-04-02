import sys
from pymongo import MongoClient
import hashlib

Client = MongoClient()
db = Client["userAccounts"]
collection = db["Accounts"]

users = collection.find()


def login(username, password):
    """Try to login with given credentials: username, password. Returns True if successful"""
    login_attempt = False

    passStr = password.encode('utf-8')
    passCrypt = hashlib.pbkdf2_hmac('sha256',passStr,b'TeamProjectsSalt',10000)
    find_result = collection.find_one({"username": username, "password":passCrypt.hex()})
    if find_result is not None:
        login_attempt = True
    return login_attempt

def passChange(username,password,newpass):
    """Change password given: username, password, new password"""
    change = False

    passStr = password.encode('utf-8')
    passCrypt = hashlib.pbkdf2_hmac('sha256',passStr,b'TeamProjectsSalt',10000)
    newpassStr = newpass.encode('utf-8')
    newpassCrypt = hashlib.pbkdf2_hmac('sha256',newpassStr,b'TeamProjectsSalt',10000)
    collection.find_one_and_update({"username": username, "password":passCrypt.hex()},{'$set': {"password":newpassCrypt.hex()}})
    if collection.find_one({"username": username, "password":newpassCrypt.hex()}) is not None:
        change = True
    return change

def userChange(username,password,newuser):
    """Change username given: username, password, new username"""
    change = False

    passStr = password.encode('utf-8')
    passCrypt = hashlib.pbkdf2_hmac('sha256',passStr,b'TeamProjectsSalt',10000)
    collection.find_one_and_update({"username": username, "password":passCrypt.hex()},{'$set': {"username":newuser}})
    if collection.find_one({"username": newuser, "password":passCrypt.hex()}) is not None:
        change = True
    return change

# Uncomment to test initial login
# if __name__ == '__main__':
#     attempt = login(sys.argv[1],sys.argv[2])
#     print(attempt)


# TEST CASES: Also resets all to default
# print(login('default','default'))
# print(passChange('default','default','default1'))
# print(userChange('default','default1','default1'))
# print(passChange('default1','default1','default'))
# print(userChange('default1','default','default'))