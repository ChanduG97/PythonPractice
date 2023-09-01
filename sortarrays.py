import numpy as np
myarray = np.array([[15.24,33.68,73.59],[3254,45.68,63.59],[51.54,28.39,9.29]])
print("The Original matrix is :\n",myarray)
print("\nSorting the above array by row in ascending order : ")
sortedarray = np.sort(myarray,axis=1) #--> if 1 it sorted by rows if 0 it sorted by column
print(sortedarray)
#by default the axis is 1
columnsortarray = np.sort(myarray,axis=0)
print("The sorting is done based on column in ascending order : ",columnsortarray)
#swap rows and columns
swapedarrays = myarray[::-1,::-1]
print("The swapped matrix is  : \n",swapedarrays)

#eye function gives the identity matrix ( square matrix ) 
#we have to pass a value, if we give 3 it gives 3 x 3 identity matrif that is all 1's are diagonal
#remaining elements in the matrix are 0

identirymatrix=np.eye(5,dtype=int)
print("The identity matrix is  : \n",identirymatrix)

givenarray = np.ones((2,2,3),dtype=int)
print("The given matrix is only ones :\n",givenarray)
likearray = np.zeros_like(givenarray)
print("The zeros like array is :\n",likearray)
print("The shape of like array is :",likearray.shape)


firstarray= np.array([1,2,3,4])
secondarray = np.array([[4,3,2,1]])
print("Original vectors are : \n",firstarray)
print("The second array is :\n",secondarray)
product = np.dot(secondarray,firstarray)
print("The inner product of given vectors is as follows : \n",product)

#transpose of an array
transposearray = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,1,1],[2,2,2],[3,3,3]]])
print("The original matrix is :\n",transposearray)
t=transposearray.transpose()
print("\n",t)