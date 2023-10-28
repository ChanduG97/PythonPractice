### 6. In this exercise you will create a function named nextPrime that finds and returns the first prime number larger than some integer, n. The value of n will be passed to the function as its only parameter. Include a main program that reads an integer from the user and displays the first prime number larger than the entered value.

def nextprime(n):
    while True:
        n+=1
        for i in range(2,n):
            if n%i==0:
                break
        else:
            return n
n=int(input('Enter an Integer:'))
print('The prime number after',n,'is : ',nextprime(n))
