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

#Homework 7


def conj(matrix_a: list) -> list:
    x: int = len(matrix_a[0])
    y: int = len(matrix_a)
    result: list = [[matrix_a[row][column].conjugate() for row in range(y)]for column in range(x)]
    return result


def out_prod(vector_a: list,
             vector_b: list) -> list:
    vector_b_conj: list = conj([vector_a])
    result = LA.Matr_Matr_mult(vector_a, vector_b_conj)
    return result


def house_qk(matrix_b: list, q: int) -> list:
    x = len(matrix_b[0])
    q_k: list = [[1 if i == j
                  else 0 for i in range(x)] for j in range(x)]
    vector_c: list = matrix_b[q][q:]
    vector_d: list = q_k[q][q:]
    v_scl: float = LA.p_norm_2(vector_c) * (1 if vector_c[0].real >= 0
                                            else -1)
    vector_d = LA.Scal_Vec_mult(vector_d, vector_c)
    vector_d = LA.add_vectors(vector_d, vector_c)
    matrix_c: list = out_prod(vector_d, vector_d)
    c_scl: float = -2 / LA.inn_prod(vector_d, vector_d)
    matrix_c = LA.Scal_Matr_mult(matrix_c, c_scl)
    for i, c_col in enumerate(matrix_c, start=q):
        q_k[i] = LA.add_vectors(q_k[i][:q] + c_col, q_k[i])
    return q_k


def householder(matrix_d: list) -> list:
    x: int = len(matrix_d[0])
    y: int = len(matrix_d)
    matrix_e: list = [[1 if i==j
                       else 0 for i in range(x)] for j in range(x)]
    matrix_b: list = [column[:]for column in matrix_d]
    for q, _ in enumerate(matrix_b):
        q_k = house_qk(matrix_b, q)
        matrix_b = LA.Matr_Matr_mult(q_k, matrix_b)
        matrix_e = LA.Matr_Matr_mult(q_k, matrix_e)
    matrix_e = conj(matrix_e)
    return [matrix_e, matrix_b]

