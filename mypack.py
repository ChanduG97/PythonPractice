### 8.Suppose there are three modules m1.py, m2.py and m3.py containing functions f1(), f2() and f3() respectively. Write a program to use these functions

import mypack.m1 as f1
num1 = int(input('Enter the first number :'))
num2 = int(input('Enter the second number :'))
print('The addition of',num1,'and',num2,'is',f1.add(num1,num2))

import mypack.m2 as f2
num1 = int(input('Enter the first number :'))
num2 = int(input('Enter the second number :'))
print('The substraction of',num1,'and',num2,'is',f2.sub(num1,num2))


import mypack.m3 as f3
num1 = int(input('Enter the first number :'))
num2 = int(input('Enter the second number :'))
print('The multiplcation of',num1,'and',num2,'is',f3.mul(num1,num2))


