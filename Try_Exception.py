x = int(input('Enter x value:'))
y = int(input('Enter y value:'))
try:
    if y==0:
        raise ValueError('Division is not possible with 0')
    print('The result of diviaon is : ',my_function(x,y))
except ValueError as v:
        print(v)
else:
    print('Everything worked fine')