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
