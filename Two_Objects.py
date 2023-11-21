class Organization:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

class Employee:
    def __init__(self, name,age):
        self.name = name
        self.age = age

# Creating an organization and adding employees
org1 = Organization("LMN Pvt Ltd.")
org2 = Organization("UI Pvt Ltd.")

emp1 = Employee("Marif",25)
emp2 = Employee("Sandeep",26)
emp3 = Employee("Lokesh",25)
emp4 = Employee("Usman",25)
emp5 = Employee("Jyothi",24)
emp6 = Employee("Teja",22)
emp7 = Employee("Chandu",25)
emp8 = Employee("Mahesh",25)
org1.add_employee(emp1)
org1.add_employee(emp2)
org1.add_employee(emp3)
org1.add_employee(emp4)
org1.add_employee(emp5)
org2.add_employee(emp6)
org2.add_employee(emp7)
org2.add_employee(emp8)


# Accessing organization and employee information
print("Organization 1:", org1.name)
print("Employees in Organization 1:")
for employee in org1.employees:
    print("-", employee.name,", Age : ",employee.age)

print("\nOrganization 2:", org2.name)
print("Employees in Organization 2:")
for employee in org2.employees:
    print("-", employee.name,', Age : ',employee.age)
