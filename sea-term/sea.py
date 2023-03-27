from termcolor import colored
import os

term = colored('''
[1]SIMPLE NEURAL NETWORK *no libs*
''', 'green')
print(term)
in_put = input('<>--->')
if in_put == '1':
    os.system('cat neural-network.c')
    print('\n\n')
    print('-' * 25)
    print('NEURAL NETWORK CODE OUTPUT\n')
    os.system('./nn')
