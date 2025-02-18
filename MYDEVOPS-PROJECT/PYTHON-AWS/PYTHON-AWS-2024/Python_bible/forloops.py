# foloops
# its iterable iterable means perform actions on a single item. you can loop through a single single 
# range (1, 11) # range is a function it give you the following range itterable: 
# # it doesn't include 11. 
# [1,2,3,4,5,6,7,8,9,10]
# syntaxe
# for variable in iterrable  #iterable can be a list string dict, set, tuple
#     code 
# for number in range(1,11):
#     print(number)

# this code will get all the name on this dictionnaire with a letter "a"
students = {
    "male": ["Tom", "Charlie","Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Elisabeth"]
} # this is the iterable which is this case is dictionnaire
for key in students.keys():  #students.keys() makes dictionnary an iterrable 
    for name in students[key]:
        if "a" in name:
            print(name)

syntaxe
my_iterable = [1,2,3]
for item_name in my_iterable: #item_name represent all the single items from your iterable
    print(item_name)


Example 7
d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)
k1
k2
k3
Notice how this produces only the keys. So how can we get the values? Or both the keys and the values?

We're going to introduce three new Dictionary methods: .keys(), .values() and .items()

In Python each of these methods return a dictionary view object. It supports operations like membership test and iteration, but its contents are not independent of the original dictionary – it is only a view. Let's see it in action:

# Create a dictionary view object
d.items()
dict_items([('k1', 1), ('k2', 2), ('k3', 3)])
Since the .items() method supports iteration, we can perform dictionary unpacking to separate keys and values just as we did in the previous examples.

# Dictionary unpacking
for k,v in d.items():
    print(k)
    print(v) 
k1
1
k2
2
k3
3
If you want to obtain a true list of keys, values, or key/value tuples, you can cast the view as a list:

list(d.keys())
['k1', 'k2', 'k3']
Remember that dictionaries are unordered, and that keys and values come back in arbitrary order. You can obtain a sorted list using sorted():

sorted(d.values())
[1, 2, 3]
