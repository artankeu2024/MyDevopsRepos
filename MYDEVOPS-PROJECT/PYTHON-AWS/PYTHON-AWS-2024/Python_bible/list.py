#data structure
# list
# list can content multiple data type
# a list is iterable . it meant it can be broken in a little piece call
# element . each element has it own index starting from Zero and goes up
# to get an element of a list you use his index
# user = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]
# user[1]
# = Bob
# index also works from the end of the list but it start by -1 not 0
# user[-2]
# = Georgie
# you can create variable with an element from the list

variableA = user[1]
>> variableA
>> Bob

To take out multiple element from the list we use slicing 
user[start:end:step]
the end is not included
the step is default to 1
to have Alice", "Bob", "Claire" from the list we do this:
user[0:3]
 
A list can content another list.
classmate = [1,2,[3,4,5],6,7,8]
to get the the list [3,4,5] we use index 2
classmate[2]
>>[3,4,5]
to have an element from the list inside our first list 
to have 3 for example
classmate[2][0]
>>3


user = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

print(len(user)) # to know how many element you have in a list

while True:
    print ("hi my name is travis")
    name = input(" what is your name ? ").strip().capitalize()
    if name in user:
        print(("hello {} this name is recognised").format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()
        if remove == "y":
            print(user)
            user.remove(name)  #the remove function remove something from the list
            print("you have been removed from the system")
            print(user)
        elif remove == "n":
            print("No Problem, I didnt want you to leave anyway")
    else :
        print("hummmmmmm I dont think I have meet you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)? ").strip().lower()
        if add_me == "y":
            print(user)
            user.append(name) # the  append function is used to add something to the list
            print(user)
        elif add_me == "n":
            print("No worries, you can always come back")

# .strip remove any space from the users input
   # deleting from the list using index and del function its 
   # its usefull when you just know the index but not the exact value
   # you can also use the del function to slice a list
#  >>> 
# >>> L = [1,2,3,4,5]
# >>> del L[0]
# >>> L
# [2, 3, 4, 5]
# >>>   


# more way to add something to the list 
>>> # append add something at the end of the list
>>> A = [5,12,72,55,89]
>>> A.append(10)
>>> A
[5, 12, 72, 55, 89, 10]
>>> A = A + [2]  # list = list + [what you want to add]
>>> A
[5, 12, 72, 55, 89, 10, 2]
>>> 
>>> 

adding a string to the list 
>>> A = A + "bcd"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "str") to list
>>> A = A + ["BCD"]
>>> A
[5, 12, 72, 55, 89, 10, 2, 'BCD']
>>> 
>>> A = A + list("BCD") # THIS ADD STRING AS INDIVIDUALL ELEMENT 
>>> A
[5, 12, 72, 55, 89, 10, 2, 'BCD', 'B', 'C', 'D']
>>> 
>>> 

>>> A = A + [1,2,3] # BEST way to add interger
>>> A
[5, 12, 72, 55, 89, 10, 2, 'BCD', 'B', 'C', 'D', 1, 2, 3]
>>> 

>>> A = A + list(str(123)) Converting number to a string to add to a list
>>> A
[5, 12, 72, 55, 89, 10, 2, 'BCD', 'B', 'C', 'D', 1, 2, 3, '1', '2', '3']
>>> 
 # adding a list to a list 
>>> 
>>> A = A + [[5,6,7,8]] # adding a list to a list
>>> A
[5, 12, 72, 55, 89, 10, 2, 'BCD', 'B', 'C', 'D', 1, 2, 3, '1', '2', '3', [5, 6, 7, 8]]
>>> 

>>> A.append([10,11,12,13]) # adding list to a list method 2 
>>> A
[5, 12, 72, 55, 89, 10, 2, 'BCD', 'B', 'C', 'D', 1, 2, 3, '1', '2', '3', [5, 6, 7, 8], [10, 11, 12, 13]]
>>> 

# to insert something inside the list
>>> A = [5, 12, 72, 55, 89, 10, 2]
>>> A.insert(3,34) # list.insert(index,new-element)
>>> A
[5, 12, 72, 34, 55, 89, 10, 2]
>>> 
 # inserting a list to a list using index and insert function
>>> A.insert(4,[10,11,12,13])
>>> A
[5, 12, 72, 34, [10, 11, 12, 13], 55, 89, 10, 2]
>>> 

to remove . you remove using the remove function
or the pop method it remove from the end of the list if you dont add the index number

to organise in alphabetical order use .sort()method
or the sorted method (this print out the result)
to reverse .reverse method

