#!/bin/python3

#Excersise 1 & 2
hours = float(input('Enter hours clocked: '))
rate = float(input('Enter rate: '))
try: 
    if hours <= 40:
        pay = hours * rate
        print(pay)
    else:
        #naming variables can be difficult at the beginning but inputing pay2 can be confusing. Especially if someone else is looking at the code in the future or pay2 is called somewhere farther along the program away from its declaration
        overtimePay = ((hours - 40) * (rate * 1.5)) + (40 * rate)
        print(overtimePay)
except: 
    print('Error, please enter numeric input ')

#Excersise 3
grade = input('Enter score between 0.0 and 1.0: ')
try:
    score = float(grade)
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score < 0.6:
        print('F')
except:
    print('Not a score')
    


