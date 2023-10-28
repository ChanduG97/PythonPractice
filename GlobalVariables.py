# global variable 

a_var = 200       #globla varible
def my_fun1():
    a_var=100     #local variable
    print('The value of a_var is :',a_var)  #returns local varibale value
my_fun1()
print('The value of a_Var is:',a_var)       #returns global varibale value
