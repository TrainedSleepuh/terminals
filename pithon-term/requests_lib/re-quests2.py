import requests
from termcolor import colored

print(colored('''

-------------------------------------------------------------------------------------------
payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)
-------------------------------------------------------------------------------------------
payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
r_dict = r.json()
-------------------------------------------------------------------------------------------
#r = requests.get('http://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
-------------------------------------------------------------------------------------------
r = requests.get('https://httpbin.org/delay/7', timeout=3)
-------------------------------------------------------------------------------------------
[PRINT FUNCTION EXAMPLES]
#print(r.text)
#print(r.url)
#print(r.json())
#print(r_dict['form'])
print(r)
-------------------------------------------------------------------------------------------

''', 'red'))

