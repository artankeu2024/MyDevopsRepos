# EXERCISE 2: 
 
# Compare Three Numbers 
 
# Write a Python program that prints "Equal" if three numbers a, b, 
# and c are equal. 
# If at least one number if different, the program should print "Not 
# Equal". 
 
num_a = float(input("choose the first numbers\n"))
num_b = float(input("choose the second numbers\n"))
num_c = float(input("choose the third numbers\n"))

if num_a == num_b and num_c:
    print("equal")

if not num_a == num_b or num_c:
    print("not equal")
