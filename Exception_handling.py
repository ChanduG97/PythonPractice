def runcalc(x):
    x/0
try:
    runcalc(6)
except ZeroDivisionError:
    print('Zero division error in runcalc function')