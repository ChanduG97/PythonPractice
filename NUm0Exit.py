### 6. Write a program that reads numbers from the user until a 0 is entered. Your program should display the average of all of the values entered by the user. Then the program should display all of the below average values, followed by all of the average values (if any), followed by all of the above average values. An appropriate label should be displayed before each list of values.

list1 = list()
below1 = list()
above1 = list()
sum = 0 
count = 1
while True:
    num = int(input('Enter the numbers : '))
    if num == 0:
        break
    else:
        list1.append(num)
        sum += num
        count += 1
avg = sum /count
print('Average of the numbers is: ',avg)
for i in list1:
    if avg>i:
        below1.append(i)
    else:
        above1.append(i)
print('The below average number is : ',below1)
print('The above average number is : ',above1)