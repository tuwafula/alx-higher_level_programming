#!/usr/bin/python3

def max_integer(my_list=[]):

    maximum = my_list[0]
    for x in my_list:
        if x > maximum:
            maximum = x
    return maximum
