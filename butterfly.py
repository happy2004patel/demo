
n=5
for i in range(n):
    for j in range(0,i,1):
        print("*",end="")
    for z in range(0,(n-i-2)*2+2,1):
        print(" ",end="")
    for j in range(0,i,1):
        print("*",end="")
    print()


n=5
for i in range(0,5+1,1):
    for j in range(0,5+1,1):
        if(i==0 or i==n or j==0 or j==n):
            print("*",end="")
        else:
         print(" ",end="")
    print()

    
for i in range(5):
    print("*", end ="")
    for j in range(i):
        print("*",end ="")
    print()

    '''butterfly'''
for i in range(6):
    for j in range(i):
        print("*",end="")
    print(" "*(11-i*2),end="")
    for j in range(i):
        print("*",end="")
    print()
    


'''star,que'''
for i in range(1,5,1): 
    for j in range(i):
        print("*",end="")
    for j in range(5-i):
        print("?",end="")
    print()


'''square'''
for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()    


'''triangle'''
for i in range(1,5):
    print(" "*(5-i),end="")
    for j in range(i):
     print("* ",end="")
    print()
    