# program to accept the value of n. Implements the iterator which returns factorial upto n
class Fact:
    def __init__(self,l):
        self._limit = l
        self._val = 0
        
    def __iter__(self):
        return self
    
    # to find the factorial of the number
   
    def fact(self,num):
        prod  = 1
        for i in range(1,num+1):
            prod *=i
        return prod
    
    def __next__(self):
        if self._val > self._limit:
            raise StopIteration
        else:
            return_val = self.fact(self._val)
            self._val += 1
            return return_val
print('Start Iterator')
n = int(input('Enter the limit (n>1) :'))
print('Factorial from 0 to',n)
for i in Fact(n):
    print('Factorial =',i)
print('End of the Iterator')