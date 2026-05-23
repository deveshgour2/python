n = int(input("enter the number: "))
temp = n 
rev = 0
while n>0:
    digit = n % 10
    rev = rev * 10 + digit
    n//10

if(temp == n):
    print("Number is pallindrome")
else:
    print("Number is not Pallindrome")