income =int(input("Enter Your Salary : "))
tax_payable = 0
print("Given Salary : ", income,"\n","-"*50)


if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # Tax is 8% tax
    print("Tax is 8%.")
    tax_payable = x * 8 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 8% tax
    tax_payable = 10000 * 8 / 100

    # remaining 16% tax
    tax_payable += (income - 20000) * 16 / 100

print("Total tax to pay is", tax_payable)