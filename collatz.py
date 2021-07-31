#!/usr/bin/env python
# coding: utf-8

# # [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)

print("Enter an integer, then press Enter")
number = input() #this grabs what was entered and converts it to an integer so we can math with it
increment = 1 #this tracks the number of increments

print("---")

if number != "":
    number = int(number)
    while number > 1:
        
        if number % 2 == 0:
            nextnumber = int(number / 2)
            #print(str(increment) + ": " + str(number) + " is EVEN; (" + str(number) + " / 2) = " + str(nextnumber)) 
        else:
            nextnumber = (number * 3) + 1
            #print(str(increment) + ": " + str(number) + " is ODD; (" + str(number) + " * 3) + 1 = " + str(nextnumber)) 
        
        print(str(increment) + ": " + str(number) + " -> "+ str(nextnumber))

        number = nextnumber
        increment += 1

print("Done")