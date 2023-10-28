### 2. An online retailer provides express shipping for many of its items at a rate of $10.95 for the first item, and $2.95 for each subsequent item. Write a function that takes the number of items in the order as its only parameter. Return the shipping charge for the order as the function’s result. Include a main program that reads the number of items purchased from the user and displays the shipping charge.
def Shipping_Charge(no_of_item):
    if(no_of_item == 1): 
        return 10.95
    else:
        return 10.95+(no_of_item - 1)*2.95
no_of_item = int(input('Enter a numbers of item list : '))
print(Shipping_Charge(no_of_item))