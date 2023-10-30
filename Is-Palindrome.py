### 9. In this exercise you will write a recursive function that determines whether or not a string is a palindrome. The empty string is a palindrome, as is any string containing only one character. Any longer string is a palindrome if its first and last characters match, and if the string formed by removing the first and last characters is also a palindrome. Write a main program that reads a string from the user. Use your recursive function to determine whether or not the string is a palindrome. Then display an appropriate message for the user.
def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

str1 =str(input('Enter string : '))

if(is_palindrome(str1)==True):
    
    print('String',str1,'is a palindrome!')

else:
    print('String',str1,'is not a palindrome!')