### 1.Write a program that read contents of the file ‘messages’ one character at a time and prints each character that is read.


f1 = open('messages.txt','r') # opening file in read mode

lines = f1.read() # reading all the lines of the file in a list called lines

for line in lines: # iterate through the list one item ata time
    print(line,end='')
    
f1.close()