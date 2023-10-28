#factorial of a number using recursion
def fact(x):
    if x<=1:
        return 1
    else:
        return x*fact(x-1) #recursive call

n = int(input('Enter a number :'))

print("The factorial of ",n,'is ',fact(n))