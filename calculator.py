num1 = float(input("enter first no:  "))
num2 = float(input("enter second no:  "))
print("choose operation")
print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")
print("press 5 for modulo")
print("press 6 for square")

choice = (input("enter your choice: "))

if choice=='1':
   print("result = ", num1 + num2)

elif choice=='2':
   print("result = " ,num1 - num2)

elif choice=='3':
   print("result = " ,num1 * num2)

elif choice=='4':
   print("result = " ,num1 / num2)

elif choice=='5':
   print("result = " ,num1 % num2)

elif choice=='6':
   print("result = " ,num1 ** num2)
else:
   print("invaid choice ")
