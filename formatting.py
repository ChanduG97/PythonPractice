### 10. Write a function that takes a list of strings as its only parameter. Your function should return a string that contains all of the items in the list formatted in the manner described previously as its only result. While the examples shown previously only include lists containing four elements or less, your function should behave correctly for lists of any length. Include a main program that reads several items from the user, formats them by calling your function, and then displays the result returned by the function. Consider the following four lists:

### apples
### apples and oranges
### apples, oranges and bananas
### apples, oranges, bananas and lemons

def formatting (lst2):
    s = ''
    s += lst2[0] 
    for i in (lst2[1:-1]):
        s = s + ', '+ i
    s = s + ' and ' + lst2[-1]
    return s
a = input('Enter the elements seperated with space : ')
b= list(a.split(' '))
print(formatting(b))