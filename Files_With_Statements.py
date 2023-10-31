# using files and with statement
with open('mynewfile.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        print(line,end='')