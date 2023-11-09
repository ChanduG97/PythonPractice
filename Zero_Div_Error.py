try:
    num = float(input('Enter a number :'))
    val = 50/num
except ZeroDivisionError as z:
    print(z,'Error raised')
except ValueError as v:
    print('ValueError raised',v)
else:
    print(val)