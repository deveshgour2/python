class book:
    def __init__(self, book, price):
        self.book = book
        self.price = price
    
b1 = book("python", 900)
b2 = book("java", 600)
b3 = book("c++", 400)

print(f" book 1 = {b1.book} {b1.price}")
print(f" book 2 = {b2.book} {b2.price}")
print(f" book 3 = {b3.book} {b3.price}")

if (b1.price > b2.price and b1.price > b3.price):
    print("book 1 is expensive", b1.price)

elif (b2.price > b1.price and b2.price > b3.price):
    print("book 2 is expensive", b2.price)

else:
    print("book 3 is expensive")