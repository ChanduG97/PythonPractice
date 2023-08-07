#create a student table with data student name student roll no student  age and student marks
import os
import pickle
os.getcwd()
mylist=[]
studentdata = open("C:\\Users\\navee\PycharmProjects\pythonProject\\venv\studentdata.txt","w+")
studentdata.write("Student Name Roll-no Age Marks")
while True:
    Student_Name = input("Enter Student name : ")
    mylist.append(Student_Name)
    Rollno=int(input("Enter Roll NO: "))
    mylist.append(Rollno)
    Age = int(input("Enter age: "))
    mylist.append(Age)
    Marks = float(input("Enter total marks obtained: "))
    mylist.append(Marks)
    studentdata.write(str(mylist))
    conformation = input("Doy you want to add more Data [Y/N] : ")
    if conformation.upper()=="Y":
        continue
    else:
        break
studentdata.seek(0,0)
print(studentdata.readlines())

