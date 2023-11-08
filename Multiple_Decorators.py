# demonstrate multiple decorators
def star(func):
    def inner(*args,**kwargs):
        print('*'*75)
        func(*args,**kwargs)
        print('*'*75)
    return inner
def percentage(func):
    def inner (*args,**kwargs):
        print('%'*75)
        func(*args,**kwargs)
        print('%'*75)
    return inner

@star
@percentage
def printer(msg):
    print(msg)

printer('program to illustrate the concept of multiple decorators')