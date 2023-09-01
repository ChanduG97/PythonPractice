import numpy as np

square_matrix = np.array([[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[4,3,2,0,5]])
print("The given matrix is  : \n",square_matrix)
np.fill_diagonal(square_matrix,1)
print("The updated matrix is : \n",square_matrix)
