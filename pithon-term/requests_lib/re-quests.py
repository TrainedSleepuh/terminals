import requests
from termcolor import colored

print(colored('''

-----------------------------------------------------------------------------------------------------
[TOO INSTALL]
pip install requests
-----------------------------------------------------------------------------------------------------
[THE WEBSITES ARE JUST EXAMPLES]
[EXAMPLE 1]
r = requests.get('https://xkcd.com/353/')
print(r.text) # Gets the html code
-----------------------------------------------------------------------------------------------------
[EXAMPLE 2]
r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.content) # Prints bytes of image
with open('comic.png', 'wb') as f: # wb is write bytes
    f.write(r.content) # gets the picture created
-----------------------------------------------------------------------------------------------------
[PRINT FUNCTION EXAMPLES]
print(r.status_code) # 200 is success, 300 is redirects, 400 is errors, and 500 is server errors
print(r.ok) # anything under a 400 will give it a True
print(r.headers) # prints out all the headers
-----------------------------------------------------------------------------------------------------

''', 'red'))
