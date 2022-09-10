import handleFunctions
import sys
sys.path.append('./api')

def HandleMainOptions(index):
    if index == 0:
        handleFunctions.send()
    if index == 1:
        handleFunctions.inbox()
    if index == 2:
        handleFunctions.users()
    if index == 3:
        handleFunctions.clearUsers()
    if index == 4:
        handleFunctions.logout()
