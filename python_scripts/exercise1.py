# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = 1
string = "string example"
5>2
print(5>2)
print(x)
print(string)


while x < 11:
    print(x)
    x +=1

i = -1
while i > -11:
    print(i)
    i += -1


    
guess = int(input("Enter a number: "))
j = 0
for i in range(0, guess+1):
    j = j+i
    print(j)
print("The sum of all numbers up to your guess is " , j)
        