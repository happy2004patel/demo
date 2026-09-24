Day=input("enter the name of days")
match Day :
 case "monday":
    print(1)
 case "tuesday":
    print(2)
 case "wensday":
    print(3)
 case "thursday":
    print(4)  
 case "friday":
    print(5)
 case "saturday":
    print(6)
 case "sunday":
    print(7)
 case _:  
      print ("invalid")