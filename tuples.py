tuple1= ("apple", " mango", "banana", "orange","guava")
print("tuple= ", tuple1)
print("first element of tuple: ",tuple1[0])
print("last element of tuple: ",tuple1[-1])

#length of  tuple 
print("length of tuple: ",len(tuple1))

#find index of an element 
tuple2=(56, 48, 50)
print("tuple2: ",tuple2)
n = int(input("enter the number for finding its index: "))
if n in tuple2:
    i = tuple2.index(n)
    print("found at index: ", i)
else:
    print("element not found in tuple")


#convert list into tuples
list1 = [2,5,62]
tuple3 = tuple(list1)
print("tuple3: ", tuple3)

#convert into list
list2 = list(tuple1)
print("list: ", list2)

#concatenate two tuples
tuple4 = tuple1 + tuple2
print("concatenate tuple: ", tuple4)

#element found  in tuple or not
n= input("enter the element for finding in tuple: ")
if int(n) in tuple2:
    print("element found")
else:
    print("not found")

