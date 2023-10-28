# map function

data = [1,4,3,5,2,9,7,10]
print('Data is :',data)
#applying the lambda function to each element in the list using the map function
d1 = list(map(lambda i:i+1,data))
print('The result of map function is:',d1)