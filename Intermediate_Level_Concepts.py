#Generate a list of squares for numbers 0 to 9
print('-'*50)
squares = [x**2 for x in range(10)] #Using Lists
print(squares)


#Square for required number using List
n=int(input("Enter a Number to find Square : "))
squareN=[n**2]
print('-'*50)
print("Square of ",n,"is :",squareN)

#map filter
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(doubled)
print(evens)
