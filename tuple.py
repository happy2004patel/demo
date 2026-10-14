''' 
lst=[1,2,3,4,5,6,7,8]
oddlst=[]
evenlst=[]
for i in lst:
    if i%2==0:
        oddlst.append(i)
    else:
        evenlst.append(i)
print(oddlst)   
print(evenlst)'''
lst=[1,2,3,4,5]
lstrevers=[]
for i in range(len(lst)):
    lstDigi =lst.pop()
    lstrevers.append(lstDigi)
print(lstrevers)    
print(lst)
'''
lstrevers=[5,4,3,2,1]
i=0, lstdigi =5,lstrevers.append(lstdigi),i=1
i=1, lstdigi =4,lstrevers.append(lstdigi),i=2
i=2, lstdigi =3,lstrevers.append(lstdigi),i=3
i=3, lstdigi =2,lstrevers.append(lstdigi),i=4
i=4, lstdigi =1,lstrevers.append(lstdigi),i=5
'''
