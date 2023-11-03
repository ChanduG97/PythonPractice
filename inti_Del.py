# __init__() and __del__() example

class employee1:
    def __init__(self,n='N/A',a=0,s=0.0):
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
    def __del__(self):
        print('Deleting the object : ',str(self))
	
e1 = employee1('Mahesh',24,60000)
e1.display_data()
e2 = employee1()
e2.display_data()
e3 = employee1('Sanjay',24,75000)
e3.display_data()