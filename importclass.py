'''
----> What to Learn <----
--> How to Debugging
--> Importing packages
--> import particular class and functions
--> students classs, college class, department class etc...
--> import functions and classes from one program to another program
'''

class calculations:
    def add(self):
        a = int(input("Enter A value : "))
        b = int(input("Enter B Value : "))
        print("The sum of ",a,"and ",b,"is : ",a + b)
    def sub(self):
        a = int(input("Enter A value : "))
        b = int(input("Enter B value : "))
        print("The subtraction of ", a, "and ", b, "is : ", a - b)
    def multiply(self):
        a = int(input("Enter A value : "))
        b = int(input("Enter B value : "))
        print("The multiplication of ", a, "and ", b," is : ", a * b)
    def square(self):
        a = int(input("Enter A value : "))
        print("The Square of ", a ," is : ", a * a)
    def division(self):
        a = int(input("Enter a value : "))
        b = int(input("Enter B value : "))
        print("The division on ",a,"and ",b,"is : ",b/a)

