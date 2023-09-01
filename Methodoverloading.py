def area():
    print("This calculates the area of the Square")


def area( side):
    area = side * side
    print("The Area of the square is  :", area)


def area( length, breadth):
    area = length * breadth


class area:
    def area(self):
        print("This calculates the area of the Square")
    def area(self,side):
        area = side * side
        print("The Area of the square is  :",area)
    def area(self,length,breadth):
        area = length*breadth
        print("The area of the Rectangle is : ",area)

a = area()
l = int(input("Enter Length : "))
b = int(input("Enter Breadth : "))
a.area(l,b)