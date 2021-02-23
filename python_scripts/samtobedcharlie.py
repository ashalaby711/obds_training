# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 09:48:13 2021

@author: zafar_et7oqrc
"""

#Exercise - Genomic File Format Conversion
#1. Write a Python script to convert the SAM file to a BED file
#• One BED line per SAM line
#• Read SAM file input
#• Write BED file output - format your output using fstrings
#2. Supply input file names using command line parameters
#• Supply the SAM file name on the command line using –i or --input
#• Supply the BED file name on the command line using –o or --output
#3. Write out a gzip compressed file (.bed.gz)
#4. Make the script run on the command line
#5. Provide a command line argument to pad the intervals in the bed file
#6. Output a file with the coordinates of the sequenced fragments rather
#than reads

#'chrom' 'chromStart' 'chromEnd' 'score' 'strand'
#sam fields
#POS QNAME FLAG RNAME MAPQ CIGAR RNEXT PNEXT TLEN SEQ QUAL

#C:\Users\zafar_et7oqrc\Desktop\ERR1755082.test.sam

import argparse
parser = argparse.ArgumentParser("") 
parser.add_argument('--output', dest= 'bedfile_path', help='this is the output file expecting .gz file name')
parser.add_argument('--input', dest='samfile_path', help='Input file name')
args = parser.parse_args()


#path = '/Users/ab2018/devel/obds_training/ERR1755082.test.sam'
#print(path)

import gzip
with gzip.open (args.bedfile_path, 'wt') as bedfile:
        # iterate line by line
        #wt to let the file to expect a text

    with open (args.samfile_path, 'r') as f:
    # iterate line by line
        for line in f:
            if "@" in line:
                continue
            
            
            #save a variable to store line values
            #split the line into columns
            list_of_fields = line.split('\t')      
            print(list_of_fields)
            if "*" in list_of_fields[2]:
                continue
            #defining new variables
            name = list_of_fields[0]
            chrom = list_of_fields[2]
            chromStart = int(list_of_fields[3]) -1
            chromEnd = int(len(list_of_fields[9]))+int(chromStart)
            score = "."
            strand = "+"
            print(chromStart)
            print(chromEnd)
            #swapping the 2 values around
    
            #if int(list_of_fields[8]) < 0:
                #chromEnd = list_of_fields[3]
                #chromStart = int(list_of_fields[8])+int(chromStart)
                
    
            bedfile.write(F"{chrom}\t{chromStart}\t{chromEnd}\t{name}\t{score}\t{strand}\n")
            #bubblesort(mylist)
            #print(mylist)
            
            
    
print(bedfile)
print(args)


