import numpy as np
twoDarray = np.array([[1,2],[3,4]],dtype=int)
imatrix = np.eye(1,dtype=int)
print("2D matrix is : \n",twoDarray)
print("1D I matrix is :\n",imatrix)
print("\n<----------------------------------------------->")

#operations on matrices
#Addition
addition_of_matrices = twoDarray + imatrix
print("The addition of 2 matrices are : \n",addition_of_matrices)
print("\n<----------------------------------------------->")
#multiplicaiton
mul_of_matrices = twoDarray * imatrix
print("The multiplicaiton of two matrices are : \n",mul_of_matrices)
print("\n<----------------------------------------------->")
#creating 2D I matrix
imatrix2d = np.eye(2,dtype=int)
print("2D matrix is : \n",twoDarray)
print("2D I matrix is :\n",imatrix2d)
print("\n<----------------------------------------------->")
#operations on matrices
#Addition
addition_of_matrices = twoDarray + imatrix2d
print("The addition of 2 matrices are : \n",addition_of_matrices)
print("\n<----------------------------------------------->")
#multiplicaiton
mul_of_matrices = twoDarray * imatrix2d
print("The multiplicaiton of two matrices are : \n",mul_of_matrices)
print("\n<----------------------------------------------->")
#Operations perform with ones matrices

#creating ones matrix
onesmatrix = np.ones((2,2),dtype=int)
print("The ones matrix is :\n",onesmatrix)
print("\n<----------------------------------------------->")
#multiplication with 2D matrix and ones matrix
mul_with_ones_and_2d = twoDarray * onesmatrix
print("The multiplication of 2D and ones is :\n",mul_with_ones_and_2d)
print("\n<----------------------------------------------->")

#addition of ones matrix and 2D matrix
add_with_ones_and_2d = twoDarray + onesmatrix
print("The addition of 2D and ones is : \n",add_with_ones_and_2d)
print("\n<----------------------------------------------->")

#multiplication of I matrix and Ones matrix
mul_with_ones_and_i = imatrix * onesmatrix
print("The multiplication of 2D and ones is :\n",mul_with_ones_and_i)
print("\n<----------------------------------------------->")

#Addition of I matrix and Ones matrix
add_with_ones_and_i = imatrix + onesmatrix
print("The addition of 2D and ones is : \n",add_with_ones_and_i)
print("\n<----------------------------------------------->")