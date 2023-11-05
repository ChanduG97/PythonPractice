# an example to demonstrate Containership
class Department:
    def set_department(self):
        self._id = input('Enter Department ID :')
        self._name = input('Enter Department Name :')
    def display_department(self):
        print('Department Id : ',self._id)
        print('Department Name :',self._name)
class Employee4:
    def set_employee(self):
        self._eid = input('Enter Employee ID :')
        self._ename = input('Enter Employee Name :')
        self._dept = Department()
        self._dept.set_department()
    def diaplay_employee(self):
        print('Employee ID : ',self._eid)
        print('Employee Name : ',self._ename)
        self._dept.display_department()         
emp = Employee4()
emp.set_employee()
print('-'*40)
emp.diaplay_employee()