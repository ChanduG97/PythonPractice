# write some msgs into a file called messagesnew.txt

print('Writing to a File')
f= open('mynewfile.txt','w')
f.write('Hello from Python\n')
f.write('Working with files is easy\n')
f.write('It is cool\n')
f.close()


file = open('mynewfile.txt','r')
lines = file.readlines()
for line in lines:
    print(line,end = '')
file.close()