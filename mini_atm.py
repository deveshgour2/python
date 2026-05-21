balance = 10000

while True:
    print("\n=====mini atm=====")
    print("press 1 for check balance")
    print("press 2 for deposit")
    print("press 3 for withdraw")
    print("press 4 for exit")
    
    choice = int(input("enter your choice: "))

    if choice == 1:
        print("current balance = Rs", balance)

    elif choice== 2:
        deposit = int(input("enter amount to deposit: "))
        balance = balance + deposit
        print("amount deposited successfully")
        print("updated balance = Rs" , balance)

    elif choice == 3:
        withdraw = int(input("enter amount  to withdraw: " ))
        if balance >= withdraw:     
            balance = balance - withdraw
            print("collect your cash")
            print("remaining balance = Rs", balance)
        else:
            print("insufficient balance")   

    elif choice == 4:
        print("thank you for using ATM")
     
    else:
        print("Invalid choice: Please try again")
