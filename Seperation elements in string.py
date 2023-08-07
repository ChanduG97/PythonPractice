str1 = "Welcome EKIPIT @ madhapur. The session starts at 10:10 am."
num=" "
alpha=" "
special =" "
Upper=" "
for i in range (0,len(str1)):
    if str1[i].isdigit():
        num = num + str1[i]
    elif ((str1[i]>="A" and str1[i]<="Z")):
        alpha+= str1[i]
    elif ((str1[i]>="a" and str1[i]<="z")):
        Upper += str1[i]
    else:
        special+= str1[i]

print("\nThe Uppercase letters are : ",alpha,end=" ")
print("\nThe Lower case letter in string is:",Upper,end = " ")
print("\nThe numbers in string are :",num,end = " ")
print("\nThe special characters in string are : ",special,end=" ")