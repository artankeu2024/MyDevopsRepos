

args= argument
kwargs = keyword argument

*args : its use to pass any argument in your code/function. it gives you a result as tupple
When a function parameter starts with an asterisk, it allows for an arbitrary number of arguments, and the function takes them in as a tuple of values. Rewriting the above function:

def myfunc(*args):
    return sum(args)*.05

myfunc(40,60,20)
6.0
Notice how passing the keyword "args" into the sum() function did the same thing as a tuple of arguments.

It is worth noting that the word "args" is itself arbitrary - any word will do so long as it's preceded by an asterisk. To demonstrate this:

def myfunc(*spam):
    return sum(spam)*.05

myfunc(40,60,20)

6.0

kwargs = keyword argument
this return a dictionnary

**kwargs
Similarly, Python offers a way to handle arbitrary numbers of keyworded arguments. Instead of creating a tuple of values, **kwargs builds a dictionary of key/value pairs. For example:

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
    else:
        print("I don't like fruit")
        
myfunc(fruit='pineapple')
My favorite fruit is pineapple
myfunc()
I don't like fruit
