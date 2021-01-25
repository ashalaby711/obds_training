# -*- coding: utf-8 -*-
"""
Find the complementary DNA strand
"""

def complementarynucleotide(nucleotide):
    #input is base A, T, C or G
    #output is base T, A, G, C
    output = None
    print(nucleotide)
    if nucleotide == "A":
        output = "T"
    elif nucleotide == "T":
        output = "A"
    elif nucleotide == "C":
        output = "G"
    elif nucleotide == "G":
        output = "C"
    else:
        print("*")
    return output
        
sequence = "ATCGGCTAACGTA"



#The above code expects one base

x = 0

def complementary_strand(strand):
    #input is a strand of bases A, T, C or G
    #output is base T, A, G, C
   
   print(strand)
   complementarystrand = ""
   for n in strand:
       x = complementarynucleotide(n)
       
       complementarystrand += x
       
   print(complementarystrand)    
   return(complementarystrand)
   
complement_seq = complementary_strand(sequence)

print(complement_seq)

reverse = sequence[::-1]

print("The srand is", sequence, "and the reverse strand is", reverse)

reversestring = 0
def reversestring (string):
    return string[::-1]

print(reversestring(complement_seq))