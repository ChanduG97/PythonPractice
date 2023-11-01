# create a mymath module in a file called mymath.py

import mymath

x = int(input('Enter x value: '))
y = int(input('Enter y value: '))

print('sum of ',x,'and',y,'is: ',mymath.add(x,y))
print('multiplication of ',x,'and',y,'is: ',mymath.mul(x,y))
print('subtraction of ',x,'and',y,'is: ',mymath.sub(x,y))
print('division of ',x,'and',y,'is: ',mymath.div(x,y))
print('modular division of ',x,'and',y,'is: ',mymath.mod(x,y))