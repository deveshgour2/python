n = input(" enter a string : ")
def pallindrome(n):
    if (n == n[:: -1]):
        print("Pallindrome")
    else:
        print(" not Pallindrome")
pallindrome(n)