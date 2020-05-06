#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    found = []
    for i in my_list:
        if i % 2:
            found.append((False))
        else:
            found.append((True))
    return (found)
