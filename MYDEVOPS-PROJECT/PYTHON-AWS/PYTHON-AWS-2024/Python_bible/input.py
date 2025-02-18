name = input("enter your name here: \n")
age = input("enter your age here")
city = input("enter your city here")
distraction = input("enter your distraction here")

# # it only take a string if you want it to return another data type, you have to cast it
# .format method
string = "my name is {}, Im {}, I live in {} and I like {}"
output= string.format(name, age, city, distraction)
print(output)

string2 = "my name is {}, Im {}, I live in {} and I like {}".format(name, age, city, distraction)
print(string2)

#f string 

string3 = f"my name is {name}, Im {age}, I live in {city} and I like {distraction}"
print(string3)


# file in python 
you can pass a text file as an input 
in this case i created input.txt file and i used the open method to open the file
i set up a variable wiht it 
myfile = open("input.txt")
>>> myfile.read() # to read as one string 
'hello this is a text file \nthis is the second line\nthis is the third line'
 # to read a second time you have toe the cursor like this
 myfile.seek(0)
0
>>> myfile.read

>>> myfile.readlines() the results appear as list. you can loop ...
['hello this is a text file \n', 'this is the second line\n', 'this is the third line']
 
 # to close the file 
 myfile.close()

if you dont want to worry about the files being close:
with open("input.txt") as mynewfile:
    contents = mynewfile.read()


# writting to a file 
By default, the open() function will only allow us to read the file. We need to pass the argument 'w' to write over the file. For example:

# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file

my_file = open('test.txt','w+')
Use caution!
Opening a file with 'w' or 'w+' truncates the original, meaning that anything that was in the original file is deleted!

# Write to the file
my_file.write('This is a new line')



exercice
Write a script that opens a file named 'test.txt' , writes 'Hello World'  to the file, then closes it.

myfile = open('test.txt','w')

myfile.write('Hello World')
myfile.close()