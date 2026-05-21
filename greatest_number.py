num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
num3 = float(input("enter third number"))

if(num1 >= num2 and num1 >= num3):
    print("number 1 is greater" , num1)

elif(num2 >= num1 and num2 >= num3):
    print("number 2 is greater" , num2)

else:
    print("number 3 is greater" , num3)