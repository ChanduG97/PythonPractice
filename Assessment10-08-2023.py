import os
class GoodsGST:
    ProductName = "Product Name"
    Quantity = "Qty"
    Price = "Price"
    GstPercentage = "GST Percentage"

    def __init__(self,PName,Qty,Price,GstPc):
        self.ProductName = PName
        self.Quantity = Qty
        self.Price = Price
        self.GstPercentage = GstPc
    def DisplayDetails(self):
        print("The Attributes are : ","\n",self.ProductName,"\n",self.Quantity,"\n",self.Price,"\n",self.GstPercentage)
    def UpdateValues(self):
            self.ProductName = input("Enter The name of the Product : ")
            self.Quantity = int(input("Enter the Quantity of the Product : "))
            self.Price = int(input("Enter the price of the Product : "))
            self.GstPercentage = float(input("Enter The GST Percentage : "))
    def CalculateGST(self):
        GST = (self.Price * (self.GstPercentage / 100))
        print("The GST on ",self.ProductName,"is : ",GST)

emptyObj = GoodsGST("self",1,2,3)
emptyObj.DisplayDetails()
emptyObj.UpdateValues()
emptyObj.CalculateGST()

print(os.getcwd())
NewFile = open("C:\\Users\\navee\PycharmProjects\pythonProject\\venv\GoodsInfoFile.txt","a+")
NewFile.seek(0,0)
