n = int(input("enter the number of  terms: "))
a = 0 
b = 1
temo = 0
print("fibbonacci series: ")
for i in range(n):
    print(a, end=" ")
    temp = a
    a = b 
    b = temp + b

