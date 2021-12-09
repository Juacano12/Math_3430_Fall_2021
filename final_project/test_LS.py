# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:43:52 2021

@author: juanc
"""

import pytest
import LS


matrix_01 = [[0,2,3],[1,1,2],[2,0,2]]
matrix_02 = [[3,4,5],[0,2,1],[1,0,3]]
vector_01 = [0,0,1]

def test_least_square():
    assert LS.least_square(matrix_01, vector_01) == [1,-2,1]
    assert LS.least_square(matrix_02, vector_01) == [-0.17,0.33,0.5]

pytest.main()
