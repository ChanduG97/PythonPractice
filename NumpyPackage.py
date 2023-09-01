import numpy as np

#zeroDarray = np.array([4,8,5]) #--> single dimension
#zeroDarray = np.array([[4,8,5],[2,3,5]]) #--> 2 dimension [[[4,5]]]
zeroDarray = np.array(5)  #--> 3 Dimension
onedimension = np.array([4,5,6])
twodimension = np.array([[1,2,3],[4,5,6]])
threedimension = np.array([[[[1],[2]][1],[1]]])
print("zero dimension array is : \n",zeroDarray)  #--> Prints the given array
print("The Dimension of the array is :",zeroDarray.ndim) #--> ndim is used to find the dimension of the array
print("The size of the array is : ",zeroDarray.size) #--> size represents the length of the array (No of elements of the array)
print("The Shape of the array is : ",zeroDarray.shape) #--> shape declares the items present in the each dimension
print('\n------------------------------------------------------------')
print("One dimension array is :\n ",onedimension)
print("The Dimension of the array is :",onedimension.ndim)
print("The size of the array is : ",onedimension.size)
print("The Shape of the array is : ",onedimension.shape)
print('\n------------------------------------------------------------')
print("Two dimension array is :\n ",twodimension)
print("The Dimension of the array is :",twodimension.ndim)
print("The size of the array is : ",twodimension.size)
print("The Shape of the array is : ",twodimension.shape)
print('\n------------------------------------------------------------')

print("Three dimension array is :\n ",threedimension)
print("The Dimension of the array is :",threedimension.ndim)
print("The size of the array is : ",threedimension.size)
print("The Shape of the array is : ",threedimension.shape)
print('\n------------------------------------------------------------')


'''
list shape is 1 then tuple shape is 0 
if list shape is 2 then with the same size and elements the tuple shape is 1
    that means list = -1 of tuple ( shape)
'''

#Arithematic operations on Arrays (zero dimension)
zeroarray = np.array(100)
zeroarray1 = np.array(200)
resultarray = zeroarray+zeroarray1
print("--> Addition operation <--")
print("The addition result array is : \n",resultarray)
print("The Dimension of the array is :",resultarray.ndim)
print("The size of the array is : ",resultarray.size)
print("The Shape of the array is : ",resultarray.shape)
print('\n------------------------------------------------------------')

zeroarraytp = np.array((100))
zeroarraytp1 = np.array((200))
resultarraytp = zeroarraytp +zeroarraytp1
print("The addition result array is : \n",resultarraytp)
print("The Dimension of the array is :",resultarraytp.ndim)
print("The size of the array is : ",resultarraytp.size)
print("The Shape of the array is : ",resultarraytp.shape)
print('\n------------------------------------------------------------')

zeroarrayl = np.array([100])
zeroarrayl1 = np.array([200])
resultarrayl = zeroarrayl +zeroarrayl1
print("The addition result array is : \n",resultarrayl)
print("The Dimension of the array is :",resultarrayl.ndim)
print("The size of the array is : ",resultarrayl.size)
print("The Shape of the array is : ",resultarrayl.shape)
print('\n------------------------------------------------------------')

#one dimension array
onedarray = np.array([1,5,9,12])
onedarray1 = np.array([-10,-11,7,9])
resultonedarray = onedarray - onedarray1
print("--><--")
print("The one dimension array is : ",onedarray)
print("The one dimension array 1 is : ",onedarray1)
print("The subtration of one dimension array and one dimension array 1 is : ",resultonedarray)
print("The Dimension of one dimension array is : ",resultonedarray.ndim)
print("The shape of one dimension array is : ",resultonedarray.size)
print("The Shape of the array is : ",resultonedarray.shape)
print('\n------------------------------------------------------------')
# Operations on one dimension with scalar or ( zero dimension )
onedarray2 = np.array([1,5,9,12])
onedarray12 = np.array(10) #-->Scalar
resultonedarray2 = onedarray2 * onedarray12
print("\n-->Multiplication Operation<--")
print("The one dimension array is : ",onedarray2)
print("The one dimension array 1 is : ",onedarray12)
print("The multiplication of one dimension array and one dimension array 2 is : ",resultonedarray2)
print("The result Dimension of one dimension array  is : ",resultonedarray2.ndim)
print("The shape of result one dimension array is : ",resultonedarray2.size)
print("The Shape of the result array is : ",resultonedarray2.shape)
print('\n------------------------------------------------------------')

