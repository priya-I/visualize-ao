'''
Created on Apr 20, 2013

@author: Priya

This code extracts the data from the AO dataset in CSV format for visualizing using d3 
'''

'''
0:uid   
1:treatment
2:userid 
3:   sessid 
4:   listentime 
5:   forumid 
6:   messageforumid 
7:   messagecrop   
8: messagetopic 
9:   messagedate    
10: listendurations  
11:   educ  
12:  village 
13:   age

'''
'''3,10,7,8'''
import csv
import fileinput
import datetime as t
from collections import defaultdict


records=[]

count=0
 
for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        timestamp=row[4]
        parsed=timestamp.split("/")
        month=parsed[0]
        day=parsed[1]
        year=parsed[2][:4]
        listendate=t.date(int(year),int(month),int(day))
        #Storing variables that I need 
        callduration=row[10]
        crop=row[7]
        topic=row[8]
        #1 is the number of sessions in that week and year
        if(crop and topic):
            records.append((listendate,(1,callduration,crop)))
        count+=1
res=defaultdict(list)
for k,v in records: res[k].append(v)


'''
sum of tuple[0]
average of tuple[1]
merge all tuple[2]

'''

o=open("bardata.csv","w+")
o.write("Date, Sessions, Duration, Crops\n")
for record in res:
    avg=0
    sessions=0
    duration=0
    crops=[]
    count=0
    cropset=""
    for tuples in res[record]:#res[record] returns list of tuples
        sessions+=1
        #print tuples
        duration+=int(tuples[1])
        count+=1
        crops.append(tuples[2])
    avg=duration/count
    print sessions,avg, record
    
    lisDate=record;
    for crop in set(crops):
        cropset+=str(crop)+" " 
    o.write(str(lisDate)+","+str(sessions)+","+str(avg)+","+cropset+"\n")
o.close() 
    
#csv conversion to json through a website.
     
        
        
        
        