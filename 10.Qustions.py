#1 Reverse the tuple
tuple1 = (1,2,3,"Hai","Hello",5)
print("Reversing a tuple : ",tuple1[::-1])

#2 Access value 20 from the tuple
tuple2 = ("Hello","Welcome","India",[10,20,300],(1,2,3))
print("Accessing the value 20 from nnested tuple",tuple2[3][1])

#3: Create a tuple with single item 50
tuple3 =(50,)
print("The single valued tuple is :",tuple3)

# 4: Unpack the tuple into 4 variables
tuple4 = (1,2,3,4)
a,b,c,d = tuple4
print("Unpacking tuple")
print("The tuple is :",tuple4)
print("A value :",a)
print("B value :",b)
print("C value :",c)
print("D value :",d)

#5: Swap two tuples in Python
tuple5 = (10,20)
tuple6 = (30,40)
print("tuple5 is :",tuple5)
print("Tuple6 is :",tuple6)

tuple5, tuple6  = tuple6 , tuple5
print("Tuples after swap ")
print("Tuple5 :",tuple5,"\nTuple6 :",tuple6)

#6 Copy specific elements from one tuple to a new tuple
tuple7 = (1,2,3,4,5,6,7)
tuplecopy = tuple7[2:8]
print("The original tuple is :",tuple7,"\nCopied values in 2nd tuple is:",tuplecopy)

#7: Modify the tuple
tuple8 = (1,2,[3,4],5,6)
print("The original tuple is: ",tuple8)
tuple8[2][0]=66
print("The value after modified :",tuple8)

# 9: Counts the number of occurrences of item 50 from a tuple
tuple9 = (10,50,20,30,50,45,50,92,31,50)
print("The count of 50 in tuple is:",tuple9.count(50))


#10 Check if all items in the tuple are the same

def check(i):
    return all(a==i[0] for a in i)
tuple10=(10,10,10,10,10)
print("After checking value:",check(tuple10))
