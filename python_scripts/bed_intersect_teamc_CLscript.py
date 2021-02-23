# -*- coding: utf-8 -*-
"""
Team C: Carla and Ahmed
Python script to count the number of intervals overlapping between two bed files
"""
import argparse
#set parameter for output, input, pad and fragment
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", dest="bedfilename", default="output.bed", help="output file name")
parser.add_argument("-i", "--input1", dest="bedfilename1", help="input file name of first bed file")
parser.add_argument("-j", "--iput2", dest="bedfilename2", help="input file name of second bed file")
args = parser.parse_args()
#defining the path for bedfile1 and bedfile2
#path1 ="C:\\Users\\User\\test_sequence\\brain_dnase1_chr21.bed"
#path2 ="C:\\Users\\User\\test_sequence\\gut_dnase1_chr21.bed"

#creating output file
outputbed = open(args.bedfilename, "w")


#open bedfile1 to read only
with open(args.bedfilename1, 'r') as bedfile_1:
    #splitting lines in bedfile 1 to columns
    for line1 in bedfile_1:

        columns1 = line1.split("\t")
        chrom1 = columns1[0]
        chromStart1 = int(columns1[1])
        chromEnd1 = int(columns1[2])
        #print("printing line of bedfile1")
        #opening bedfile2 to read only
        with open(args.bedfilename2, 'r') as bedfile_2:        
            for line2 in bedfile_2:
                columns2 = line2.split("\t")
                chrom2 = columns2[0]
                chromStart2 = int(columns2[1])
                chromEnd2 = int(columns2[2]) 
                #print("printing line of bedfile2")
                
                #comparison arguments to define overlapping
                if chrom1 == chrom2:
                    if chromEnd2>=chromStart1>=chromStart2 or chromEnd2>=chromEnd1>=chromStart2 or chromStart1>=chromStart2>chromEnd1 or chromStart1>=chromEnd2>=chromEnd1:
                        if args.bedfilename=="-":
                            print(F"{chrom2}\t{chromStart2}\t{chromEnd2}\n")
                        else:
                            outputbed.write(F"{chrom1}\t{chromStart1}\t{chromEnd1}\t{chrom2}\t{chromStart2}\t{chromEnd2}\n")
                    
                    elif chromStart2>=chromStart1 and chromEnd2<=chromEnd1:
                        if args.bedfilename=="-":
                            print(F"{chrom2}\t{chromStart2}\t{chromEnd2}\n")
                        else:
                            outputbed.write(F"{chrom1}\t{chromStart1}\t{chromEnd1}\t{chrom2}\t{chromStart2}\t{chromEnd2}\n")
                    
                    
                    
                        #copy output to an output file
                        #outputbed.write(F"{chrom1}\t{chromStart1}\t{chromEnd1}\t{chrom2}\t{chromStart2}\t{chromEnd2}\n")
outputbed.close()
