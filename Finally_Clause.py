#finally clause 

try:
    print('The result of my-function is:',my_function(6,0))
except ZeroDivisionError as z:
    print(z,'Exception raised')
else:
    print('Everything is working fine')
finally :
    print('This code always runs')