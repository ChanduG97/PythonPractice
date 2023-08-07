'''output:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5  '''

num = int(input("Enter a range to print : "))
for i in range(1,num+1):
    print("")
    for j in range(1,i+1):
        print(j,end=" ")