import sys
sys.path.append('./api/handlers')
import handleOptions
from simple_term_menu import TerminalMenu

class SelectionMenu():
    def mainMenu():
        mainOptions = ["[a]Send mail", "[b]Check mails", "[c]Users", "[d]Clear Users", "[e]Logout"]
        terminal_menu = TerminalMenu(mainOptions)
        menu_entry_index = terminal_menu.show()
        handleOptions.HandleMainOptions(menu_entry_index)
        
