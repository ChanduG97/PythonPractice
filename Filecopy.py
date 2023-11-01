# file copy application 
source_file = input('Enter the name of source file: ')
destination_file = input('Enter the name of destination file: ')
f1 = open(source_file,'r')
f2=open(destination_file,'w')
while True:
    data = f1.read(1)
    if data == '':
        break
    f2.write(data)
f1.close()
f2.close()