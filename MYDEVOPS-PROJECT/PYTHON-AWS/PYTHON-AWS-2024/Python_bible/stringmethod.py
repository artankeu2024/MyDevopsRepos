a = " Mayamba is a beautifull girl, she is a belle fille"
a.count("is")
a.count("Mayamba")

>>> x = "happy birthday"
>>> x.lower()
'happy birthday'
>>> x
'happy birthday'
>>> x.upper()
'HAPPY BIRTHDAY'
>>> x
'happy birthday'
>>> x.lower()
'happy birthday'
>>> x.capitalize() only the frist letter is capitalize
'Happy birthday'
>>> x.title()  all the words ae capitalize
'Happy Birthday'

# to check if a string is : 
x.islower
x.isupper
x.istitle
x.isalpha
x.isdigit
x.isalnum alphanumerique
# to look for the position of a word in a string 
x.index("birthday") on commence a compter ero et non 1
x.find("birthday")

# to remove a specific letter from the string
>>> y = " 000000000000happybirthday0000000000"
>>> y.strip(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: strip arg must be None or str
>>> y.strip("0")
' 000000000000happybirthday'
>>> y = "000000000000happybirthday0000000000"
>>> y.strip("0")
'happybirthday'
>>> y.strip("y")
'000000000000happybirthday0000000000'
>>> y.strip("y")
'000000000000happybirthday0000000000'
>>> y.lstrip left
y.rstrip right
y.rstrip() to remove the space on the 

5:9
# slicing formaat 
variable[start:end:step]

to show the index automatically you can use the index function
word = "supercalifragilistice"
word.index("cali")
5

1. Are strings mutable?

Strings are not mutable! (meaning you can't use indexing to change individual elements of a string)