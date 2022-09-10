#!/usr/bin/env python3.x
import pyfiglet
import time
import json
from data.mails_data import mails
from api.login import Login

with open('./data/mails.json', 'w') as outfile:
    mails_obj = json.dumps(mails, indent=4)
    outfile.write(mails_obj)

def drawWelcomeScreen():
    result = pyfiglet.figlet_format("Fr._. Mail")
    print(result)

drawWelcomeScreen()
time.sleep(2)

Login()
