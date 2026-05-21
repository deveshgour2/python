num = int(input("enter the  number of terms: "))

a = 0
b = 1
print("fibonacci series : ")

for i in range(num):
    print(a, end=" ")
    c=a+b
    a=b
    b=c

