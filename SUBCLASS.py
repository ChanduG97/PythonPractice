class Companyclass:
    companyname = 'LMN'
    companyregistration="Pvt ltd"
    companyaddress = "Hyderabad"
    companysize = 100
    companylocation = "india"

    def __init__(self, cmpname, cmpreg, cmpaddress, cmpsize, cmplocation):
        self.companyname = cmpname
        self.companylocation = cmplocation
        self.companyaddress = cmpaddress
        self.companyregistration = cmpreg
        self.companysize = cmpsize
class CompanyITC(Companyclass):#--> Creating sub class and inheriting properties
    Products_ITC = ["Books","Cosmetics","Food","Stationary"] #--> List is used here to store the products
    Locations_ITC = {"Hyderabad","Banglore","Chennai","Hyderabad","Delhi"}
    '''Set is used to store the locations, set wont allow duplicates so that we can have only unique locations '''
    def __int__(cls): #--> parent class has Self so we use another argument here. It is cls
        cls.Products_ITC = ["Electronics","Fruits","Vehicles",3]
        cls.Locations_ITC = {"Hyderabad","Chennai","Vizag","Delhi"}

    def DisplayCompanyDetails(self):
        print("The company details are : ","\n",self.Products_ITC,"\n",self.Locations_ITC)
        super().DisplayCompanyDetails()
itcObj = CompanyITC()
itcObj.DisplayCompanyDetails()
#print("The company Products and locations are : ",ITCObj.Products_ITC,"\n locaion is ",ITCObj.Locations_ITC)