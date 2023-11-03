# Demonostrate class variable and class method


class Employee2:
    instance_count = 0
    def __init__(self,n='N/A',a=0,s=0.0):
        Employee2.increment_instance_count()
        self._name = n
        self._age = a
        self._salary = s
    def set_data(self,n,a,s):
        self._name = n
        self._age = a
        self._salary = s
    def display_data(self):
        print('Name    : ',self._name)
        print('Age     : ',self._age)
        print('Salary  : ',self._salary)
    @classmethod
    def increment_instance_count(cls):
        cls.instance_count +=1
    
e1 = Employee2()
e2 = Employee2('Chandu',26,35000)
e3 = Employee2('Marif',25,40000)
print('Number of Employee objects are created : ',Employee2.instance_count)