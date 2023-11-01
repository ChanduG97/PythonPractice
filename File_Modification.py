### 3.Write a program to accept a filename from the user, create a file with that name(if it does not exist) and write some content into the file

import json

file_name = input('Enter a file name :')

file = open(file_name,'w')

file.write('My name is Chandu\n')

file.write('I am on Week 6 currently on Python programming\n')
file.write('Completing the challenge \n')

file = open(file_name,'r')

lines = file.readlines()
for line in lines:
    print(line)