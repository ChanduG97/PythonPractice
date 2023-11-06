def my_function(x,y):
    print('start my_function')
    result = x/y
    print('Exiting my_function')
    return result
print('Starting...')
try:
    print('before functin call..')
    res = my_function(5,0)
    print('The returned result is',res)
    print('after function call...')
except ZeroDivisionError as exc:
    print(exc,'error raised')
print('end')