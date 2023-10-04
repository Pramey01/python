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
        #This error will never run since you are not prompting the user for input, therefore they are incapable of inputing the wrong type of information
        print('Error, please enter numeric input ')
#add a user input for this with something like inputeHours = input('gimme the hours ye worked'), inputRate = input('how much is your time worth?')
#then you can call the function compute_pay(inputHours, inputRate) 
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
