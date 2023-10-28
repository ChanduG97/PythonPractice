### 4. Write a program to read a list of numbers from the user and remove the two largest and two smallest values from it. Display the list with the values removed, followed by the original list. Your program should generate an appropriate error message if the user enters less than 5 values.

num = int(input("Enter the list of numbers"))
l1 = list()
count = 0
if num >= 5:
        for i in range(num):
            n = int(input("Enter the numbers:"))
            l1.append(n)
            count += 1
        l1.sort()
        l2=l1.copy()
        print("Remove the two largest values are :",l1[-2:])
        print("Remove the two smallest values are :",l1[:2])
        print("Remove values are:",l1[-2:],l1[:2])
        print("Original List :",l2)
else:
        print("Error , You enter less than 5 values")