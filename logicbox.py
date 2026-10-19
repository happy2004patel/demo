while(True):
    print("select an option:"
                    "1.generate a pattern"
                    "2.Analyze a range of number"
                    "3.exit")
    userinput=int(input("enter your choice:"))
if(userinput==1):
    userinput=int(input("enter a numberrow:"))
    for i in range(5):
        for j in range(i+1):
         print("*", end=" ")
        print() 
elif(userinput ==2):
    userstartrange=int(input("enter the start of the range"))
    userendrange=int(input("enter the end of the range"))
    sum=0
    for i in range(userstartrange,userendrange):
           sum+=i
           if i%2==0:
              print(f"number{i} iseven")
           else:
              print(f"number{i} is odd") 
           print(f"sum of all number from {userstartrange},{userendrange}")      
elif userinput==3:
    print("exting the prigram .goodbye!")
    break
else:
    print("invalid choice")