a = int(input("enter a number1: "))
b = int(input("enter a number2: "))
c = int(input("enter a number3: "))
def largest(a, b, c):
    if(a > b and a > c):
        print(f"{a}  is greater.")
    elif(b > a and b > c):
        print(f"{b} is greater.")
    else:
        print(f"{c} is greater.")

largest(a, b, c)