# random file access
f = open('text.txt','w')
f.write('abcdefghijklmnopqrstuvwxyz\n')
f.write('Hello world!')
f.seek(6,0)
f.write('Bye')
f.seek(12,0)
f.write('HELLO')
f.close()
with open('text.txt','r') as f:
    for line in f:
        print(line,end='')