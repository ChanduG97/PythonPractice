# program to accept n value as positive integer, print the squares of numbers from 1 to n 
#if a negative number is entered, then raise value error and display a relavent error message and exit

class Squares(object):
    def __init__(self,l):
        self._limit = l
        self._val=1
    def __iter__(self):
        return self
    def __next__(self):
        if self._val>self._limit:
            raise StopIteration
        else:
            return_val = self._val * self._val
            self._val +=1
            return return_val
        
n = int(input('Enter n value: '))
try :
    if n<0:
        raise ValueError('Entered value is negative number \n')
except ValueError as v:
    print(v,'Enter a positive Integer')
for i in Squares(n):
    print(i,end='\n')