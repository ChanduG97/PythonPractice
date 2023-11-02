### 7.Suppose a file contains student records, with each record containing name and age of student. Write a program to read these records and display them in sorted order by name

import json

f = open('student_record','w')

student = {'Loki':24,'Chandu':25,'Marif':26}

json.dump(student,f)

f.close()

import json 

f = open('student_record','r')

student = json.load(f)

print(student)

for line in sorted(student):
    print(line ,':' , student[line])
	