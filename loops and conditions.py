def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def main():
    while True:
        print("1. Calculate Factorial")
        print("2. Check if a number is Prime")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            num = int(input("Enter a number to calculate its factorial: "))
            print(f"The factorial of {num} is: {calculate_factorial(num)}")
        elif choice == '2':
            num = int(input("Enter a number to check if it's prime: "))
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
