import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
def sqr(pa):
    return pa*pa
x=[]
y=[]
a=pd.read_csv('HoR.DAT', sep='\t',decimal=',')

a['median']= a['R'].rolling(4).median()
a['std'] = a['R'].rolling(4).std()

#filter setup
#a = a[(a[1] <= a['median']+3*a['std']) & (a[1] >= a['median']-3*a['std'])]
for rw in a.values:
    x.append(rw[0])
    y.append(rw[3])
    if (rw[1]>rw[2]+3*math.sqrt(rw[3]) or rw[1]<rw[2]-3*math.sqrt(rw[3]) ):
        print("Found"+str(rw[0])+" ;; "+str(rw[1]))
    #print(str(rw))
def mydata(filename):
    mydata=pd.read_csv(filename, sep='\t',decimal=',')
    mx=[]
    my=[]
    for mrw in mydata.values:
        mx.append(mrw[0])
        my.append(mrw[1])
    mdx=[]
    mdy=[]
    ms=len(mx)-1
    j=0
    while(j<ms):
        if(mx[j+1] != mx[j]):
          mdy.append((my[j+1]-my[j])/(mx[j+1]-mx[j]))
          mdx.append(mx[j])
        j+=1
    j=1
    ox=[]
    oy=[]
    while(j<ms-3):
        ymean=(my[j+3]+my[j+1]+my[j+2]+my[j-1])/4
        ystd=sqr(my[j+3]-ymean)+sqr(my[j+1]-ymean)+sqr(my[j+2]-ymean)+sqr(my[j-1]-ymean)
        #print(str(my[j])+"<>"+str(ymean)+"<>"+str(math.sqrt(ystd)))
        if my[j] < ymean-3*math.sqrt(ystd) or my[j] > ymean+3*math.sqrt(ystd) :
            print("found outlier" + str(mx[j])+" : "+str(my[j])+"<>"+str(ymean)+"<>"+str(math.sqrt(ystd)))
            ox.append(mx[j])
            oy.append(my[j])
            del mx[j]
            del my[j]
            ms-=1
        j+=1
    return mx,my,mdx,mdy,ox,oy
fig = plt.figure()  # an empty figure with no axes
fig.suptitle('Resistivity')  # Add a title so we know which it is
plt.xlabel('T')
plt.ylabel('R')
plt.plot(x,y,'r+', label="HoR std")

kx,ky,kdx,kdy,kox,koy=mydata("HoR.DAT")
#plt.plot(kx,ky,'bo', label="Dy1R")
#plt.plot(kox,koy,'r+', label="Dy1R outliers")

plt.legend()
plt.show()