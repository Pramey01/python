#!/bin/python3

#Exersise 1 & 2

total = 0
count = 0
average = 0
maximum = 0
minimum = 0
while True: 
    number = input('Enter a number: ')
    if number == "done":
        break
    x = float(number)
    try:
        if count == 0:
            maximum = x
            minimum = x
        elif x > maximum:
            maximum = x
        elif x < minimum:
            minimum = x
        total += x
        count = count + 1
        average = total / count
    except:
        print ("Invalid input")
        continue
print("total:",total,"count:",count,"average:",average,"maximum:",maximum,"minimum:",minimum)
