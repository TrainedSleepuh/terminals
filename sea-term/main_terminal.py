import os
import pyfiglet
from termcolor import colored

sea_banner = colored(pyfiglet.figlet_format("C C++ C#"), 'green')
print(sea_banner)
sea_term = colored('''
------C-C++-C#-------
[1]C
[2]C++
[3]C#
-----TERMINAL----
''', 'green')
print(sea_term)
sea_input = input('<>--->')
if sea_input == '1':
    os.system('clear')
    os.system('python sea.py')
if sea_input == '2':
    os.system('clear')
    os.system('python seaplusplus.py')
if sea_input == '3':
    os.system('clear')
    os.system('python seasharp.py')