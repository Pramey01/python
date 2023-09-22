#!/bin/python3

#Exersise 1
import random

for i in range(10):
    x = random.random()
    print(x)

#Exersise 2 & 3
def print_lyrics():
    print ("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

#Exersise 4
#D

#Exersise 5
#D

#Exersise 6
def compute_pay(hours,rate):
    try: 
        if hours <= 40:
            pay = hours * rate
            print(pay)
        else:
            overtimePay = ((hours - 40) * (rate * 1.5)) + (40 * rate)
            print(overtimePay)
    except: 
        print('Error, please enter numeric input ')
compute_pay(45,10)

#Exersise 7
def compute_grade():
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
compute_grade()