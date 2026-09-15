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
        listendate=t.datetime.strptime(timestamp[:10], "%m/%d/%Y").date()
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

with open("bardata.csv","w+") as o:
    writer=csv.writer(o)
    writer.writerow(["Date","Sessions","Duration","Crops"])
    for record in res:
        duration=0
        crops=[]
        for tuples in res[record]:
            duration+=int(tuples[1])
            crops.append(tuples[2])
        sessions=len(res[record])
        avg=duration/sessions
        cropset=" ".join(set(crops))
        print sessions,avg,record
        writer.writerow([record,sessions,avg,cropset])
    
#csv conversion to json through a website.
     
        
        
        
        