# implement the Timer decerator (returns calculation or execution time)

import time
def timer(func):
    def calculate(*args,**kwargs):
        start_time = time.perf_counter()
        value = func(*args,**kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print('Execution time is ::{0:10.10f}secs'.format(run_time))
        return value
    return calculate

@timer
def factorial(n):
    fact  = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact
    
factorial(9)