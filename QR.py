# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:15:01 2021

@author: juanc
"""

import LA
import pytest



def unstable_GrSch(matrix_a: list) -> list:
    """
    Performs an unstable version of the Gram-Schmidt method for QR factorization

    Arguements
    ----------
    matrix_a : list
        A matrix represented as a list of lists.

    Returns
    -------
    list
        Q & R, a list of two matricies.

    """
    Q = []
    R = []
    V = []
    for element in matrix_a:
        Q.append([0 for i in range(len(element))])
        R.append([0 for i in range(len(matrix_a))])
    for index in range(len(matrix_a)):
        V.append(matrix_a[index])
        for inner_index in range(0, index):
            R[inner_index][index] = LA.inn_prod(Q[inner_index], V[index])
            V[index] = LA.add_vectors(V[index], LA.Scal_Vec_mult(Q[inner_index], -R[index][inner_index]))
        R[index][index] = LA.p_norm_2(V[index])
        Q[index] = LA.Scal_Vec_mult(V[index], 1/R[index][index])
    return(Q, R)



def stable_GrSch(matrix_a: list) -> list:
    """
    Finds the QR Factorization of a matrix

    Arguements
    ----------
    matrix_a : list
        A matrix represented as a list of lists.

    Returns
    -------
    list
        The [Q,R] factorization of the input matricies.

    """
    Q: list = []
    R: list = [[0, 0], [0, 0]]
    V: list = []
    for element in matrix_a:
        V.append(element)
    for index in range(len(matrix_a)):
        R[index][index] = LA.p_norm(V[index])
        Q.append(LA.Scal_Vec_mult(V[index], 1 / R[index][index]))
        for inner_index in range(index, len(matrix_a)):
            R[inner_index][index] = LA.inn_prod(Q[index], V[inner_index])
            s = LA.Scal_Vec_mult(Q[index], -R[inner_index][index])
            V[inner_index] = LA.add_vectors((V[inner_index]), s)
    return [Q, R]


