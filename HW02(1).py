"""
For this homework assignment we will take our work from HW01 and use it to
prepare a python script which will implement our algoirthms as python functions. 

For Problems #0-5 from HW01, Do the following.



1) Write your answer from HW01 in a comment.

2) Below the comment write a function which implements the algorithm from your
comment. If you find that you need to change your algorithm for your python
code, you must edit your answer in the comment. 

3) Test each of your functions on at least 2 inputs. 

4) Upload your .py file to a github repo named "Math_3430_Fall_2021"

This assignment is due by 11:59pm 09/27/2021. Do NOT upload an updated version to github
after that date. 
"""


#Example:

#Problem 00

"""
-The Three Questions

Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 

-PsuedoCode

def add_vectors(vector_a,vector_b):

Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

Return the desired result.
"""

def add_vectors(vector_a,vector_b):
  result = [0 for element in vector_a]
  for index in range(len(result)):
      result[index] = vector_a[index] + vector_b[index]
  return result

#End Example



#Problem 01

"""
Write an algorithm to implement scalar-vector multiplication.

Q1: What do we have?

A1: We have a vector and a scalar stored as a list. We can refer to the vector as vector_c and the scalar as scalar_a

Q2: What do we want?

A2: We want the original vector to be multiplied by the scalar and get an output of the new vector.

Q3: How do we get there?

A3: Have every element in the original vector be overwritten by its product from the given scalar.


Pseudo-Code

def Scal_Vec_mult(vector_c, scalar_a):
    result = [0 for element in vector_c]
    for index in range(len(result)):
        result[index] = vector_c[index] * scalar_a
    return result
"""


def Scal_Vec_mult(vector_c, scalar_a):
    result = [0 for element in vector_c]
    for index in range(len(result)):
        result[index] = vector_c[index] * scalar_a
    return result

    
#Problem 02

"""
Write an algorithm to implement scalar-matrix multiplication.

Q1: What do we have?

A1: We have a scalar and a matrix. The matrix is kept as multiple lists of either rows or columns. We can refer to these as matrix_a and scalar_b

Q2: What do we want?

A2: We want the matrix to be scaled by the given scalar

Q3: How do we get there?

A3: We multiply each row/column of the matrix by the scalar. We can use a previous algorithim of scalar-vector multiplicaation, implimenting it over multiple vector list instead of just one.

Pseudo-Code

Step 1: Define scalar matrix multiplication

Step 2: Include previous algorithim of scalar-vector multiplication. Adjust for multiple vectors

Step 3: Return matrix
"""


def Scal_Matr_mult(matrix_a, scalar_b):
    result = []
    for index in range((len(matrix_a))):
        result.append(Scal_Vec_mult(matrix_a[index], scalar_b))
    return result

#Problem 03

"""
Write an algorithm to implement matrix addition.

Q1: What do we have?

A1: We have multiple matricies, each having the same amount of elements as they must be compatible with each other to find a sum. We'll label them as matrix_b and matrix_c'

Q2: What do we want?

A2: We want to get the sum of these matricies

Q3: How do we get there?

A3: We can add each set of lists with its corresponding element using the example algorithim of vector addition.

Pseudo-Code

Step 1: Define matrix addition

Step 2: Impliment previous algorithim of vector addition

Step 3: Adjust for multiple vectors corresponding to similar elements

Step 4: Add corresponding vectors together

Step 5: Return Matrix
"""


def Matr_add(matrix_b, matrix_c):
    result = []
    for index in range(len(matrix_b)):
        result.append(add_vectors(matrix_b[index], matrix_c[index]))
    return result

#Problem 04

"""
Write an algorithm to implement matrix-vector multiplication using the linear
combination of columns method. You must use the algorithms from Problem #0 and
Problem #1.  

Q1: What do we have?

A1: We have a matrix and a vector stored, labeled as matrix_d and vector_d, respectively.

Q2: What do we want?

A2: We want the product of the matrix and the vector

Q3: How do we get there?

A3: We'll multiply each column of the matrix with the vector given

Pseudo-Code

Step 1: Define matrix-vector multiplication

Step 2: Initialize result vector to the size equal to the number of columns on the 

Step 3: Return Matrix
"""


def Matr_Vec_mult(matrix_d, vector_d):
    matrix_res = [0 for element in matrix_d]
    result = [0]
    for index in range(len(vector_d)):
        matrix_res[index] = Scal_Vec_mult(matrix_d[index], vector_d[index])
    result = add_vectors(matrix_res[0], matrix_res[1])
    for index in range(2, len(matrix_res)):
        result = add_vectors(result, matrix_res[index])
    return result


#Problem 05

"""
Write an algorithm to implement matrix-matrix multiplication using your
algorithm from Problem #4.

Q1: What do we have?

A1: We have multiple matricies that are able to be multiplied with each other. Labeled as matrix_e and matrix_f

Q2: What do we want?

A2: We want the product of the given matricies

Q3: How do we get there?

A3: We will multiply each column by the corresponding element of the vector in the second matrix

Pseudo-Code

Step 1: Define matrix multiplication

Step 2: Initialize the result vector of the size equal to the number of columns on the matrix. For this we can re-use the previous algorithim of matrix-vector multiplication

Step 3: Return matrix
"""

def Matr_Matr_mult(matrix_e, matrix_f):
    matrix_res = [0 for element in matrix_e]
    result = [0]
    for index in range(len(matrix_f)):
        matrix_res[index] = Matr_Matr_mult(matrix_e[index], matrix_f[index])



#Test Inputs

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]

test_scalar_01 = 2
test_scalar_02 = 3

test_matrix_01 = [[1, 2, 4], [3, 1, 2]]
test_matrix_02 = [[3, 1, 2], [1, 2, 4]]

test_matrix_03 = [[1, 2], [2, 3]]
test_matrix_04 = [[2, 3], [1, 2]]

test_matrix_05 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
test_matrix_06 = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]

"""
# add_vectors(test_vector_01,test_vector_02) should output [4,3,6]
print('Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_02)))
print('Should have been [4, 3, 6]')
"""

#"""
print( )
print('Test Output #1 for Scalar Vector Multiplication: ' + str(Scal_Vec_mult(test_vector_01,test_scalar_01)))
print('Should have been [2, 4, 8]')
print( )
print('Test Output #2 for Scalar Vector Multiplication: ' + str(Scal_Vec_mult(test_vector_02, test_scalar_02)))
print('Should have been [9, 3, 6]')
print( )
#"""

#"""
print( )
print('Test Output #1 for Scalar Matrix Multiplication: ' + str(Scal_Matr_mult(test_matrix_01, test_scalar_01)))
print('Should have been [[2, 4, 8], [6, 2, 4]]')
print( )
print('Test Output #2 for Scalar Matrix Multiplication: '+ str(Scal_Matr_mult(test_matrix_02, test_scalar_02)))
print('Should have been [[9, 3, 6], [3, 6, 12]]')
print( )
#"""

#"""
print( )
print('Test Output #1 for Matrix Addition: ' + str(Matr_add(test_matrix_01, test_matrix_02)))
print('Should have been [[4, 3, 6], [4, 3, 6]]')
print( )
print('Test Output #2 for Matrix Addition: ' + str(Matr_add(test_matrix_03, test_matrix_04)))
print('Should have been [[3, 5], [3, 5]]')
print( )
#"""

#"""
print( )
print('Test Output #1 for Matrix Vector Multiplication: ' + str(Matr_Vec_mult(test_matrix_05, test_vector_01)))
print('Should have been [7, 7, 7]')
print()
print('Test Output #2 for Matrix Vector Multiplication: ' + str(Matr_Vec_mult(test_matrix_06, test_vector_02)))
print('Should have been [12, 12, 12]')
print()
#"""

#All except Q5 is complete. Cut off the final test so the error won't pop up when running code
"""
print()
print('Test Output #1 for Matrix Matrix Multiplication: ' + str(Matr_Matr_mult(test_matrix_05, test_matrix_06)))
"""
