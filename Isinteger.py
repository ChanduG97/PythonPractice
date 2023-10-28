### 5. In this exercise you will write a function named isInteger that determines whether or not the characters in a string represent a valid integer. When determining if a string represents an integer you should ignore any leading or trailing white space. Once this white space is ignored, a string represents an integer if its length is at least 1 and it only contains digits, or if its first character is either + or - and the first character is followed by one or more characters, all of which are digits. Write a main program that reads a string from the user and reports whether or not it represents an integer.

def isinteger(s):
    s=s.strip()
    if s.isdigit() or ((s[0]=='+' or s[0]=='-') and s[1:].isdigit()):
        return True
    else:
        return False
s=input('enter a string : ')
if isinteger(s):
    print('Entered string represent an Integer')
else:
    print('Entered string is not represent an Integer')