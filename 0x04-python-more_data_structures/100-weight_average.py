#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        add = div = 0
        for i in my_list:
            add += i[1] * i[0]
            div += i[1]
        return add/div
