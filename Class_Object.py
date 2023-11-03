# an example Employee class to demonstrate the class and objects
class employee:
    def set_data(self,n,a,s):
        self._name = n
        self._age = a
        self._salary = s
    def display_data(self):
        print('Name    : ',self._name)
        print('Age     : ',self._age)
        print('Salary  : ',self._salary)