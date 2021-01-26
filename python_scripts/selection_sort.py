#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:25:21 2021

@author: ab2018
"""

#find maximum number in list 
#defining the list of numbers
number_list = [26, 54, 93, 17, 77, 31, 44, 55, 20]
#define a function: the aximum in any given list
def mymax(list1):
    max1 = list1[0],
    index = 0
    print(list1)
    max_index = 0
    for item in list1 :
        if item > max1 :
            max1 = item  
            max_index = index
        index += 1
    return max1, max_index




for index in range((len(number_list)-1), 0, -1):
    
    maximum_number, maximum_index = mymax(number_list[:index+1])
    print(maximum_index)
    
    #putting the max number at the end of the list 
    #need the length of the list need a vaiable thats the highest index number
    
    
    #Slice and save a temporary variable
    last_position_value = number_list[index]
    print(last_position_value)
    
    #write the maximum number in last position
    number_list[index] = maximum_number
    #put the value from the last position into the place that was left
    number_list[maximum_index] = last_position_value
    print(index)
    
print(number_list)
    
    
    
    
    