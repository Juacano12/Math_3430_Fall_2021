
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




#Homework 4




#Problem 1

def abs_val(scalar_c: complex) -> float:
    """
    Returns the absolute value of the input scalar
    
    Found by taking the comlplex conjugate of the input scalar, then multiplying 
    the conjugate with the original scalar, and then finally taking the square 
    root of the scalar.

    Parameters
    ----------
    scalar_c : complex
        A combination of a real and imaginary number.

    Returns
    -------
    float
        The absolute value of the scalar.

    """
    def comp_conj(scalar_c: complex) -> float:
        """
        Finds the complex conjugate of the scalar
        
        Done by taking a complex scalar and multiplying its imaginary number 
        by -1.

        Parameters
        ----------
        scalar_c : complex
            A combination of a real and imaginary number

        Returns
        -------
        float
            The complex conjugate of the input scalar.

        """
        cj: complex = complex(scalar_c.real, scalar_c.imag * -1)
        return cj
    result: float = (scalar_c*comp_conj(scalar_c)) ** (1/2)
    return result.real





 

#Problem 2

def p_norm(vector_e: list,
           scalar_d: float = 2) -> float:
    """
    Finds the p-norm of the input vector.
    
    This is done by taking the absolute value of each element within the vector
    and multiplying it to the power of the input scalar, adding it to the final
    total.

    Parameters
    ----------
    vector_e : list
        A vector capable of taking complex numbers. 
    scalar_d : float, optional
         The default is 2.

    Returns
    -------
    float
        The p-norm of the vector.

    """
    result: float = 0
    for element in vector_e:
        result += (abs_val(element) ** scalar_d)
    result **= (1 / scalar_d)
    return result 





   
#Problem 3

def inf_norm(vector_f: list) -> float:
    """
    Finds the infinite norm of the input vector.
    
    Done by finding the absolute value of each element in the input vector,
    then finding and returning the max of those elements. 

    Parameters
    ----------
    vector_f : list
        A vector capable of taking complex numbers.

    Returns
    -------
    float
        The infinite norm of the vector.

    """
    result: float = None
    vector_f = [abs_val(element) for element in vector_f]
    result = max(vector_f)
    return result





#Problem 4

def p_norm_2(vector_g: list,
             scalar_e: float = 2,
             infi: bool = False) -> float:
    """
    Finds the p-norm or the infinite norm of the input vector. 
    
    If the infi is false it will run the previous def of p_norm, however if it
    is true, then it will run the previous def of inf_norm.

    Parameters
    ----------
    vector_g : list
        A vector capable of taking complex numbers.
    scalar_e : float, optional
        The default is 2.
    infi : bool, optional
        The default is False.

    Returns
    -------
    float
        The p_norm of the vector if false. The inf_norm of the vector if true.

    """
    result: float = None
    if not infi:
        result = p_norm(vector_g, scalar_e)
    else:
        result = inf_norm(vector_g)
    return result




#Problem 5

def inn_prod(vector_h: list,
             vector_i: list) -> complex:
    """
    Finds the inner product of both input vectors.
    
    Done by finding the conjugate of the first vector and then multiplying it 
    to the second vector. Finally it adds each element with the result. 

    Parameters
    ----------
    vector_h : list
        A vector capable of holding complex numbers.
    vector_i : list
        A vector capable of holding complex numbers. Must be compatable to be
        multiplied to the first vector.
        
    Returns
    -------
    complex
        The inner product of both vectors.

    """
    cj: complex = [complex(element.real, element.imag * -1) for element in vector_h]
    result: complex = 0
    for h_element, i_element in zip(cj, vector_i):
        result += h_element * i_element
    return result

