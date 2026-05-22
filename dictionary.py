student ={
    "name" : "devesh",
    "marks" : 88
}
print(student["name"])
print(student["marks"])

#insert new key in dictionary
student["roll_no"]=44
print("dictionary= ",student)

#update key
student["marks"]=99
print("updated dictionary= ",student)

#pop an element
student.pop("marks")
print("dictionary after poping= ", student)

#length of dictionary
print("length of dictionary= ",len(student))

#key exist or not 
n = str(input("enter the key: "))
if n in student:
    print("exist in dictionary")

else:
    print("not exist")
