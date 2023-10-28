#filter ( ) function
data = [1,3,5,2,4,9,8,7,10]
print('Data is:',data)
def is_even(i):
    return i % 2 == 0
#filter for even numbers using filter()
even_data = list(filter(is_even,data))
print('Even numbers are ',even_data)

