from termcolor import colored

subprocess_yuh = colored('''

import subprocess

#p1 = subprocess.run(['ls', '-la'])    # If your on windows, also put shell=True

#p1 = subprocess.run(['ls', '-la'], capture_output=True, text=True)

#p1 = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True)

with open('output.txt', 'w') as f:
    p1 = subprocess.run(['ls', '-la'], stdout=f, text=True)

#print(p1)
#print(p1.args)
#print(p1.returncode) # 0 means ran successfully
#print(p1.stdout)
#print(p1.stdout.decode())

''', 'red')
print(subprocess_yuh)









