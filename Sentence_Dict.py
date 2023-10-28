### 7. Create a program that determines and displays the number of unique characters in a string entered by the user. For example, Hello World! has 9 unique characters while zzz has only one unique character. Use a dictionary to solve this problem.


sentance = input('Enter a sentance: ')
d = dict()
for i in sentance:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print('Number of unique characters are: ',len(d))