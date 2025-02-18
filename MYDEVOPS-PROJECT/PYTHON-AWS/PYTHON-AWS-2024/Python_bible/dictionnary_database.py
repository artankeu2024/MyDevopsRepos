
# this dictionary has a list as value
# dictionary = {
#     "key":[list],
#     "key1":[list] }
students = {
    "Alice":["id1", 25, "A"],
    "Bob":["id2", 27, "B"],
    "Claire":["id3", 17, "C"],
    "Dan":["id4", 21, "D"],
    "Emma":["id5", 22, "E"]
}

# to get all the value of a key 
print(students["Claire"])

# to get claires id 
#TO get just one value of a key 
print(students["Claire"][0])

# to get dan age and grade
print(students["Dan"][1:])


# this dictionary has a dictionary as a value
# dictionary = {
#     "key":{"key":value,"key":value},
#     "key":{"key":value,"key":value},
#     "key":{"key":value,"key":value}  
#  }
students = {
    "Alice":{"id":"id1", "age":25, "grade":"A"},
    "Bob":{"id":"id2", "age":27, "grade":"B"},
    "Claire":{"id":"id3", "age":17, "grade":"C"},
    "Dan":{"id":"id4", "age":21, "grade":"D"},
    "Emma":{"id":"id5", "age":22, "grade":"E"},
}

# printing alice age 
print(students["Alice"]["age"])

# printing alice age and grade
print(students["Alice"]["age"], students["Alice"]["grade"])
