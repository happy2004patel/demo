students=[]
print("Welcome to the student Data Organizer !") 
while(True):
    print(''' Select an option:  
              1.Add student
              2.Display All students
              3.Update student Information
              4.Delete student
              5.Display subject Offered
              6.Exit''')
    userinput= int(input("Enter your choice: "))
    if(userinput==1):
        studentid=int(input("student id: "))
        name=input("name: ")
        age=int(input("age: "))
        grade=input("grade: ")
        dob=input("date of birth(yyyy-mm-dd): ")
        subj=input("subjects(comma-seprated): ")
        identitytuple=(studentid,dob)
        studentdic={
            "studentid":studentid,
            "name":name,
            "age":age,
            "grade":grade,
            "dob":dob,
            "subj":set(subj.split(","))
        }
        students.append(studentdic)
    elif(userinput==2):
        for i in students:
            print(f"studentid:{studentid},{i,name},{i,age},{i,grade},{i,dob},{i,subj}")
    elif(userinput==3):
        userstudentid=int(input("enter studentid to update: "))
        for i in students:
            if(i["studentid"]==userstudentid):
                enteryourage=input("enter the age: ")
                i["age"]=enteryourage  
                print("student update successfully!")
    elif(userinput==4):
        userstudentid=input("enter studentid: ")
        if i in students:
         del[studentid]
        print("student deleted!")
    elif(userinput==5):
        for i in students:
            print(i)                
    elif(userinput==6):
        print("Exiting the program. Goodbye!")    
        break
    else:
        print("invalid choice")