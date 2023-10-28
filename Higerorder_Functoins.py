# Higher order functions
def apply(x,fun):
    result = fun(x)
    return result
def square(n):
    return n*n
print(apply(4,square))