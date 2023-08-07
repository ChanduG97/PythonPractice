list1 = ["Chandu","Nikhil","Bala","Srikanth"]
list2 = [2,3,4,5,6]
print("The list 1 is  : ", list1)
print("The length of list 1 is : ",len(list1))
print("The type of list 1 is : ",type(list1))
print("The memory for list1 is : ",id(list1))

print("The list 2 is  : ", list2)
print("The length of list 2 is : ",len(list2))
print("The type of list 2 is : ",type(list2))
print("The memory for list2 is : ",id(list2))
list1 = list2
#Here we perform Shallow copy
print("The list 1 after shallow copy : ",list1)
print("The list 2 after shallow copy : ",list2)
print(type)
