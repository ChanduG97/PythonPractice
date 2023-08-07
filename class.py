class Companyclass:
    companyname = 'LMN'
    companyregistration="Pvt ltd"
    companyaddress = "Hyderabad"
    companysize = 100
    companylocation = "india"
# creating constructor
    def __init__(self,cmpname,cmpreg,cmpaddress,cmpsize,cmplocation):
        self.companyname = cmpname
        self.companylocation=cmplocation
        self.companyaddress=cmpaddress
        self.companyregistration=cmpreg
        self.companysize=cmpsize
'''
    def __init__(self, cmpname, cmpreg, cmpaddress, cmpsize, cmplocation): #assigning default values to parameters
    #Default values should assign from right most item to left
        self.companyname = cmpname
        self.companylocation = cmplocation
        self.companyaddress = cmpaddress
        self.companyregistration = cmpreg
        self.companysize = cmpsize
'''
    def DisplayCompanyDetails(self):
        print("The company details are : ","\n",self.companyname,"\n",self.companyregistration,"\n",self.companyaddress,"\n",self.companysize,"\n",self.companylocation)
    def UpdateCompanyAddress(self):
        self.companyaddress=input("Enter the Company's New address : ")
        print("The new company address is : ",self.companyaddress)
    def companyEmpcount(self):
        print("The number of employees in the company is : ",self.companysize)

companyobj = Companyclass("HR & CO","Firm","Banjaara hills",100,"India")
companyobj1 = companyobj
companyobj.companyname="EKIP IT"
companyobj.companyregistration="MCA Registration"
companyobj.companysize="150"
companyobj.companyaddress="100ft road, Madhapur,Hyderabad"
companyobj.companylocation="India"
companyobj.DisplayCompanyDetails()
companyobj1.DisplayCompanyDetails()

# companyobj = Companyclass() --> find the error and pass argument (Task)
# How to create 1st object in class
