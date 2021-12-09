# -*- coding: utf-8 -*-
"""
Created on Fri Dec 3 15:13:35 2021

@author: juanc
"""
import LA
import QR
import LS


print("Hello, my name is Juan Cano");
print("This library is a collection of different linear algebra functions");
print("the function explinations and examples are below.");
print(" ");

print(" ")
print("LA.py")
print(" ")



print("add_vectors") 
print(" ")
print("takes in two vectors and returns their sum")
print("Example: ")
print("vector_a = [1, 2, 4], vector_b = [3, 1, 2] then add_vectors(a,b) returns:")
print(" ")
vector_a: list = [1, 2, 4];
vector_b: list = [3, 1, 2];
print(LA.add_vectors(vector_a, vector_b))
print(" ")



print("Scal_Vec_mult")
print(" ")
print("takes in a scalar and a vector and teturns their product")
print("Example: ")
print("num_1 = 2, vec_1 = [1, 2, 4] then Scal_Vec_mult returns:")
print(" ")
num_1: float = 2;
vec_1: list = [1,2,4]
print(LA.Scal_Vec_mult(num_1, vec_1))
print(" ")


print("Scal_Matr_mult") 
print(" ")
print("takes in a scalar and a matrix and returns their scalar-matrix multiplication")
print("Example: ")
print("if num_1 = 2, mtx_1 = [[1, 2, 4],[3, 1, 2],[5, 3, 1]] then scalar_matrix_mult returns:")
print(" ")
num_1: float = 2;
mtx_1: list = [[1, 2, 4],[3, 1, 2],[5, 3, 1]];
print(LA.Scal_Matr_mult(num_1, mtx_1))
print(" ")


print("Matr_add")
print(" ")
print("takes in two matrix and returns thier sum")
print("Example: ")
print("mtx_1 = [[1, 2, 4],[3, 1, 2],[5, 3, 1]], mtx_2 = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]")
print("Matr_add returns: ")
print(" ")
mtx_1: list = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]
mtx_2: list = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]
print(LA.Matr_add(mtx_1, mtx_2))
print(" ")


print("Matr_Vec_mult ")
print(" ")
print("takes in a matrix and a vector and returns matrix vector multiplication")
print("Example: ")
print("mtx_1 = [[1, 2, 4],[3, 1, 2],[5, 3, 1]], vec_1 = [1, 2, 4] then Matr_Vec_mult")
print("returns:")
print(" ")
mtx_1: list = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]
vec_1: list = [1, 2, 4]
print(LA.Matr_Vec_mult(mtx_1, vec_1))
print(" ")


print("Matr_Matr_mult")
print(" ")
print("takes in takes in two matrix and returns their matrix matrix multiplication")
print("Example: ")
print("if mtx_1 = mtx_2 = [[1, 2, 4],[3, 1, 2],[5, 3, 1]] then Matr_Matr_mult returns:")
print(" ")
mtx_1: list = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]
mtx_2: list = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]
print(LA.Matr_Matr_mult(mtx_1, mtx_2))
print(" ")


print("abs_val")
print(" ")
print("takes in a complex number and returns the absolute value")
print("Example: ")
print("num_1 = 3 - 4j then absolute_value returns: ")
print(" ")
num_1: complex = 3 - 4j;
print(LA.abs_val(num_1))
print(" ")


print("p_norm")
print(" ")
print("takes in a vector and a float and returns the p-norm of the vector,")
print("p is the float and defaults to 2.")
print("Example: ")
print("vec_1 = [3 + 4j, 1, 4-3j] then pNorm returns")
print(" ")
vec_1: list = [3 + 4j, 1, 4-3j];
print(LA.p_norm(vec_1))
print(" ")


print("inf_norm")
print(" ")
print("takes in a vector and returns the infinity norm")
print("Example: ")
print("vec_1 = [3 + 4j, 1, 4-3j] then infNorm returns:")
print(" ")
vec_1: list = [3 + 4j, 1, 4-3j]
print(LA.inf_norm(vec_1))
print(" ")


print("p_norm_2")
print(" ")
print("takes in a vector a float and a boolean and returns infinity norm")
print("if bool is true and returns p-norm if bool is false")
print("Example: ")
print("if vec_1 = [3 + 4j, 1, 4-3j], num_1 = 2, bool = False, then normSelect returns:")
print(" ")
vec_1: list = [3 + 4j, 1, 4-3j]
num_1: float = 2
print(LA.p_norm_2(vec_1,num_1,False))
print(" ")


print("inn_prod")
print(" ")
print("takes two vectors and returns the inner product.")
print("Example: ")
print("if vec_1 = [1, 2, 4], vec_2 = [5, 3, 1] then innerProd returns:")
print(" ")
vec_1: list = [1, 2, 4]
vec_2: list = [5, 3, 1]
print(LA.inn_prod(vec_1, vec_2))
print(" ")


print(" ")
print("~~~QR.py~~~")
print(" ")


print("stable_GrSch")
print(" ")
print("takes in a matrix and implements gram-schmidt and returns")
print("the Q, R matrices")
print("Example: ")
print("if mtx_1 = [[2,2,1],[-2,1,2],[18,0,0]] then stable_GrSch returns:")
print(" ")
mtx_1: list = [[2,2,1],[-2,1,2],[18,0,0]]
print(QR.stable_GrSch(mtx_1))
print(" ")


print("orthonormal")
print(" ")
print("takes in a list of vectors returns orthonormal list of vectors")
print("Example: ")
print("if mtx_1 =  [[2,2,1],[-2,1,2],[18,0,0]] then orthonormal returns:")
print(" ")
mtx_1: list = [[2,2,1],[-2,1,2],[18,0,0]]
print(QR.orthonormal(mtx_1))
print(" ")


print("householder")
print(" ")
print("takes in a martix implements householder orthogonalization,")
print("returns the Q and R matrixes")
print("Example: ")
print("if mtx_1 = [[12,6,-4],[-51,167,24],[4,-68,-41]] then householder returns: ")
mtx_1: list = [[12,6,-4],[-51,167,24],[4,-68,-41]]
print(" ")
print(QR.householder(mtx_1))
print(" ")


print(" ")
print("~~~LS.py~~~")
print(" ")


print("least_square")
print(" ")
print("takes in a matrix and a vector and returns the least squares solution")
print("Example: ")
print("if mtx = [[-1,2,-1],[2,-3,3]] and vec = [4,1,2] then least_square returns:")
print(" ")
mtx: list = [[-1,2,-1],[2,-3,3]]
vec: list = [4,1,2]
print(LS.least_square(mtx, vec))
print(" ")

print("back_sub")
print(" ")
print("takes in a matrix and a vector returns the back substitution using the two")
print("Example: ")
print("if mtx = [[1,0,0],[2,3,0],[4,5,6]] and vec =  [7,8,9] then back_sub returns:")
print(" ")
mtx: list = [[1,0,0],[2,3,0],[4,5,6]]
vec: list =  [7,8,9]
print(LS.back_sub(mtx, vec))
print(" ")

