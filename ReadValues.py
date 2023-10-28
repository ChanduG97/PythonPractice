### 8. Write a program that reads values from the user until a blank line is entered. Display the total of all of the values entered by the user (or 0.0 if the first value entered is a blank line). Complete this task using recursion. Your program may not use any loops. The body of your recursive function will need to read one value from the user, and then determine whether or not to make a recursive call. Your function does not need to take any parameters, but it will need to return a numeric result.

def fun():
    n = input("Enter a value: ")
    if n =="":
        return 0.0
    else:
        return (int(n) + fun())
print("Total of all the values = ", fun())