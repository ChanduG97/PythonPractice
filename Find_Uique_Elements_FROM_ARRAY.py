import numpy as np

myarray = np.array([[1,3,4,5],[7,3,4,2],[3,2,6,8]])
#Compare all the values and find only unique values
uniquevalues = np.unique(myarray)
print("The unique values are --> " ,uniquevalues)

unique_values,counts = np.unique(myarray,return_counts= True)
unique_values_list = unique_values[counts==1]
print("The Distinct values are --> ",unique_values_list)
