# accessing global varibale within a fucntion
x = 100
def my_fun2():
    global x
    x+=1
    print('The value of x after increment is:',x)
my_fun2()
print("The value of x is:",x)