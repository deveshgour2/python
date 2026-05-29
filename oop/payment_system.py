class payment:
    def pay(self, amount):
        self.amount = amount

class upi_payment(payment):
    def pay(self, amount):
        print(f"paid {amount} using upi ")

class creditcard_payment(payment):
    def pay(self, amount):
        print(f"paid {amount} using credit card")

class cash_payment(payment):
    def pay(self, amount):
        print(f"paid {amount} using cash")

payments = [ upi_payment(), creditcard_payment(), cash_payment()]

for p in payments:
    p.pay(2000)
