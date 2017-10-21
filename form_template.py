#TEMPLATE USER
#-add users to main dict using on signup inputs
#-add events to event dict using "make listing" inputs
#-login checks username['password'] against password input
from security import *
users = {
	username: {"name": "",
                   "location": "",
	           "age": 0,
	           "gender": "",
	           "email": "",
	           "password": "", #hashed
	           "msg_link": ""
                   "events" : { "event1" :
                       {"time" : "00:00",
                        "description" : ""
                   }
        }
                
def login_verif(user,pword):
        
"""
simple check if password is correct,
if password is wrong print an error and clear inputs
"""
        enc_pword=encrypt(pword)
        if enc_pword==user['password']:
            return True
        else:
            return False
        
