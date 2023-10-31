# program to read the contents of an Existing file
file = open('messages.txt','r')
lines = file.readlines()
for line in lines:
    print(line,end = '')
file.close()