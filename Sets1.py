### 1. A set contains names which begin either with A or with B. Write a program to separate the names into two sets, one containing names beginning with A and the other containing names beginning with B

s1 = set()
s2 = set()
names = {'Anil','aneesha','Babu','Baby','avinash','bala','banti','Akshitha','Chandu'}
for i in names:
    if i.startswith('a'):
        s1.add(i)
    elif i.startswith('A'):
        s1.add(i)
    elif i.startswith('b'):
        s2.add(i)
    elif i.startswith('B'):
        s2.add(i)
    else:
        print('Name',i,' does not starts with a or b ')
print('Names starts with a in set1 :',s1)
print('Names starts with b in set2 :',s2)