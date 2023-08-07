# 1.Write a program to find negative numbers in a tuple

tuple1 = (1,2,-2,-4,5,-4,-5,8,9,10,-10,-6)
count = 0
for i in tuple1:
    if(i < 0):
        count +=1
        print("Negative numbers are : ",i)


#2. From a string,concatinate a vowel for each characte in string and store it in a list
string1 = "string"
vowels = ["a","e","i","o","u"]
for i in string1:
    for j in vowels:
        print(i + j,end=" ")


# 3. Create a directory and create a file in the directory and print 3 multiples in the range of 51 to 71

import os
import pickle
print("The current working directory is : ",os.getcwd())
#os.mkdir('C:\\Users\\navee\PycharmProjects\pythonProject\\venv\chandu')
#os.chdir('C:\\Users\\navee\PycharmProjects\pythonProject\\venv\chandu')
print("The new directory is : ",os.getcwd())
newfile=open("C:\\Users\\navee\PycharmProjects\pythonProject\\venv\chandu\\text.txt",'a+')

#os.rmdir('C:\\Users\\navee\PycharmProjects\pythonProject\\venv\chandu')
#print(os.getcwd())

for i in range (0,101):
    newfile.write(str(i))
    newfile.write('\n')
for k in range(51,72):
    if k % 3 == 0:
        print(k," is divisible by 3",file=newfile,end='\n')

# 4 write a program in read mode only to read 10th character in line 2





''' 5 write a program to differentiate the data in a file as alphabets lower,upper and numbers int and float
special characters and escape sequence
'''


