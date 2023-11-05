# implement operator overloading on the quantithy class
class Quantity:
    def __init__(self,v=0):
        self._value = v
    def __add__(self,other):
        new_value=self._value + other._value
        return Quantity(new_value)
    def __sub__(self,other):
        new_value=self._value - other._value
        return Quantity(new_value)
    def __pow__(self,other):
        new_value=self._value ** other._value
        return Quantity(new_value)
    def __lt__(self,other):
        new_value = self._value < other._value
        return Quantity(new_value)
    def __str__(self):
        return str(self._value)
    
q1 = Quantity(12)
q2 = Quantity(18)
q3 = Quantity()
print('Q1 = ',q1)
print("Q2 = ",q2)
q3 = q1+q2
print('the sum = ',q3)
q4 = q1-q2
print("the sub = ",q4)
q5 = q1 ** q2
print('The power of ',q1,'&',q2,'is :',q5)

if q1<q2:
    print(q1,'is lessthan ',q2)
q6 = q1<q2
print(q1,'is lessthan ',q2,'is :',q6)
