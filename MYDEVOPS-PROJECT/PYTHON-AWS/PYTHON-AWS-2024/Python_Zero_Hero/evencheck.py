def even_check(num_list):
    mylist = []
    for number in num_list:
        if number%2 == 0:
            mylist.append(number)
        else:
            pass
    return mylist


even_check([1,2,3,4,5,6,7,8])