# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 11:22:33 2016

@author: Econ12
"""
import os

os.path.abspath('mydir/myfile.txt')

path = 'C:/Users/econ12/Documents/Ancestry_Scraping/TestFiles/'
file_names = os.listdir(path)
for x in range(2): file_names[x] = path + file_names[x]

OUTFILENAME = 'records.txt'

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
                    recordlist= []
                    templist = listreadfile[i].split(',')
                    
                    
                    recordlist.append(templist[0].split()[0].strip())
                    recordlist.append(templist[0].split()[1].strip())

                    recordlist.append(templist[1].strip())
                    recordlist.append(templist[2].strip())                                                      
                    
                    fullrecords[counter] = recordlist[:4]
                    
                    counter += 1
            
            except:
               continue
            
        readfile.close()

            
with open(OUTFILENAME, 'a') as outfile:
    for i in range(1,len(fullrecords)+1):
        record = '\t'.join(fullrecords[i])
        outfile.write(str(i) + '\t' + record + '\n')
       
        
outfile.close()