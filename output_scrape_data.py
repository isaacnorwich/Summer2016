# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 11:22:33 2016

@author: Econ12
"""
import os

os.path.abspath('mydir/myfile.txt')
path = 'C:/Users/econ12/Documents/Ancestry_Scraping/TestFiles/'

file_names = [f for f in os.listdir(path) if f.endswith('.res')]
for x in range(len(file_names)): file_names[x] = path + file_names[x]
print(file_names)


OUTFILENAME = path + 'records.txt'

counter = 1
fullrecords = {}

for file in file_names:
    with open(file, 'r') as readfile:
        listreadfile = list(readfile)
    
        for i in range(len(listreadfile)):          
            first_split = listreadfile[i].split()
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
            

with open(OUTFILENAME, 'w+') as outfile:
    outfile.truncate()    
    for i in range(1,len(fullrecords)+1):
        record1 = '\t'.join(fullrecords[i])
        outfile.write(str(i) + '\t' + record1 + '\n')
        
    outfile.close()