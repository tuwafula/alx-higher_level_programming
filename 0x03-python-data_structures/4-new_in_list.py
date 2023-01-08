#!/usr/bin/python3

def new_in_list(my_list, idx, new_element):
    if idx < 0:
        return my_list.copy()
    elif idx > len(my_list):
        return my_list.copy()
    else:
        temp_list = my_list.copy()
        temp_list[idx] = new_element
        return temp_list
