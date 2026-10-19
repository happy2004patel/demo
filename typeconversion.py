#implicit
a=5
b=5.5
c=a+b
print(c,type(c))
#explicit
n1="25"
n2="25"
print(n1+n2)
print(type(n1))
print(int(n1))
#int,float,str,boolen
#list,set,tuple,dic
#real number + imaginary
name=None
print(list("cat"))#string to list
print(list((1,2,3)))#tuple to list
print(list(range(3,30)))#using range generate list

print(tuple([1,2,3]))#list to tuple
print(tuple("hi"))#string to tuple
tuple(range(4))#using range function we generate tuple

print(set([1,2,3,3]))
print(set("hello"))
print(frozenset([1,2,3,4,5,5]))

student={ 
    "name":"happy",
    "age":21,
    "rollno":123
}
print(list(student.items()))