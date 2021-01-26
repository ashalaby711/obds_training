# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:22:36 2021

@author: User
"""

sequence = """"ATTGCCAGC
TAATCGC"""

sequence_length = len(sequence)
print(sequence_length)

gc_count = 0
a_count = 0
t_count = 0
g_count = 0
c_count = 0
n_count = 0
unknown_count = 0
for base in sequence:
    if base == "A":
        a_count += 1
    elif base == "T":
        t_count += 1
    elif base == "C":
        c_count += 1
    elif base == "G":
        g_count += 1
    else:
        unknown_count +=1
        
print(gc_count)

gc_content = gc_count/sequence_length
a_content = a_count/sequence_length
t_content = t_count/sequence_length
g_content = g_count/sequence_length
c_content = c_count/sequence_length
unknown_content = unknown_count/sequence_length
gc_content = (g_count + c_count)/(sequence_length - unknown_count)
at_content = (a_content + t_count)/(sequence_length - unknown_count)
 
print(f"C content is: {c_content}")
print(f"A content is: {a_content}")
print(f"T content is: {t_content}")
print(f"G content is: {g_content}")
print(f"N content is: {unknown_content}")
print(f"GC content is: {gc_content}")
print(f"AT content is: {at_content}")