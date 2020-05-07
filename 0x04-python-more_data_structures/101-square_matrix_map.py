#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_mtx = []
    for j in matrix:
        support_list = list(map(lambda x: x ** 2, j))
        new_mtx.append(support_list)
    return(new_mtx)
