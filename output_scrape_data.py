# -*- coding: utf-8 -*-
"""
This code takes the scraped death information from ancestry.com and parses
the relevant information from the output files. It outputs a file that is a
tab delimited format of the death information.
"""

# Import Libraries
import os

# Locate Path of Death Information Files and Set Output File Location
os.path.abspath('mydir/myfile.txt')
path = 'C:/Users/econ12/Documents/Ancestry_Scraping/TestFiles/'
file_names = [f for f in os.listdir(path) if f.endswith('.res')]
for x in range(len(file_names)): file_names[x] = path + file_names[x]
OUTFILENAME = path + 'records.txt'

# Initial Setup
counter = 1
fullrecords = {}

# For each file, this loop collects the data in a dictionary
for file in file_names:
    with open(file, 'r') as readfile:
        listreadfile = list(readfile)
    
        for i in range(len(listreadfile)):          
            first_split = listreadfile[i].split()
            # Sometimes the string is empty and throws an error            
            try:
                if first_split[0].isdigit():
                #checks the first string of the row for a number
                    recordlist = []
                    recordlist = listreadfile[i].split(',')
                    recordlist = [x.strip() for x in recordlist]
                    
                    templist = recordlist[0].split(" ",1)
                
                    recordlist[0] = templist[0]
                    recordlist.insert(1, templist[1])

                    fullrecords[counter] = recordlist[:4]

                    counter += 1           
            except:
               continue

# Writes one tab delimited text file with the relevant data
with open(OUTFILENAME, 'w+') as outfile:
    outfile.truncate()    
    for i in range(1,len(fullrecords)+1):
        record1 = '\t'.join(fullrecords[i])
        outfile.write(str(i) + '\t' + record1 + '\n')
        
    outfile.close()