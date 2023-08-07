def prime():
    print("Enter the number to check whether it is prime or not ")
    num=int(input(" :"))
    count=0
    for prime_Iterator in range (2,(num%2)+1,1):
        if(num % prime_Iterator == 0):
            count+=1
            print("The number",num," is not prime.")
            break
        if(count==0):
            print("Entered number",num," is a prime number.")
prime()