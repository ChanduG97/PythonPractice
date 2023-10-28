#default parameters
def greeter(name,prompt='Welcome',msg = 'to the python programming'):
    print(name,prompt,msg)
greeter('Chandu')
greeter('Chandu',msg='India')
greeter(name='Chandu',msg='Welcome',prompt='Hello')