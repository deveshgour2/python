n = int(input("enter the number: "))
temp = n
sum = 0
while n > 0:
    digit = n%10
    sum = sum + digit ** 3
    n//=10
if(sum == temp):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
    
    
