def runcalc(x):
    x/0
try:
    runcalc(6)
except IndexError as i:
    print(i,'exception has occured')
except FileNotFoundError as f:
    print(f,'exception has occured')
except ZeroDivisionError as z:
    print(z,'exception has occured')
except Exception:
    print('An unknown exception has occured')