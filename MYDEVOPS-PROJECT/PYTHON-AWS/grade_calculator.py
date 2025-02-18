sciences = float(input("Enter your grade in Sciences \n"))
maths= float(input("Enter your grade in maths \n"))
english = float(input("Enter your grade in english \n"))
sport = float(input("Enter your grade in sport \n"))
french = float(input("Enter your grade in french \n"))

grade = sciences + maths + english + sport + french / 5
if grade >= 16 :
    print(" your grade is A\n ")

elif grade >= 12 and grade < 16:
    print ("your grade is B")

else :
    print("your grade is C")

