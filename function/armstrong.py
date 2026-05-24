n = int(input(" enter a number: "))

def Armstrong(n):
    temp = n
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit ** 3
        n //= 10

    return temp == total
    
print(Armstrong(n))