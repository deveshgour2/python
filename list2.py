list = []
for i in range(5):
    n= int(input("enter the value of lists: "))
    list.append(n)

print(list)

#create a list of square from 1 to 10
square = [x*x for x in range (1,11)]
print("square of 1 to 10: ",square)

#creating of second list
list2 = []
for i in range(5):
    n= int(input("enter the value of list2: "))
    list2.append(n)
print("list2: ", list2)

#merge two list
list3 = list + list2
print("merged list: ", list3)

#copy of list 
list4 = list3.copy()
print("copy list: ", list4)

#common elements in lists
for i in list:
    if i in list2:
        print("common elements from list1 and  list2: ", i)


