# function which return function as return value

def check(s):
    if s == 'even':
        return lambda n : n%2==0
    elif s == 'positive':
        return lambda n : n>=0
    elif s == 'negative':
        return lambda n : n<0

    
f1 = check('even')
f2 = check('positive')
f3 = check('negative')

print('f1(5) = ',f1(5))
print('f2(5) = ',f2(5))
print('f3(5) = ',f3(5))
