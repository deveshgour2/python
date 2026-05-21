num = int(input("enter the  number for finding factorial: "))

if(num < 0):
    print("factorial is not defined for negtaive number")

else:
    factorial = 1
    for i in range(1 , num + 1):
        factorial = factorial * i
    print(f"factorial of {num} = {factorial}")

    