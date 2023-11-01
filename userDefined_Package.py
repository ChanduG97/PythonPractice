# create a package called mypack with the modules mymath and mystr
import mypack.mystr as ms
#or 
from mypack.mymath import *
str1 = input('Enter a string: ')
str2 = input('Enter another string : ')
print('Length of',str1,'is',ms.str_len(str1))
print('Length of',str2,'is',ms.str_len(str2))
print('Result of string comparision is : ',ms.str_cmp(str1,str2))
print('Result of string concatination is : ',ms.str_con(str1,str2))


x = int(input('Enter x value: '))
y = int(input('Enter y value: '))

print('sum of ',x,'and',y,'is: ',mymath.add(x,y))
print('multiplication of ',x,'and',y,'is: ',mymath.mul(x,y))
print('subtraction of ',x,'and',y,'is: ',mymath.sub(x,y))
print('division of ',x,'and',y,'is: ',mymath.div(x,y))
print('modular division of ',x,'and',y,'is: ',mymath.mod(x,y))


import mypack.myfile as mf

filename = input('Enter a file name in this directory: ')
print('The size of the file is: ',mf.file_size(filename))
