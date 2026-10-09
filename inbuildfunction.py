# define of list : it is a collection data type which is used to store multipe element in a single variable with different data type or same 

# hetrogenous (mixture of many data type)
# 1 ordered : we can access tha element by using index ,and also update the elementby using index
#2 mutable
#3 hetrogenous
#4 dhyamic type
#5 noted by []

lst1=["happy","janvi","tanisha"]
lst2=[22,20,21]
print(lst1[0])
print(lst2[2])

lst1.append("shree")#append (add one item at the end)
print(lst1)

lst=["happy",21,True,5.1]
lst.reverse()#reverse(reverse the list)
print(lst)

lst1 =["happy","janvi","tanisha"]
lst.clear()#clear (remove everything)
print(lst)

lst2=lst1.copy() #copy (make a copy of the list)
print(lst2)

lst1.extend("shree")#extend(add multiple items)
print(lst1)

print(lst1.index("tanisha"))#index (find the position of an item)

lst1.insert(3,"happy")#insert (find the position of an item)
print(lst1)

lst1.remove("janvi")#remove (remove a specific item)
print(lst1)

lst2=[22,20,21]
lst2.sort()#sort (arrange item in order)(for descending lst.sort(reverse=True))
print(lst2)

lst2.pop(1)#pop (remove an item using position)
print(lst2)

lst2.extend("25")#extend(add multiple items)
print(lst2)

print(lst2.count(20))#count (how many times an item occurs)