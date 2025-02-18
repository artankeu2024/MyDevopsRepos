# for number in range (1,100):
#     if number % 2 == 0:
#         print(number)

#using list comprehension the bellow line of code is the same as the upper code
evennumbers = [x for x in range(1,100) if x % 2 ==0]
print(evennumbers)


list comprehension works for any data type.