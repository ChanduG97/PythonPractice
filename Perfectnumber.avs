### 9. An integer, n, is said to be perfect when the sum of all of the proper divisors of n is equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2, 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28. Write a program that determines whether or not a positive integer is perfect. Your program will accept a number from the user. If that number is a perfect number then your program will display true. Otherwise it will display false.

n = int(input("Enter an integer :"))
sum = 0
for i in range(1,n):
      if n % i == 0:
        sum += i
if sum == n:
        print("The number",n,"is a perfect number TRUE")
else:
        print("The number",n,"is not a perfect number  FALSE")