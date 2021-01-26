# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:19:20 2021

@author: User
"""

numbers_list= [26,54,93,17,77,31,44,55,20]

# pseudocode:

maxx = 0  
for number in numbers_list:
    if number > maxx:
        maxx = number

print(maxx)



#python script method
        


#through a function
numbers_list= [26,54,93,17,77,31,44,55,20]
def mymax(numbers_list):
    max1 = numbers_list[0]
    index = 0
    max_index = 0
    for num in numbers_list:
        index += 1
        if num > max1:
            max1 = num
            max_index = index
    return max1, max_index

maximum_number , maximum_index = mymax(numbers_list)

print(maximum_number, maximum_index)

#the maximum number should be placed at the last position in the list
numbers_list= [26,54,93,17,77,31,44,55,20]
length_numbers_list = len(numbers_list) -1
last_position_numbers_list = numbers_list[length_numbers_list]
print(length_numbers_list)
print(last_position_numbers_list)

numbers_list[length_numbers_list] = maximum_number
numbers_list[maximum_index] = last_position_numbers_list

print(numbers_list)




mymax(numbers_list)

# sort a list through a loop
maximum_number = mymax(numbers_list)


    numbers_list.sort()
print(numbers_list)