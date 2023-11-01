### 5.Write a program to copy the contents of one file into another

source_file = input("Enter the name of source file :")

destination_file = input("Enter the name of the destination :")

f1 = open(source_file,'r')

f2 = open(destination_file,'w') # opening the file in write mode

while True:
    data = f1.read(1)
    if data == '':
        break
    f2.write(data)

f1.close()
f2.close()