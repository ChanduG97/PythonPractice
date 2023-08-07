def age_Eligibility(age,Nationality):
    if(age>18):
        print("Person is Adult")
        if(Nationality.upper()=="INDIAN"):
            print("Person is eligible for Vote")
        else:
            print("Person is not eligible for Vote")
    else:
        print("Person age is lessthan 18, not eligible for Vote.")
        return age
age = int(input("Enter Age : "))
Nationality=input("Enter Nationality : ")
age_Eligibility(age,Nationality)