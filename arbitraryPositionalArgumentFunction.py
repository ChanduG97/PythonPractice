#arbitrary positional argument functions
def greeter(*args):
    for name in args:
        print('Welcome',name)
greeter("Naveen",'Marif','Lokesh')
greeter('Hyderabad','Ongole','Bengaluru')