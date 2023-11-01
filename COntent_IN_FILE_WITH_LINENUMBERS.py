### 4.Write a program to read a file and display its contents along with line numbers before each line

my_hob = ["My name is Chandu \n", "I like to play shuttle badminton \n", "I love to travel \n"]
  
with open("myhob.txt", "w") as mh:
    mh.writelines(my_hob)

count = 0
  
with open("myhob.txt") as mh:
    Lines = mh.readlines()
    for line in Lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))