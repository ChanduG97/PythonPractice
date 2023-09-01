import numpy as np

myarray = np.array(0)
print("The elements in MyArray is  : ",myarray)

firstarray = np.arange(10) # arange is a range function returns values from starting value to end value -1
print("The arange function : ",firstarray)

range1 = np.arange(1,8) # given staring and ending value
print("arange functin returns value in particular range : \n",range1)

range2 = np.arange(5,55,5) # given starting and ending value with step count
print(":\n",range2)

onesarray = np.ones((1)) # creates one dimension array  with function ones
print("creates one dimension array  with function ones : ",onesarray)

ones = np.ones_like((2,3,2),dtype=int) #--> gives in single dimension
print("The ones like array is :",ones)

onesarray = np.ones((2,3,2)) #--> gives shape as input
print("\n",onesarray)

onesarray = np.array(((1,3,2)),dtype=int)
print("the ones aarray with shape of 1,3,2 is :\n",onesarray)

zerosarray = np.zeros((3,2),dtype=int)
print(zerosarray)

zerosarray = np.zeros_like((2,2),dtype=int) #gives 0's in single  dimension
print("",zerosarray)

lin_space = np.linspace(5,20,20) #(start value, stop value and no.of elements)
print(lin_space)

newarray = np.random.random(5) #--> 5 random numbers will print in one dimension array
print(newarray)
print("Size of random array function is  :",newarray.size)

rangearray = np.arange(2,20,3)
print("the range array is  :\n",rangearray)

myshapearray = np.reshape(rangearray,(3,2))
print("The reshaped range array is :\n,",myshapearray)

myshapearray[2,0]=1400
print("The index row of 2 and 0th column value is replaced from 14 to 1400 :\n",myshapearray)
#to access particular value from matrices. we can access with index number
print("The datatype of elements in range array is :",rangearray.dtype)
#rangearray[0][5]=int(20)
print("The updated value is : ",rangearray)

#operations
onesarray1 = np.ones((2,2))
onesarray1[1,1] = 5
onesarray1[0,1] = 3
newarray1 = 5 * onesarray1 - 3
print("The operations on onesarray1 is  :\n",newarray1)
#sorted array
print("The Random array is :",newarray)
sortedarray = np.sort(newarray)
print("The sorted random array is :",sortedarray)
#concatination
firstarray1 = np.array([1,5])
secondarray1 = np.array([2,4])
#number of rows is equal to no of columns in next array
