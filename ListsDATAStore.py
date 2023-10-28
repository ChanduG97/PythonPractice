### 3. Write a program that reads integers from the user and stores them in a list. Your program should continue reading values until the user enters 0. Then it should display all of the values entered by the user (except for the 0) in order from smallest to largest, with one value appearing on each line. Use either the sort method or the sorted function to sort the list.


list1 = list()
count= 0
n = 1
while n != 0:
    num = int(input("Enter the integer :"))
    list1.insert(count,num)
    count += 1
    n =  num
list1.sort()
print('The sorted values are: ',list1)