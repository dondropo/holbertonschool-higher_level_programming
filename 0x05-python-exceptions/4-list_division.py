#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in (list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            new_list = div
        except ZeroDivisionError:
            div = None
            print("Division by 0")
            new_list = div
        except TypeError:
            div = None
            print("Wrong type")
            new_list = div
        finally:
            div = None
    return new_list