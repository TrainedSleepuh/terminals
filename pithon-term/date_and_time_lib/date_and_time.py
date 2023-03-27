from termcolor import colored
import os
import calendar
from datetime import datetime
import pyfiglet

all_months = colored('''
{------------------}
{1}  JANUARY     {1}
{2}  FEBURARY    {2}
{3}  MARCH       {3}
{4}  APRIL       {4}
{5}  MAY         {5}
{6}  JUNE        {6}
{7}  JULY        {7}
{8}  AUGUST      {8}
{9}  SEMPTEMBER  {9}
{10} OCTOBER     {10}
{11} NOVEMBER    {11}
{12} DECEMBER    {12}
{-------------------}
''', 'red')
print(all_months)
months_input = input("<calendar>--->")
if months_input == '1':
    os.system('clear')
    janu = pyfiglet.figlet_format('JANUARY')
    print(colored(janu, 'blue'))
    now = datetime.now()
    print("\nCLOCK:", now, "\n")
    jan = calendar.TextCalendar(calendar.SUNDAY)
    one = jan.formatmonth(2023, 1)
    print(colored(one, 'blue'))

    with open('january.txt', 'w') as f:
        f.write("-" * 50)
        f.write('''\nJANUARY SCHEDULE\nDAY 1:\nDAY 2\nDAY 3\nDAY 4\nDAY 5\n
DAY 6\nDAY 7\nDAY 8\nDAY 9\nDAY 10\nDAY 11\nDAY 12\nDAY 13\nDAY 14\nDAY 15\n
DAY 16\nDAY 17\nDAY 18\nDAY 19\nDAY 20\nDAY 21\nDAY 22\nDAY 23\nDAY 24\nDAY 25\nDAY 26\n
DAY 27\nDAY 28\nDAY 29\nDAY 30\nDAY 31\n''')
        f.write("-" * 50)
    file_open = input("EDIT SCHEDULE? [yes/no]")
    while True:
        if file_open == 'yes':
            os.system('mousepad january.txt')

    home_ski = input("<type home to go back>--->")
    if home_ski == 'home':
        os.system('clear')
        os.system('python date_and_time.py')
if months_input == '2':
    os.system('clear')
    febu = pyfiglet.figlet_format('FEBUARY')
    print(colored(febu, 'blue'))
    now = datetime.now()
    print("\nCLOCK:", now, "\n")
    feb = calendar.TextCalendar(calendar.SUNDAY)
    two = feb.formatmonth(2023, 2)
    print(colored(two, 'blue'))
    home_ski = input("<type home to go back>--->")
    if home_ski == 'home':
        os.system('clear')
        os.system('python date_and_time.py')
if months_input == '3':
    os.system('clear')
    marc = pyfiglet.figlet_format('MARCH')
    print(colored(marc, 'blue'))
    now = datetime.now()
    print("\nCLOCK:", now, "\n")
    mar = calendar.TextCalendar(calendar.SUNDAY)
    three = mar.formatmonth(2023, 3)
    print(colored(three, 'blue'))
    home_ski = input("<type home to go back>--->")
    if home_ski == 'home':
        os.system('clear')
        os.system('python date_and_time.py')
if months_input == '4':
    os.system('clear')
    apri = pyfiglet.figlet_format('APRIL')
    print(colored(apri, 'blue'))
    now = datetime.now()
    print("\nCLOCK:", now, "\n")
    apr = calendar.TextCalendar(calendar.SUNDAY)
    four = apr.formatmonth(2023, 4)
    print(colored(four, 'blue'))
    home_ski = input("<type home to go back>--->")
    if home_ski == 'home':
        os.system('clear')
        os.system('python date_and_time.py')
if months_input == '5':
    os.system('clear')
    maye = pyfiglet.figlet_format('MAY')
    print(colored(maye, 'blue'))
    now = datetime.now()
    print("\nCLOCK:", now, "\n")
    may = calendar.TextCalendar(calendar.SUNDAY)
    five = may.formatmonth(2023, 5)
    print(colored(five, 'blue'))
    home_ski = input("<type home to go back>--->")
    if home_ski == 'home':
        os.system('clear')
        os.system('python date_and_time.py')
if months_input == '6':
    os.system('clear')
    junee = pyfiglet.figlet_format('JUNE')
    print(colored(junee, 'blue'))
    now = datetime.now()
    print("\nCLOCK:", now, "\n")
    jun = calendar.TextCalendar(calendar.SUNDAY)
    six = jun.formatmonth(2023, 6)
    print(colored(six, 'blue'))
    home_ski = input("<type home to go back>--->")
    if home_ski == 'home':
        os.system('clear')
        os.system('python date_and_time.py')
if months_input == '7':
    os.system('clear')
    julyy = pyfiglet.figlet_format('JULY')
    print(colored(julyy, 'blue'))
    now = datetime.now()
    print("\nCLOCK:", now, "\n")
    jul = calendar.TextCalendar(calendar.SUNDAY)
    seven = jul.formatmonth(2023, 7)
    print(colored(seven, 'blue'))
    home_ski = input("<type home to go back>--->")
    if home_ski == 'home':
        os.system('clear')
        os.system('python date_and_time.py')
if months_input == '8':
    os.system('clear')
    augu = pyfiglet.figlet_format('AUGUST')
    print(colored(augu, 'blue'))
    now = datetime.now()
    print("\nCLOCK:", now, "\n")
    aug = calendar.TextCalendar(calendar.SUNDAY)
    eight = aug.formatmonth(2023, 8)
    print(colored(eight, 'blue'))
    home_ski = input("<type home to go back>--->")
    if home_ski == 'home':
        os.system('clear')
        os.system('python date_and_time.py')
if months_input == '9':
    os.system('clear')
    semp = pyfiglet.figlet_format('SEMPTEMBER')
    print(colored(semp, 'blue'))
    now = datetime.now()
    print("\nCLOCK:", now, "\n")
    sem = calendar.TextCalendar(calendar.SUNDAY)
    nine = sem.formatmonth(2023, 9)
    print(colored(nine, 'blue'))
    home_ski = input("<type home to go back>--->")
    if home_ski == 'home':
        os.system('clear')
        os.system('python date_and_time.py')
if months_input == '10':
    os.system('clear')
    octob = pyfiglet.figlet_format('OCTOBER')
    print(colored(octob, 'blue'))
    now = datetime.now()
    print("\nCLOCK:", now, "\n")
    octo = calendar.TextCalendar(calendar.SUNDAY)
    ten = octo.formatmonth(2023, 10)
    print(colored(ten, 'blue'))
    home_ski = input("<type home to go back>--->")
    if home_ski == 'home':
        os.system('clear')
        os.system('python date_and_time.py')
if months_input == '11':
    os.system('clear')
    nove = pyfiglet.figlet_format('NOVEMBER')
    print(colored(nove, 'blue'))
    now = datetime.now()
    print("\nCLOCK:", now, "\n")
    nov = calendar.TextCalendar(calendar.SUNDAY)
    eleven = nov.formatmonth(2023, 11)
    print(colored(eleven, 'blue'))
    home_ski = input("<type home to go back>--->")
    if home_ski == 'home':
        os.system('clear')
        os.system('python date_and_time.py')
if months_input == '12':
    os.system('clear')
    dece = pyfiglet.figlet_format('DECEMBER')
    print(colored(dece, 'blue'))
    now = datetime.now()
    print("\nCLOCK:", now, "\n")
    dec = calendar.TextCalendar(calendar.SUNDAY)
    twelve = dec.formatmonth(2023, 12)
    print(colored(twelve, 'blue'))
    home_ski = input("<type home to go back>--->")
    if home_ski == 'home':
        os.system('clear')
        os.system('python date_and_time.py')