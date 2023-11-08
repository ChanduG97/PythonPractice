# a simple decorator
def my_decorator(func):
    def wrapper():
        print('-'*50)
        func()
        print('-'*50)
    return wrapper
@my_decorator
def display():
    print('Welcome to Decorators...')
display()