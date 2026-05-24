n = int(input("enter a terms: "))

def fibonacci(n):
    a = 0 
    b = 1
    temp = 0
    for i in range(n):
        print(a, end=" ")
        temp = a
        a = b
        b = temp + b
fibonacci(n)
    
    