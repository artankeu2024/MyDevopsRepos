Dictionary = {"key":value, "key":value}
the key has to be a string.
key + value = item
to call an element of the dictionary:
dictionary["key"]

# To call for a value of a key in the dictionnary
>>> students = {"Alice":25, "Bob":27, "Claire":17, "Dan":21, "Emma":22}
>>> students["Claire"]   # to look for the value of a key                           
 17

# to get an element to a dictionnary:
dictionary["key"] = value 
>>> students["Fred"] = 25
>>> students
{'Alice': 25, 'Bob': 27, 'Claire': 17, 'Dan': 21, 'Emma': 22, 'Fred': 25}

# To edit the value of an element in the dictionary
>>> students["Alice"] = 30
>>> student["Alice"]
30

# To delete an element from the list
del dictionnary["Key"]
>>> del students["Fred"]
>>> students
{'Alice': 30, 'Bob': 27, 'Claire': 17, 'Dan': 21, 'Emma': 22}
>>> 
>>> students["Fred"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Fred'
>>> 

# to look for all the keys in the dictionnnary
dictionnary.keys()
>>> students.keys()
dict_keys(['Alice', 'Bob', 'Claire', 'Dan', 'Emma'])
>>> 

# Dictionary doesnt support indexing 
To get a specific element of a dictionnary you have to first 
convert the dictionnary to a list 
newdictionaryName = list(dictionary.keys())
>>> dictionaryconvert = list(students.keys())
>>> dictionaryconvert
['Alice', 'Bob', 'Claire', 'Dan', 'Emma']
>>> dictionaryconvert[1]
'Bob'
>>>

# to look for all the key in a dictionary:
>>> dictionaryconvert = list(students.keys())
>>> dictionaryconvert
['Alice', 'Bob', 'Claire', 'Dan', 'Emma']
>>> dictionaryconvert[1]
'Bob'
>>>

# to look for all the value 
dictionary.values()
>>> students.values()
dict_values([30, 27, 17, 21, 22])
# converting the values to a list
>>> newdicvalue = list(students.values())
>>> newdicvalue
[30, 27, 17, 21, 22]
>>> newdicvalue[0]
30
or you can simply do this:
list(dictionary.values())[index]
list(students.values())[2]
>>> 
>>> list(students.values())[2]
17
>>> 
>>> list(students.values())[2:] # to slice
[17, 21, 22]
>>>
# to get the list of all the items
dictionary.items()
>>> students.items()
dict_items([('Alice', 30), ('Bob', 27), ('Claire', 17), ('Dan', 21), ('Emma', 22)])
>>> 

# adding multiple value to a key, or adding a list to a dictionary 

students = {"Alice":25, "Bob":27, "Claire":17, "Dan":21, "Emma":22}

students = {
    "Alice":["id1", 25, "A"],
    "Bob":["id2", 27, "B"]
    "Claire":["id3", 17, "C"]
    "Dan":["id4", 21, "D"]
    "Emma":["id5", 22, "E"]

}