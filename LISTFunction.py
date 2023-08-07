#List []
list1= [1,2,3,4,5,6]
print("The length of list1 is : ",len(list1))

#Empty list
list2 = []

#Lenght of list
print("The length of list2 is : ",len(list2))

# append is a function is used to add element in then end of the list
list1= [1,2,3,4,5,6]
print(list1)
list1.append(7)
print(list1)

#pop -> is used to remove last element in the list
list1= [1,2,3,4,5,6]
print(list1)
list1.pop()
print(list1)


#insert() function is used to add an Element in particular location
print("The list1 before adding any element :",list1)
list1.insert(0,0)
print("The list1 after adding 0 is : ",list1)
list1.insert(4,45)
print("The list after adding element in 4th index:",list1)

# Delete function
print("the values in list1 :",list1)
del list1[3]
print("After deleting 4th value in list1 is :",list1)

#List multiplication
list1= [1,2,3,4,5,6]
list3=['nikhil','Srikanth']
print("The list3 after multiplication : ",list3 * 4) #-> multiplication
print("The list1 after multiplied with 2: ",list1 * 2) #-> multiplicaton

#List Addition
list1=[1,2,3,4,5,6,7,8,9]
list3 = ['Srikanth','Bala','Nikhil']
print("After adding list1 and list3 is :",list1 + list3) #-> addition
list4 = list1 + list2 + list3
print("The list4 is adding of list1 list2 list3 :",list4)
print("after adding list1 and list3 : ",list4)
print("list1 after adding jyothi is: ",list1 + ['jyothi'])
print("List3 after adding jyothi name is : ",list3 + ['Jyothi'])

# clear the values in list
#Clear()
print("list 4 is:",list4)
list4.clear()
print('After clearing values in list4 : ',list4)

