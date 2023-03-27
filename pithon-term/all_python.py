import os
from termcolor import colored

all_python = colored('''
<1><requests>
<2><twisted>
<3><pyfiglet/termcolor>
<4><tkinter>
<5><subprocess>
<6><networkX>
<7><date & time>
<8><ctypes>
<9><argparse>
''', 'yellow')
print(all_python)
all_python_input = input('<all python>--->')

if all_python_input == '1':
    os.system('python /home/puta/CRAZY/terminals/pithon-term/requests_lib/re-quests.py')
    next_page = input('NEXT PAGE? [Y/n]')
    if next_page == 'Y':
        os.system('clear')
        os.system('python /home/puta/CRAZY/terminals/pithon-term/requests_lib/re-quests2.py')
        os.system('python main_terminal.py')
    if next_page == 'y':
        os.system('clear')
        os.system('python /home/puta/CRAZY/terminals/pithon-term/requests_lib/re-quests2.py')
        os.system('python main_terminal.py')
    if next_page == 'n':
        os.system('clear')
        os.system('python main_terminal.py')

if all_python_input == '3':
    os.system('clear')
    os.system('python /home/puta/CRAZY/terminals/pithon-term/pyfig_lib/pyfig-termco.py')

if all_python_input == '4':
    os.system('clear')
    os.system('python /home/puta/CRAZY/terminals/pithon-term/tkinter_lib/tkin_for_term2.py')
    os.system('python /home/puta/CRAZY/terminals/pithon-term/tkinter_lib/tkinter_for_term.py')

if all_python_input == '5':
    os.system('clear')
    os.system('python /home/puta/CRAZY/terminals/pithon-term/subprocess_lib/sub-process.py')

if all_python_input == '6':
    os.system('clear')
    os.system('cat /home/puta/CRAZY/terminals/pithon-term/networkx_lib/Net-work-X.py')

if all_python_input == '7':
    os.system('clear')
    os.system('python /home/puta/CRAZY/terminals/pithon-term/date_and_time_lib/date_and_time.py')

if all_python_input == '9':
    os.system('clear')
    os.system('cat argparse_lib/argparse_for_term.py')
    print('\n------------------------------------------------')
    print()
    run_file = input('PICK A NUM FOR FIB CALCULATION <5, 8, 10, 13, 15, -h, -o -v>---> ')
    if run_file == '5':
        os.system('python argparse_lib/argparse_for_term.py 5')
    if run_file == '8':
        os.system('python argparse_lib/argparse_for_term.py 8')
    if run_file == '10':
        os.system('python argparse_lib/argparse_for_term.py 10')
    if run_file == '13':
        os.system('python argparse_lib/argparse_for_term.py 13')
    if run_file == '15':
        os.system('python argparse_lib/argparse_for_term.py 15')
    if run_file == '-h':
        os.system('python argparse_lib/argparse_for_term.py -h')
    if run_file == '-o':
        os.system('python argparse_lib/argparse_for_term.py -o')
    if run_file == '-v':
        os.system('python argparse_lib/argparse_for_term.py -v')

if all_python_input == '8':
    os.system('clear')
    os.system('echo Here is the C code')
    print()
    os.system('cat /home/puta/CRAZY/terminals/pithon-term/ctypes_lib/clibrary.c')
    print('\n')
    runn = input('Run the file [Y/n]?')
    if runn == 'Y':
        os.system('python /home/puta/CRAZY/terminals/pithon-term/ctypes_lib/ctypes_term.py')
    
if all_python_input == '2':
    os.system('clear')
    print('''
<1><twisted server/client>
<2><twisted peer 2 peer server/client>
    ''')
    twstd = input('<twisted>--->')
    if twstd == '1':
        os.system('clear')
        os.system('python /home/puta/CRAZY/terminals/pithon-term/twisted_lib/twisted-server.py')
        next_page2 = input('WANNA SEE CLIENT SIDE NOW? [Y/n]')
        if next_page2 == 'Y':
            os.system('clear')
            os.system('python /home/puta/CRAZY/terminals/pithon-term/twisted_lib/twisted-client.py')
            both_seen = input('<python>--->')
            if both_seen == 'home':
                os.system('clear')
                os.system('python all_python.py')
        if next_page2 == 'y':
            os.system('clear')
            os.system('python /home/puta/CRAZY/terminals/pithon-term/twisted_lib/twisted-client.py')
            both_seen = input('<python>--->')
            if both_seen == 'home':
                os.system('clear')
                os.system('python all_python.py')
        if next_page2 == 'n':
            os.system('clear')
            os.system('python all_python.py')
    if twstd == '2':
        os.system('clear')
        os.system('python /home/puta/CRAZY/terminals/pithon-term/twisted_lib/twistedp2p-server.py')
        y_n = input('NEXT PAGE? [Y/n]')
        if y_n == 'Y':
            os.system('clear')
            os.system('python /home/puta/CRAZY/terminals/pithon-term/twisted_lib/twistedp2p-client.py')
            bof_seen = input('<type home to exit>--->')
            if bof_seen == 'home':
                os.system('clear')
                os.system('python main_terminal.py')
        if y_n == 'y':
            os.system('clear')
            os.system('python /home/puta/CRAZY/terminals/pithon-term/twisted_lib/twistedp2p-client.py')
            bof_seen = input('<type home to exit>--->')
            if bof_seen == 'home':
                os.system('clear')
                os.system('python main_terminal.py')
        if y_n == 'n':
            os.system('clear')
            os.system('python main_terminal.py')


