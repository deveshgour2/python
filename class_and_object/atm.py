class atm:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin

    def check_pin(self, entered_pin):
        return self.pin == entered_pin
    
    def deposit(self, amount):
        self.balance  += amount
        print(f"deposited successfully: {self.balance}")

    def withdraw(self, amount):
        if(self.balance > amount):
            self.balance -= amount
            print("withdraw successfully: ", amount)
        else:
            print("insufficient balance")

a = atm(10000, 1234) 

if(a.check_pin(1234)):
    a.deposit(2000)
    a.withdraw(6000)

print("balance= ", a.balance )

