# -*- coding: utf-8 -*-
"""
This code takes the scraped death information from ancestry.com and parses
the relevant information from the output files. It outputs a file that is a
tab delimited format of the death information.

Note: This code is written in Python 3.5
"""

# Import Libraries
import os

# Locate Path of Death Information Files and Set Output File Location
os.path.abspath('mydir/myfile.txt')
path = 'C:/Users/econ12/Documents/Ancestry_Scraping/TestFiles/'
file_names = [f for f in os.listdir(path) if f.endswith('.res')]
for x in range(len(file_names)): file_names[x] = path + file_names[x]
OUTFILENAME = path + 'records.csv'

# Initial Setup
counter = 1
fullrecords = {}


# For each file, this loop collects the data in a dictionary
for file in file_names:
    with open(file, 'r') as readfile:
        #Turns every line into a new entry in a list        
        listreadfile = list(readfile)
    
        for i in range(len(listreadfile)):          
            first_split = listreadfile[i].split()
            # Sometimes the string is empty and throws an error            
            try:
                #checks the first string of the row for a number    
                if first_split[0].isdigit():
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

# Writes one tab delimited text file with the relevant data from fullrecords
with open(OUTFILENAME, 'w+') as outfile:    
    for i in range(1,len(fullrecords)+1):
        record1 = ','.join(fullrecords[i])
        outfile.write(str(i) + ',' + record1 + '\n')  