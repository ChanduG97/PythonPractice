# Class inheritance
#Parent class / super /base class

class Person:
    def __init__(self,n,a):
        self._name = n
        self._age = a
    def birthday(self):
        print('Happy Birthday, you were : ',self._age)
        self._age += 1
        print('Now you are ',self._age,'years old')
    def __str__(self):
        return self._name + ' is '+ str(self._age) +' years old'
print('A person object only')
p = Person('Chandu',25)
print('The person object p is: ',p)
print('-'*50)
print("Employee object")

e = Employee5('Marif',25,2000)

e.birthday()

print(e,'pay of employee for 40 hours is :',e.calculate_pay(40))
print('-'*50)