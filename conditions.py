def main():
    print("Welcome to the Python Operations App!")

    while True:
        print("\nChoose an operation:")
        print("1. Print numbers from 1 to N using 'for' loop")
        print("2. Check if a number is even or odd using 'if' condition")
        print("3. Sum of numbers from 1 to N using 'while' loop")
        print("4. Print numbers from 1 to N using 'do while' concept")
        print("5. Check the grade using 'elif' conditions")
        print("0. Exit")

        choice = input("Enter your choice (0-5): ")

        if choice == "0":
            print("Exiting the application. Goodbye!")
            break
        elif choice == "1":
            n = int(input("Enter the value of N: "))
            print_numbers_for(n)
        elif choice == "2":
            num = int(input("Enter a number: "))
            check_even_odd(num)
        elif choice == "3":
            n = int(input("Enter the value of N: "))
            sum_numbers_while(n)
        elif choice == "4":
            n = int(input("Enter the value of N: "))
            print_numbers_do_while(n)
        elif choice == "5":
            score = int(input("Enter the score: "))
            check_grade(score)
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

def print_numbers_for(n):
    print("Printing numbers from 1 to", n, "using 'for' loop:")
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")

def sum_numbers_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    print("Sum of numbers from 1 to", n, "using 'while' loop:", total)

def print_numbers_do_while(n):
    print("Printing numbers from 1 to", n, "using 'do while' concept:")
    i = 1
    while True:
        print(i, end=" ")
        i += 1
        if i > n:
            break
    print()

def check_grade(score):
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

if __name__ == "__main__":
    main()