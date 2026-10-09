lst=[1,2,3,4,5,6,7,8]
oddlst=[]
evenlst=[]
for i in lst:
    if i%2==0:
        oddlst.append(i)
    else:
        evenlst.append(i)
print(oddlst)   
print(evenlst)   