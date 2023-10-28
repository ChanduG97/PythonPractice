#reduce function
from functools import reduce
data = [1,4,3,6,8,9]
result = reduce (lambda total,value:total+value,data)
print('The sum of total data: ',result)
result2 = reduce(lambda total,value:total * value,data)
print('The multiplication of data using reduce() :',result2)