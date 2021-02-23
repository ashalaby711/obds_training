# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 09:36:47 2021

@author: User
"""

# """1.Write a Python script to convert the SAM file to a BED file
#•One BED line per SAM line
#•ReadSAMfileinput
#•Write BED file output -format your output using fstrings
#2.Supply input file names using command line parameters
#•Supply the SAM file name on the command line using –ior --input
#•Supply the BED file name on the command line using –o or --output
#3.Write out a gzipcompressedfile (.bed.gz)
#4.Make the script run on the command line
#5.Provide a command line argument to padthe intervals in the bed file
#6.Output a file with the coordinates of the sequenced fragments rather than reads
          
    

#"chrom" "chromStart" "chromEnd" "name" "score" "strand"

#SAM fields
#"QNAME" "FLAG" "RNAME" "POS" "MAPQ" "CIGAR" "RNEXT" "PNEXT" "TLEN" "SEQ" "QUAL" "TAGS"

path = "C:\\Users\\User\\test_sequence\\ERR1755082.test.sam"

print(path)

with open(path , "r") as f:
    for line in f:
        print(line)

with open("C:\\Users\\User\\test_sequence\\ERR1755082.bed" , "w") as bedfile:
    bedfile.write("sequence")
    print(line)
        
