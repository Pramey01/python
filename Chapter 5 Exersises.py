#!/bin/python3

#Exersise 1 

total = None
count = None
average = None
while True: 
    number = input('Enter a number: ')
    try:
        if number = "done":
            break
        total = float(number)
        count = count + 1
        average = total / count
    except:
        print ("Invalid input")
print("total:",total,"count:",count,"average:",average)

