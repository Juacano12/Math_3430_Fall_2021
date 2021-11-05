# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:15:01 2021

@author: juanc
"""

import LA
import pytest




def stable_GrSch(matrix_a: list) -> list:
    """
    Finds the QR Factorization of a matrix

    Arguements
    ----------
    matrix_a : list
        A matrix represented as a list of lists.

    Returns
    -------
    Q and R
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


def orthonormal(matrix_a: list) -> list:
    """
    Finds the orthonormal list of vectors in the input matrix. Recalls the
    previous stable_GrSch function to return the orthonormalized list of vectors
    as Q and R

    Arguements
    ----------
    matrix_a : list
        A matrix stored as a list of lists.

    Returns
    -------
    Q and R
        The [Q,R] factorization of the input matricies with Q being 
        orthonormalized.

    """
    result: list = stable_GrSch(matrix_a)[0]
    return result

