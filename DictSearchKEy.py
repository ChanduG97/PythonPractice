### 10. Write a program that finds all of the keys in a dictionary that map to a specific value. The program will take the value to search for as its input. It will display a (possibly empty) list of keys from the dictionary that map to the provided value.


str1 = input("Enter the value to search :")
capitals = {'Telangana':'Hyderabad', 'Tamil Nadu':'Chennai', 'Andhra Pradesh':'Hyderabad',
               'Karnataka':'Bengaluru','Maharastra':'Mumbai'}
print("The values will map the keys: ",list(key for key, value in capitals.items() if value == str1))