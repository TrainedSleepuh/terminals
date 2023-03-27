from termcolor import colored
import os

cplustymestwo = colored('''
----------------------
[1]WRITING HELLO WORLD
[2]OBJECT ORIENTED PROGRAMMING
[3]SERVER/CLIENT
----------------------
''', 'green')
print(cplustymestwo)
seaplusxtwo = input('<>--->')
if seaplusxtwo == '1':
    cplusplus = colored('''
---> .cpp will be the c++ file
---> command to run cpp file ---> g++ file.cpp -o file

---> LETS WRITE HELLO WORLD
#include <iostream>
using namespace std;
int main()
{
    cout << "Hallo Welt!" << endl;
}

''', 'blue')
    print(cplusplus)
    cplusx2two = input("WANNA RUN FILE? [Y/n]")
    if cplusx2two == 'Y':
        os.system('./hello')
    if cplusx2two == 'y':
        os.system('./hello')
    if cplusx2two == 'n':
        os.system('clear')
        os.system('python main_terminal.py')

if seaplusxtwo == '2':
    oop = ('''
    [1]FILE 1
    [2]FILE 2
    ''')
    print(oop)
    oop_input = input('<>--->')
    if oop_input == '1':
        os.system('cat oop1.cpp')
        print('\n\n')
        print('-' * 25)
        print('OUTPUT\n')
        os.system('./oop1')
    if oop_input == '2':
        os.system('cat oop2.cpp')
        print('\n\n')
        print('-' * 25)
        print('OUTPUT\n')
        os.system('./oop2')

if seaplusxtwo == '3':
    print('SERVER SIDE[s]\nCLIENT SIDE[c]\nBOTH[b]')
    serv_cli = input('<>--->')
    if serv_cli == 's':
        os.system('cat cplusplus-server.cpp')
    if serv_cli == 'c':
        os.system('cat cplusplus-client.cpp')
    if serv_cli == 'b':
        print('[ SERVER CODE ]\n\n')
        os.system('cat cplusplus-server.cpp')
        print('\n\n')
        print(' [ CLIENT CODE ]\n\n')
        os.system('cat cplusplus-client.cpp')