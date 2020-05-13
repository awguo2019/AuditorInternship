# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:33:17 2019

@author: Alan
"""

#load pandas library as pd
import pandas as pd

import jellyfish

#create name class
class name:
    def _init_(self, first, last, middle):
        first = 'test'
        last = 'test'
        

#get data from csv
data = pd.read_csv("StreetListing.csv", encoding = 'iso-8859-1')
datalen = len(data)

#create data arrays for mixuplist and misspelllist
stnames = ['' for x in range(datalen)]
namelist = [name() for i in range(0, datalen)]

#array for counts of all potential mix-ups
mixuplist = []

#array for counts of all potential misspellings
misspelllist = []

#populating each data array
for x in range(0,datalen):
    stnames[x] = data.iloc[x][0].replace("'", '')
    stnames[x] = stnames[x].replace(' ', '')
    
    splitstr = data.iloc[x][0].split()
    namelist[x].first = splitstr[0]
    
    if len(splitstr) > 1:
        namelist[x].last = splitstr[1]
    else:
        namelist[x].last = 'test'

#looping through the arrays
for x in range (0, datalen-1):
    for y in range (x+1, datalen):
    
       
        #searching for potential mix-up names through checking same first names and if there is a last name or not
        if namelist[x].first == namelist[y].first:
            if namelist[x].last == 'test' or namelist[y].last == 'test':
                mixuplist.append(x)
                mixuplist.append(y)

#looping through the arrays again
for x in range (0, datalen-1):
    for y in range (x+1, datalen):
        #calculating the damerau levenshtein distance to find possible misspellings (1 shift)
        checky = jellyfish.damerau_levenshtein_distance(stnames[x], stnames[y])
        if checky == 1:
            #store the misspelled pair together
            print("aa")
            misspelllist.append(x)
            misspelllist.append(y)




#clear duplicate entries from the mixuplist      
mixuplist = list(dict.fromkeys(mixuplist))

#output the misspelled list
datalist = data.values.tolist()
errorexp = []
for x in misspelllist:
    errorexp.append(datalist[x])
    
msdfexp = pd.DataFrame(errorexp, columns = ['MPSTNM', '2019 COUNT', '2018 COUNT'])
msdfexp.to_csv(r"MSentriesAG.csv")

#output the mixup list
errorexp2 = []
for x in mixuplist:
    errorexp2.append(datalist[x])
msdfexp2 = pd.DataFrame(errorexp2, columns = ['MPSTNM', '2019 COUNT', '2018 COUNT'])
msdfexp2.to_csv(r"MIXUPentriesAG.csv")


