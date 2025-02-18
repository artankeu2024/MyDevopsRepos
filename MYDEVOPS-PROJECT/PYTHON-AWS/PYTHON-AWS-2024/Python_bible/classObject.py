# class is a template
# the object is instantatiation of the template

# a class has state(characteristique) and method (function, what it can do)

# syntax
# the class name has to be in upper case
# class Classname: 
#     state

class Pound:
    value = 1.00
    color = "gold"
    num_edges = 1
    diameter = 22.5 
    thickness = 3.25
    heads = True

# making object (coin 1)
coin1 = Pound()
print(type(coin1))
# calling the state of the class
coin1.value
print(coin1.value)

# to change the value of a state 
# changing the value of a state "color"
coin1.color = "green"
print(coin1.color)

# # making object 2 (coin2)
# coin2 = Pound()
# coin2.color
# print(coin2.color)

# class method