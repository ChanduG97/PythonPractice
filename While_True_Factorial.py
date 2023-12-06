#Write a program that receives an integer as input and finds its factorial.
# If a non-integer input is entered, then report an error and accept the input again.
# Continue this process until correct input is entered.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

while True:
    try:
        num = int(input("Please enter a positive integer: "))
        if num < 0:
            print("Sorry, factorials are only defined for non-negative integers.")
        else:
            break
    except ValueError:
        print("Sorry, that is not a valid integer.")

print("The factorial of", num, "is", factorial(num))