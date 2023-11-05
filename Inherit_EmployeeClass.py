# inherit form employee 5 class
class SalesPerson(Employee5):
    def __init__(self,n,a,i,r,s):
        super().__init__(n,a,i)
        self._region = r
        self._sales = s
    def bonus(self):
        return self._sales * 0.5
print("Sales person object")
s = SalesPerson('Lokesh',25,4712,'Canada',48000)
s.birthday()
print(s,' Pay for this object for 40 hours is :',s.calculate_pay(40))
print('Bonus is :',s.bonus())