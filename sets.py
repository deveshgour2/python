set1= {100,23,315,4}
print("set1= ",set1)

#add element in sets
set1.add(556)
print("updated set= ",set1)

#remove element from set
set1.remove(4)
print("set after removing element= ", set1)

#length of a set
print("length of set= ",len(set1))

#element exist in set  or not
n= int(input("enter element for search= "))
if n in set1:
    print("element found")

else:
    print("not found")

#copy of set
set2 = set1.copy()
print("set 2= ", set2)

#union of two sets
set3= {56, 35 , 23, 65}
print("set 3= ", set3)
print("union of sets  = ", set2.union(set3))

#intersection of sets
print("intersection of sets= ", set3.intersection(set2))

#difference of sets
print("difference of two sets= ",set2.difference(set3))

#symmetric difference of set
print("symmetric difference= ", set3.symmetric_difference(set2))

#check subset or not
print("subset= ",set2.issubset(set3))

set4= set()
for i in range(4):
    n=int(input("enter elements of sets= "))
    set4.add(n)
print("set 4= ",set4)