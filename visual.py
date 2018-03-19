import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
#from sklearn.cluster import KMeans
s_bt=pd.read_csv('Steps_BT.csv')
t_bt=pd.read_csv('Time_BT.csv')
s_mv=pd.read_csv('Steps_MVR.csv')
t_mv=pd.read_csv('Time_BT.csv')

s_f=pd.read_csv('Steps_F.csv')
t_t=pd.read_csv('Time_F.csv')

f={}
bn='50'
t=list(s_f[bn])
an=list(range(0,12000,1))
#an=list(range(0,20,1))
d={}
for i in an:
    d[str(i)+'-'+str(i+1)]=0
for i in t:
    print(i-i%50)
    d[str(i)+'-'+str(i+1)]+=1
a=[]
b=[]
for i in d:
    a.append(str(i))  
    b.append(d[i])
print(a,b)

f={}
for i in range(len(b)):
    f[a[i]]=b[i]
import csv
with open('f_'+bn+'.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in f.items():
       writer.writerow([key, value])

'''
print(b,a)
plt.subplot(212)
plt.pie(b,labels=a)
at=s_bt['50']
an=list(range(0,2800,50))
d={}
for i in an:
    d[i]=0
for i in t:
    d[i-i%50]+=1
a=[]
b=[]
for i in d:
    a.append(str(i)+'-'+str(i+50))
    b.append(d[i])
plt.subplot(211)
plt.pie(b,labels=a)

t=s_bt['48']
an=list(range(0,5000,50))
d={}
for i in an:
    d[i]=0
for i in t:
    d[i-i%50]+=1
a=[]
b=[]
for i in d:
    a.append(str(i)+'-'+str(i+50))
    b.append(d[i])
#plt.subplot(210)
#plt.pie(b,labels=a)


plt.show()
#plt.hist(list(s_bt['49']),bins=200,range=(200,2000),histtype='step')
#plt.hist(list(spf_s['49']),bins=200,range=(200,2000),histtype='step')
#plt.hist(list(s_mv['49']),bins=200,range=(200,2000),histtype='step')
'''