#positional and keyword arguments
def my_function(*args,**kwargs):
    for arg in args:
        print('Arg :',arg)
    for key in kwargs.keys():
        print('Key :',key,'has value',kwargs[key])
my_function('Chandu','Marif','Lokesh',friend1 ='Marif',friend2 = 'Lokesh')