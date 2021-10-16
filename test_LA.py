# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 21:44:20 2021

@author: juanc
"""

import pytest
import LA


def test_add_vec():
    vec_1 = [1, 2, 4]
    vec_2 = [3, 1, 2]
    assert LA.add_vectors(vec_1, vec_2) == [4, 3, 6]   
    vec_3 = [1, 1, 1]
    vec_4 = [2, 2, 2]
    assert LA.add_vectors(vec_3, vec_4) == [3, 3, 3]

    
def test_Scale_Vec_mult():
    vec_1 = [1, 2, 4]
    sca_1 = 2
    assert LA.Scal_Vec_mult(vec_1, sca_1) == [2, 4, 8]
    vec_2 = [3, 1, 2]
    sca_2 = 3
    assert LA.Scal_Vec_mult(vec_2, sca_2) == [9, 3, 6]

    
def test_Scal_Matr_mult():
    matr_1 = [[1, 2, 4], [3, 1, 2]]
    sca_1 = 2
    assert LA.Scal_Matr_mult(matr_1, sca_1) == [[2, 4, 8], [6, 2, 4]]
    matr_2 = [[3, 1, 2], [1, 2, 4]]
    sca_2 = 3
    assert LA.Scal_Matr_mult(matr_2, sca_2) == [[9, 3, 6], [3, 6, 12]]


def test_Matr_add():
    matr_1 = [[1, 2, 4], [3, 1, 2]]
    matr_2 = [[3, 1, 2], [1, 2, 4]]
    assert LA.Matr_add(matr_1, matr_2) == [[4, 3, 6], [4, 3, 6]]
    matr_3 = [[1, 2], [2, 3]]
    matr_4 = [[2, 3], [1, 2]]
    assert LA.Matr_add(matr_3, matr_4) == [[3, 5], [3, 5]]

    
def test_Matr_Vec_mult():
    matr_5 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    vec_1 = [1, 2, 4]
    assert LA.Matr_Vec_mult(matr_5, vec_1) == [7, 7, 7]
    matr_6 = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    vec_2 = [3, 1, 2]
    assert LA.Matr_Vec_mult(matr_6, vec_2) == [12, 12, 12]

    
def test_Matr_Matr_mult():
    matr_3 = [[1, 2], [2, 3]]
    matr_4 = [[2, 3], [1, 2]]
    assert LA.Matr_Matr_mult(matr_3, matr_4) == [[8, 13], [5, 8]]
    matr_5 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    matr_6 = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    assert LA.Matr_Matr_mult(matr_5, matr_6) == [[6, 6, 6], [6, 6, 6], [6, 6, 6]]
    
