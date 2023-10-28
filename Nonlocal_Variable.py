# function within a function - nonloacl variables

def func():
    x = 100
    print('X = ',x) #local variable value to func
    def func1():
        nonlocal x
        x += 1
        print('The value of x after incement :',x)
    func1()
func()
