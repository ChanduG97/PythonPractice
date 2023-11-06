# program to implement an iterator called Evens that returns the even nummbers upto a limit
class Evens:
    def __init__(self,l):
        self._limit = l
        self._value = 0
        # the __iter__ makes this class iterable
        
    def __iter__(self):
        return self
    # the __next__ method makes this class an iterator
    def __next__(self):
        if self._value >  self._limit:
            raise StopIteration
        else:
            return_value = self._value
            self._value +=2
        return return_value
        
print('Start Iterator')
n = int(input('Enter the limit (n) :'))
print('Even numbers from 0 to',n)
for i in Evens(n):
    print('i =',i)
print('End of the Iterator')