#!/bin/python3

#Exersise 1
#Add comments to explain the expected output/input for the functions
#As the complexity of the application raise these practices will make maintenance and collaboration better
#most imporants can have aliases. These can make it easier to type or explain what the library is doing.
#Here is okay to have imported the library without an alias since you are using the entire library and none of the specific sub-functionality
import random

for i in range(10):
#python likes to use single character variables. This is not the best practice generally 
    randomSelection = random.random()
    print(randomSelection)

#Exersise 2 & 3
#Consider using a loop in the function so you don't have to call the function twice
#the function print lyrics will print the statement as many times as the range defines
def print_lyrics():
    for i in range(5):
        print ("I'm a lumberjack, and I'm okay.")
        print('I sleep all night and I work all day.')

print_lyrics()

#Exersise 4
#D

#Exersise 5
#D

#Exersise 6
hours = input('Enter hours worked: ')
rate = input("Whatcha makin' bacon: ")
#user inputs hours worked and wage and the computepay function gets their earnings also calculates overtime
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
compute_pay(hours,rate)

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
