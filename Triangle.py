### 4. Write a function that determines whether or not three lengths can form a triangle. The function will take 3 parameters and return a Boolean result. In addition, write a program that reads 3 lengths from the user and demonstrates the behavior of this function. In general, if any one length is greater than or equal to the sum of the other two then the lengths cannot be used to form a triangle. Otherwise they can form a triangle.

def triangle(a,b,c):
        if a+b > c and b+c > a and  c+a > b:
            return True
        else:
            return False
a = int(input('Enter the side a :'))
b = int(input('Enter the side b :'))
c = int(input('Enter the side c :'))    
result=triangle(a,b,c)
print('Entered sides can form triangle : ',result)