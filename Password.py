### 7. In this exercise you will write a function that determines whether or not a password is good. We will define a good password to be a one that is at least 8 characters long and contains at least one uppercase letter, at least one lowercase letter, and at least one number. Your function should return true if the password passed to it as its only parameter is good. Otherwise it should return false. Include a main program that reads a password from the user and reports whether or not it is good.
def password(pw):
    
    length = lower = upper = digit = False
   
    if len(pw) >= 8:
        length = True
        
        for letters in pw:
            
            if letters.islower():
                lower = True
            
            if letters.isupper():
                upper = True
            
            if letters.isdigit():
                digit = True
            
    if length and upper and lower and digit:
        print('Entered password is good')
        return True
    
    else:
        print('Entered paassword is not good')
        return False   

pw = input('Enter the password: ')

password(pw)