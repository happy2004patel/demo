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
            print(f"Student ID: {i['studentid']} | Name: {i['name']} | Age: {i['age']} | Grade: {i['grade']} | DOB: {i['dob']} | Subjects: {i['subj']}")

    elif(userinput==3):
        userstudentid=int(input("enter studentid to update: "))
        for i in students:
            if(i["studentid"]==userstudentid):
                print('''
                        1.update Name
                        2.update Age
                        3.update Grade
                        4.update subj
                        ''')
                updatechoice=input("what do you want to update? : ")
                if updatechoice == "1":
                    i['name'] = input("Enter new name: ")
                elif updatechoice == "2":
                    i['age'] = int(input("Enter new age: "))
                elif updatechoice == "3":
                    i['grade'] = input("Enter new grade: ")
                elif updatechoice == "4":
                    subjects = input(" Enter new Subjects (comma-separated): ") 
                    i['subjects'] = set(subjects.split(","))
                else:
                    print("Invalid")
                    break
                print("updated successfully!")
                break
            else:
                print("student ID not found!")

    elif(userinput==4):
        userstudentid=input("enter studentid: ")
        if i in students:
         del[studentid]
        print("student deleted!")

    elif(userinput==5):
        for i in students:
            print(f"student id {i['studentid']} | Subjects offered: {i['subj']}")

    elif(userinput==6):
        print("Exiting the program. Goodbye!")    
        break
    else:
        print("invalid choice")