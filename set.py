set={1,2,3,4,5}
set1=set.copy() #copy
set2={1,2,3,4,5,6,7,8,9,10}
set.add(6)  #add
set1.add(10)
print(set)
print(set.difference(set1))  #difference
set.difference_update(set1)  #difference_update
print(set,set1)
set1.discard(10)  #discard
print(set1)
print(set.intersection(set2))  #intersection  prints common element
set.intersection_update(set2)  #intersection_update  
print(set, set2)
print(set.isdisjoint(set2))  #isdisjoint
print(set.issubset(set1))   #issubset
print(set.issubset(set2)) 
print(set2.issuperset(set)) #issuperset
(set2.remove(10))   #remove
print(set2)
print(set.symmetric_difference(set2))  #symmetric_difference
set.symmetric_difference_update(set2)  #symmetric_difference_update
print(set,set2)
print(set.union(set2))  #union
#set.update(set2)   #update
print(set)
print(set.pop())   #pop
print(set.clear())   #clear
print(set, set1, set2)