#!/bin/python3

#Excersise 1 & 2
H = input('Enter hours clocked: ')
R = input('Enter rate: ')
try: 
    Hours = float(H)
    Rate = float(R)
    if Hours <= 40:
        Pay = Hours * Rate
        print(Pay)
    else:
        Pay2 = ((Hours - 40) * (Rate * 1.5)) + (40 * Rate)
        print(Pay2)
except: 
    print('Error, please enter numeric input ')

#Excersise 3
Grade = input('Enter score between 0.0 and 1.0: ')
try:
    Score = float(Grade)
    if Score >= 0.9:
        print('A')
    elif Score >= 0.8:
        print('B')
    elif Score >= 0.7:
        print('C')
    elif Score >= 0.6:
        print('D')
    elif Score < 0.6:
        print('F')
except:
    print('Not a score')
    


