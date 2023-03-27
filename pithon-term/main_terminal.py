import os
from termcolor import colored
import pyfiglet

banner_main = colored(pyfiglet.figlet_format("PYTHON"), 'yellow')

terminal_layout = colored('''  
----------PYTHON------------
[!]ALL PYTHON
[@]
[#]
[$]FILES
[%]
[^]GUI
[&]CHEAT SHEETS
[*]
---------TERMINAL-----------
''', 'yellow')
print(banner_main)
print(terminal_layout)
terminal_input = input('<python>--->')

if terminal_input == '!':
    os.system('clear')
    os.system('python all_python.py')

if terminal_input == '^':
    os.system('clear')
    script_window = input("Wanna see the script or window? or both???")
    if script_window == 'script':
        os.system('clear')
        os.system('python /home/puta/CRAZY/terminals/pithon-term/tkinter_lib/tkin_for_term2.py')
        leave = input("<gui>--->")
        if leave == 'home':
            os.system('clear')
            os.system('python main_terminal.py')
    if script_window == 'window':
        os.system('clear')
        os.system('python /home/puta/CRAZY/terminals/pithon-term/tkinter_lib/tkinter_for_term.py')
        leave1 = input("<gui>--->")
        if leave1 == 'home':
            os.system('clear')
            os.system('python main_terminal.py')
    if script_window == 'both':
        os.system('clear')
        os.system('python /home/puta/CRAZY/terminals/pithon-term/tkinter_lib/tkin_for_term2.py')
        os.system('python /home/puta/CRAZY/terminals/pithon-term/tkinter_lib/tkinter_for_term.py')
        leave = input("<gui>--->")
        if leave == 'home':
            os.system('clear')
            os.system('python main_terminal.py')

if terminal_input == 'languages':
    os.system('clear')
    print(colored('''
<german>
    ''', 'blue'))
    lang = input('<languages>--->')
    if lang == 'german':
        os.system('clear')
        os.system('cat /home/puta/CRAZY/terminals/pithon-term/languages_for_no_reason/german.txt')
        done = input('<languages>--->')
        if done == 'home':
            os.system('clear')
            os.system('python main_terminal.py')

if terminal_input == '$':
    os.system('clear')
    ask = input('''
--------------------------------------
  DO YOU WANT TO CREATE A FILE? [Y/n] 
--------------------------------------
<python>--->''')
    if ask == 'Y':
        ask_file = input('What is your file name going to be?:')
        with open(ask_file, 'w') as f:
            f.write(input('TYPE BELOW\n'))
            lol = True
            if lol == True:
                print('Make sure your file is in the system')
                os.system('ls')
                file_input = input('<python>--->')
                if file_input == 'home':
                    os.system('clear')
                    os.system('python main_terminal.py')
    if ask == 'y':
        ask_file = input('What is your file name going to be?:')
        with open(ask_file, 'w') as f:
            f.write(input('TYPE BELOW\n'))
            lol = True
            if lol == True:
                print('Make sure your file is in the system')
                os.system('ls')
                file_input2 = input('<python>--->')
                if file_input2 == 'home':
                    os.system('clear')
                    os.system('python main_terminal.py')
    if ask == 'n':
        file_input3 = input('Do you wanna edit a file? [Y/n]')
        if file_input3 == 'Y':
            os.system('clear')
            os.system('clear')
            print('-' * 100)
            print('IF YOU WANNA FUCK UP THE PROGRAM GO AHEAD AND EDIT THE ONES YOU DONT KNOW ABOUT TWAT')
            print('-' * 100)
            print()
            print('Which file do you want to open?')
            print()
            os.system('ls')
            print('-' * 100)
            print('type command like your going to run the file in terminal')
            print()
            input1 = input('<python>--->')
            os.system(input1)
            print('WHATEVER YOU DID WORKED! NOW TYPE HOME TO GET OUT OF HERE YOU HONKEY ASS MOTHERFUCKER')
            input2 = input('<python>--->')
            if input2 == 'home':
                os.system('clear')
                os.system('python main_terminal.py')
            if input2 == 'HOME':
                os.system('clear')
                os.system('python main_terminal.py')
        if file_input3 == 'y':
            os.system('clear')
            os.system('clear')
            print('-' * 100)
            print('IF YOU WANNA FUCK UP THE PROGRAM GO AHEAD AND EDIT THE ONES YOU DONT KNOW ABOUT TWAT')
            print('-' * 100)
            print()
            print('Which file do you want to open?')
            print()
            os.system('ls')
            print('-' * 100)
            print('type command like your going to run the file in terminal')
            print()
            input1 = input('<python>--->')
            os.system(input1)
            print('WHATEVER YOU DID WORKED! NOW TYPE HOME TO GET OUT OF HERE YOU HONKEY ASS MOTHERFUCKER')
            input2 = input('<python>--->')
            if input2 == 'home':
                os.system('clear')
                os.system('python main_terminal.py')
            if input2 == 'HOME':
                os.system('clear')
                os.system('python main_terminal.py')
                
if terminal_input == '&':
    os.system('clear')
    os.system('open /home/puta/CRAZY/terminals/pithon-term/html_for_py_term/cheatsheets.html')
else:
    print('Fuck Outa Here! Go learn Scratch Pussy')