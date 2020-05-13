#load pandas library as pd
import pandas as pd

#create name class
class name:
    def _init_(self, first, last, middle):
        first = 'test'
        last = 'test'
        middle = 'test'
        parcel = 0
        isjr = 'test'

#read data from file 'OODataCSV'
data = pd.read_csv("OODataCSV.csv", encoding = 'iso-8859-1')
datalen = len(data)

#create new name arrays with names
    namelist = [name() for i in range(0, datalen)]


#fill the name array with names and parcel data
for x in range(0, datalen):
    splitstr = data.iloc[x][3].split()
    namelist[x].first = splitstr[0]
    
    if len(splitstr) > 1:
        namelist[x].last = splitstr[1]
    else:
        namelist[x].last = 'test'
        
    if len(splitstr) > 2:
        namelist[x].middle = splitstr[2]
    else:
        namelist[x].middle = 'test'
    
    if len(splitstr) > 3:
        namelist[x].isjr = splitstr[3]
    else:
        namelist[x].isjr = 'test'
    
        
    namelist[x].parcel = data.iloc[x][0]
    
#compare time
errorlist = []
for x in range(0, datalen-1):
    if namelist[x].isjr != 'JR.' and namelist[x+1].isjr != 'JR.':
        if namelist[x].first == namelist[x+1].first:
             if namelist[x].last == namelist[x+1].last and namelist[x].last != 'test' and namelist[x+1] != 'test':
                 if namelist[x].parcel != namelist[x+1].parcel:
                     if namelist[x].middle == 'test' or namelist[x+1].middle== 'test'or namelist[x].middle== '&'or namelist[x+1].middle== '&':
                         errorlist.append(x)
                         errorlist.append(x+1)
                     elif namelist[x].middle == namelist[x+1].middle:
                         errorlist.append(x)
                         errorlist.append(x+1)
                     elif  namelist[x].middle[:1] == namelist[x+1].middle[:1]:
                         errorlist.append(x)
                         errorlist.append(x+1)

#export into excel
datalist = data.values.tolist()
errorlist = list(dict.fromkeys(errorlist))
errorexp = []
for x in errorlist:
    errorexp.append(datalist[x])
    
errordfexp = pd.DataFrame(errorexp, columns = ['Parcel', 'Account', 'Use Code', 'Owner', 'OO Net 1st Half', 'OO Net 2nd Half', 'MHSFLG'])
errordfexp.to_csv(r'OOErrorEntriesAG.csv')
        
                     
                     
                     
                     
                     