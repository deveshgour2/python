list = [1,2,3,5,70]
print(list)

#first and last element of list
print("first element of list= ",list[0])
print("last element of list=",list[-1])

#append list
list.append(35)
print("append list: ",list)

#insert element at specific position
list.insert(2,20)
print("list after inserted element: ",list)

#remove an element from list
list.remove(70)
print("list after removing element",list)

#length of list
print("length of list: ",len(list))

#reverse a list
list.reverse()
print("reverse list: ", list)

#sort a list 
list.sort()
print("sorted list: ", list)

#maximum and minimum in list 
print("max in list: ",max(list))
print("min in list: ",min(list))

#sum of element of list
print("sum of list: ", sum(list))

#even numbers in a list
for i in list:
    if i%2==0:
        print("even no of list:",i)