import json
import sys
import os
import time
import getch
sys.path.append('./data')
sys.path.append('./api/interface')
sys.path.append('./api')
import mails_data, users_data, login_data
import login
import index

def send():
    with open('./data/users.json', 'r') as f:
        users = json.load(f)
    reciever = str(input("Recievers username:"))
    message = str(input("message:"))
    if reciever in users["usernames"]:
        with open('./data/mails.json', 'r') as f:
            mails = json.load(f)
        mails[reciever] = message
        mails_obj = json.dumps(mails, indent=4)
        with open('./data/mails.json', 'w') as outfile:
            outfile.write(mails_obj)
        print(f"message => '{message}' successfully sent to {reciever}!")
        outfile.close()
        f.close()
        time.sleep(0.3)

        os.system("clear")
        index.SelectionMenu.mainMenu()
    else:
        print(f'{reciever} not found!')
        time.sleep(0.3)
        os.system("clear")
        index.SelectionMenu.mainMenu()

def inbox():
    with open('./data/credentials.json', 'r') as r:
        credentials = json.load(r)
        username = credentials["username"]
    with open('./data/mails.json', 'r') as f:
        mails = json.load(f)
    for m in mails.values():
        message = m
        print(f'-->[{username}] says {message}')
    print("type <q> or <b> key to go back", end=' ',flush=True)
    char = getch.getche()

    if char == 'q' or 'b':
        r.close()
        f.close()
        os.system("clear")
        index.SelectionMenu.mainMenu()

    
def logout():
    print("Are you sure you wanna logout? Press y")
    char = getch.getche()
    if char == 'y':
        login_data.login_data["username"] = ""
        login_data.login_data["password"] = ""
        login_obj = json.dumps(login_data.login_data, indent=4)
        with open('./data/credentials.json', 'w') as outfile:
            outfile.write(login_obj)
        print("Goodbye!")
        time.sleep(0.3)
        os.system("clear")
        outfile.close()
        login.Login()
    else:
        os.system("clear")
        index.SelectionMenu.mainMenu()

def users():
    os.system("clear")
    print("Available users:")
    with open('./data/users.json', 'r') as f:
        users = json.load(f)
    for x in users["usernames"]:
        user = x
        print(f'-->{user}')
    print('Press <q> or <b> to go back')
    char = getch.getche()
    if char == 'q' or 'b':
        os.system("clear")
        index.SelectionMenu.mainMenu()

def clearUsers():
    os.system("clear")
    print("Are you sure you wanna delete all users? Type <y>")
    char = getch.getch()
    if char == 'y':
        usernames = users_data.users
        users_obj = json.dumps(usernames)
        with open('./data/users.json', 'w') as outfile:
            outfile.write(users_obj)
        print("Succesfully deleted users!")
        time.sleep(0.2)
        os.system("clear")
        logout()
        os.system("clear")

    else:
        os.system("clear")
        index.SelectionMenu.mainMenu()
