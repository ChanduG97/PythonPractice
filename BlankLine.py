### 5. In this exercise, you will create a program that reads words from the user until the user enters a blank line. After the user enters a blank line your program should display each word entered by the user exactly once.

words  = []
word = input("Enter a word:")
while word !='':
    if word not in words:
            words.append(word)
    word = input ('Enter a word until enters a black line:')
print ('your all letters are :',words)