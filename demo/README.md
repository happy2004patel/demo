print("welcome to the interactive personal data collection")

Name=(input("enter your Name:"))
Age=int(input("enter your Age:"))
Height=float(input("enter your Height:"))
Favnumber=int(input("enter your Fav number:"))

print("Thank You! Here is the personal information we have collected:")
print("Name:",Name,"(Type:",type(Name),", Memory Address:",id(Name),")")
print("Age:",Age,"(Type:",type(Age),", Memory Address:",id(Age),")")
print("Height:",Height,"(Type:",type(Height),", Memory Address:",id(Height),")")
print("Favnumber:",Favnumber,"(Type:",type(Favnumber),", Memory Address:",id(Favnumber),")")

Birth_Year = 2026 - 2004
print("your birth year is approximately:",Birth_Year,"(based on your Age",Age,")")
print(" Thank you for using the personal data collector.")