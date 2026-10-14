#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
student={
"name":"happy",
"age":21,
"city":"ahmd"
}

print(student["name"],student["age"],student["city"])
student2=student.copy()
print(student2)
print(student.get("name"))
lst=student.items()
print(lst)
print(student.keys())
print(student.pop('name'))
print(student.popitem())
#print(student.fromkeys(student2))
print(student)
#print(dir(dict))
