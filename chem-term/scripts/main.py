from termcolor import colored
import os

welcome = colored('''
  ____ ___  __  __ ____  _   _ _____  _  _____ ___ ___  _   _    _    _     
 / ___/ _ \|  \/  |  _ \| | | |_   _|/ \|_   _|_ _/ _ \| \ | |  / \  | |    
| |  | | | | |\/| | |_) | | | | | | / _ \ | |  | | | | |  \| | / _ \ | |    
| |__| |_| | |  | |  __/| |_| | | |/ ___ \| |  | | |_| | |\  |/ ___ \| |___ 
 \____\___/|_|  |_|_|    \___/  |_/_/   \_\_| |___\___/|_| \_/_/   \_\_____|
                                                                            
  ____ _   _ _____ __  __ ___ ____ _____ ______   __
 / ___| | | | ____|  \/  |_ _/ ___|_   _|  _ \ \ / /
| |   | |_| |  _| | |\/| || |\___ \ | | | |_) \ V / 
| |___|  _  | |___| |  | || | ___) || | |  _ < | |  
 \____|_| |_|_____|_|  |_|___|____/ |_| |_| \_\|_|  
                                                    
''', 'magenta')
print(welcome)
term = ('''--------
[1]ALL
[!]PERIODIC TABLE
--------
''')
print(term)
all_input = input('''<><><>---->''')
if all_input == '1':
    os.system('clear')
    os.system('python /home/puta/CRAZY/terminals/chem-term/scripts/all_of_it/all_of_it.py')
if all_input == '!':
    os.system('clear')
    os.system('python /home/puta/CRAZY/terminals/chem-term/scripts/periodic_table/p_table.py')