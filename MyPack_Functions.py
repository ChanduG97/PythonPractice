### 10.Suppose a module called mod.py contains functions f1(), f2() and f3(). Write three forms of import statements to use these functions in your program

import mypack.mod as mod
num1 = int(input('Enter the first number :'))
num2 = int(input('Enter the second number :'))
print('The modulus of',num1,'and',num2,'is',mod.f1(num1,num2))

num1 = int(input('Enter the first number :'))
num2 = int(input('Enter the second number :'))
print('The division of',num1,'and',num2,'is',mod.f2(num1,num2))

num1 = int(input('Enter the first number :'))
num2 = int(input('Enter the second number :'))
print('The multiplication of',num1,'and',num2,'is',mod.f3(num1,num2))