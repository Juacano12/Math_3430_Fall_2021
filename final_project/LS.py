# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 12:32:58 2021

@author: juanc
"""
import LA
import QR

def back_sub(matrix: list,
             vector: list) -> list:
    """
    Performs back substitution. 
    
    Creates a result vecotr equal to the solutions of the equation

    Arguments
    ----------
    matrix : list
        A matrix stored as a list of lists.
    vector : list
        A column vector stored as a list.

    Returns
    -------
    list
        The back substitution of a matrix and a vector.

    """
    result: list = [vector[-1] * (1 / (matrix[-1][-1]))]
    for current in range(len(matrix) -1, -1, -1):
        temp: float = vector[current]
        for index in range(len(result)):
            temp -= matrix[len(matrix)-1 -index][current]*result[current]
        temp *= 1/(matrix[current][current])
        result.append(temp)
    result = result[::-1]
    return result




def least_square(matrix: list,
                 vector: list) -> list:
    """
    Returns the least squares solution, calculated by using QR factorization.

    Arguments
    ----------
    matrix : list
        A matrix stored as a list of lists.
    vector : list
        A list of floats.

    Returns
    -------
    list
        The least squares of a matrix.

    """
    a: list = QR.stable_GrSch(matrix)[0]
    b: list = QR.stable_GrSch(matrix)[1]
    c: list = LA.Matr_Vec_mult(QR.conj(a), vector)
    result = back_sub(b, c)
    return result