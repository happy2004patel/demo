'''
tst=input("enter words ")
lst=[]
for i in tst:
    if(len(lst)>3):
       tst=(lst.append(tst))
print(len(tst))
'''
sentence=input("enter your sentence")
lstofsen=sentence.split(" ")
lstgt3char=[]
for i in lstofsen:
    if (len(i)>3):
        lstgt3char.append(i)
print(lstgt3char)        