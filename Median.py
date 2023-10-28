### 3. Write a function that takes three numbers as parameters, and returns the median value of those parameters as its result. Include a main program that reads three values from the user and displays their median.
def median(a,b,c):
    if a > b:
        if a < c:
            return a
        elif b>c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b       
        else:
            return c
        
a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
c = int(input('Enter c value: '))
res = median(a,b,c)
print('The Median value is : ',res)