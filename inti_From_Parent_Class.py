# Child class / sub class / derived clas

class Employee5(Person):
    def __init__(self,n,a,i):
        super().__init__(n,a)      #invoking __init__ from parent class
        self._id = i
    def calculate_pay(self,hours_worked):
        rate_of_pay = 7.50
        if self._age >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay
    
print('A person object only')
p = Person('Chandu',25)
print('The person object p is: ',p)
print('-'*50)
print("Employee object")

e = Employee5('Marif',25,2000)

e.birthday()

print(e,'pay of employee for 40 hours is :',e.calculate_pay(40))
print('-'*50)