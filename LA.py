"""
This homework is due on 10/15/2021 by 11:59pm. 


For this assignment you will be writing a python script to be named LA.py. In
this script you will need to write 6 functions. Every function must 

1) Have a doc string.

2) Have type annotations

3) Be tested using unit testing. 

Once you have finished writing LA.py you will upload it to the same github repo
you used for HW02. The functions you need to write are 

#0 A function which takes as it's arguments two vectors stored as
lists and returns their sum, also stored as a list.


#1 A function which takes as it's arguments a vector stored as a list and a
scalar, and returns the scalar vector multiplication stored as a list.


#2 A function which takes as it's arguments a matrix, stored as a list of lists
where each component list represents a column of the matrix(you cannot represent
the matrix as a list of rows!) and a scalar and returns their product, also
stored as a list of lists where each component list represents a column. You
must use the function from problem #1. Failure to use this function will result
in an earned grade of 0.

#3 A function which takes as it's arguments two matrices stored as lists of
lists where each component list represents a column vector, and returns their
sum stored in the same manner. You must use the function in problem #0 in your
method here. Failure to use the function from problem #0 will reuslt in an
earned grade of 0.

#4 A function which takes as it's argument a matrix (stored as a list of lists,
each component list representing a column vector), and a vector stored as a
list, and returns the matrix-vector product. This function must compute the
matrix-vector product by calculating the neccessary linear combination of the
input matrices columns. All other methods of matrix-vector multiplication are
strictly forbidden and their use will result in a grade of 0. For this function
you must use the functions written for problem #0 and problem #1. Failure to use
these functions will result in an earned grade of 0.

#5 A function which takes as it's arguments two matrices, each stored as a list
of lists where each component list represents a column vector, and returns their
product stored in the same manner. To earn any credit on this problem you must
use the function from problem #4 to implement the matrix-vector method of
matrix-matrix multiplication. Use of any other method will result in an earned
grade of 0.
"""

import pytest



# Begin Example
# Problem #0

def add_vectors(vector_a: list,
                vector_b: list) -> list:
    """Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
    """ 
    result: list = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result

# End Example
# Note that you must add unit tests for problem 0!!!!!


#Problem 01



def Scal_Vec_mult(vector_c: list,
                  scalar_a: float) -> list:
    """
    Multiples the scalar to the vector.
    
    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding 
    element of the product of the input vector and the input scalar. Achieved 
    using a for loop.
    
    Parameters:
    ----------
    vector_c : list
        A vector that is stored as a list.
    scalar_a : float
        A scalar that acts as a float and is multiplied to each element of the
        vector

    Returns
    -------
    list
        The product of the input vector and scalar

    """
    result: list = [0 for element in vector_c]
    for index in range(len(result)):
        result[index] = vector_c[index] * scalar_a
    return result

 





   
#Problem 02



def Scal_Matr_mult(matrix_a: list,
                   scalar_b: float) -> list:
    """
    Multiplies a matrix by a scalar.
    
    Creates a result matrix stored as a list of lists. Each list is a vector of 
    its own and by calling our the previous function, overwrites each element 
    within each vector with the corresponding element of the product of the 
    vector and the input scalar.

    Parameters
    ----------
    matrix_a : list
        A matrix that is stored as a list of columns
    scalar_b : float
        A scalar that acts as a float and is multiplied to each column of the 
        matrix

    Returns
    -------
    list
        The product of the input matrix and scalar

    """
    result: list = []
    for index in range((len(matrix_a))):
        result.append(Scal_Vec_mult(matrix_a[index], scalar_b))
    return result







#Problem 03



def Matr_add(matrix_b: list,
             matrix_c: list) -> list:
    """
    Adds the two matrix inputs together.
    
    Creates a result matrix stored as a list of columns. Each list of columns
    is treated as a vector, and so the previous function of adding vectors is 
    called back. What returns is the sum of the input matricies.

    Parameters
    ----------
    matrix_b : list
        A matrix that is stored as a list of columns.
    matrix_c : list
        A matrix that is stored as a list of columns and has the same number of
        row and columns being compatable to add with the first matrix.

    Returns
    -------
    list
        The sum of the matricies.

    """
    result: list = []
    for index in range(len(matrix_b)):
        result.append(add_vectors(matrix_b[index], matrix_c[index]))
    return result





#Problem 04



def Matr_Vec_mult(matrix_d: list,
                  vector_d: list) -> list:
    """
    Multiplies the matrix and vector inputs together.
    
    The input matricies must be compatable with each other to multiply with 
    each other. Creates a result matrix stored as a list of columns. Each list 
    of columns is treated as a vector. 
    

    Parameters
    ----------
    matrix_d : list
        A matrix that is stored as a list of columns
    vector_d : list
        A matrix that is stored as a list of columns, being compatable to be 
        multiplied with the first matrix

    Returns
    -------
    list
        The product of the matirix and vector input.

    """
    matrix_res = [0 for element in matrix_d]
    result: list = [0]
    for index in range(len(vector_d)):
        matrix_res[index] = Scal_Vec_mult(matrix_d[index], vector_d[index])
    result = add_vectors(matrix_res[0], matrix_res[1])
    for index in range(2, len(matrix_res)):
        result = add_vectors(result, matrix_res[index])
    return result


  
    


#Problem 05



def Matr_Matr_mult(matrix_e: list,
                   matrix_f: list) -> list:
    """
    The product of two matricies.
    
    The input matricies must be compatable to be multiplied with each other. 
    Creates a result matrix stored as a list of columns. Every list of columns 
    is treated as a vector. Each vector is then multiplied within one another.
    The result is the product of the two matricies.

    Parameters
    ----------
    matrix_e : list
        A matrix that is stored as a list of columns.
    matrix_f : list
        A matrix that is stored as a list of columns, being compatable to be 
        able to be multiplied by the first input matrix.

    Returns
    -------
    list
        The product of the two input matricies. 
        
    """
    result: list = []
    for index in range(len(matrix_f)):
        result.append(Matr_Vec_mult(matrix_e, matrix_f[index]))
    return result
