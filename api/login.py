import json
import sys
import time
import os
sys.path.append('./api/interface/')
sys.path.append('./data')
import index
import login_data



def Login():
    with open("./data/credentials.json", 'r') as f:
        data = json.load(f)
    if data["username"] != '':
        index.SelectionMenu.mainMenu()
    else:
        print(data["username"])
        username = str(input("Username:"))
        login_data.login_data["username"] = str(username)
        login_obj = json.dumps(login_data.login_data, indent=4)
        with open("./data/credentials.json", "w") as outfile:
            outfile.write(login_obj)
            print(f" Welcome {username}🎉")
        with open('./data/users.json', 'r') as infile:
            users_dict = json.load(infile)
            usernames = users_dict["usernames"]
        usernames.append(username)
        username_obj = json.dumps(users_dict, indent=4)
        with open('./data/users.json', 'w') as outfile:
            outfile.write(username_obj)
            time.sleep(.2)
        os.system("clear")
        index.SelectionMenu.mainMenu()


    

