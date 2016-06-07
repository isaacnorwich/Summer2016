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
                    
                    recordlist = listreadfile[i].split(',')
                    
                 

                    fullrecords[counter] = recordlist[:4]
                    
                    counter += 1
            
            except:
               continue
            


            
with open(OUTFILENAME, 'a') as outfile:
    for i in range(1,len(fullrecords)+1):
        record = '\t'.join(fullrecords[i])

 
        outfile.write(record + str(i) + '\n')###
        break
        
        #record = '\t'.join([record_id, zip, city, county, state])
        #        outfile.write(record + '\n') 
