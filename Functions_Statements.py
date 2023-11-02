### 9.Write a program containing functions fun1(), fun2() and fun3() and some statements. Add suitable code to the program such that you can use it as a module or a normal program

import mypack.str_op as sop

str1 = input('Enter a string :')
print('The length of',str1,'is',sop.fun1(str1))

str1 = input('Enter a string :')
str2 = input('Enter another string :')
print('Result of comparision str1 == str2 :',sop.fun2(str1,str2))


str1 = input('Enter a string :')
str2 = input('Enter another string :')
print('Result of concatenation str1 + str2 :',sop.fun3(str1,str2))