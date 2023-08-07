import pickle
mylist=[]
file_handler = open("StudentsData.txt","ab+")
print("The empty list is:",mylist)
while True:
    stname = input("Student name : ")
    mylist.append(stname)
    print("The student name in mylist is : ",mylist[0])
    strollno = int(input("Student Roll no : "))
    mylist.append(strollno)
    print("The student RollNo in mylist is : ", mylist[1])
    stmarks = int(input("Student Marks : "))
    mylist.append(stmarks)
    print("The student Marks in mylist is : ", mylist[2])
    newreccord = input("You want to enter new record (Y/N) : ")
    pickle.dump(mylist,file_handler)
    if newreccord=="y":

        pass
    else:
        break