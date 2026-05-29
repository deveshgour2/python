import  random
computer = random.choice([1, 0, -1])

youstr = (input(" enter your choice: "))

youDict = { "r" : 1 , "p": 0 , "s": -1}
reverse_Dict = {1 : "rock", 0 : "paper", -1 : "scissor"}

user = youDict[youstr]

print(f"you choose {reverse_Dict[user]} \n computer choose {reverse_Dict[computer]}" )
if(user == computer ):
    print(" draw ")

elif(computer == 1 and user == 0 ):
    print("you win")

elif(computer == 0 and user == -1):
    print("you win")

elif(computer == -1 and user == 1):
    print("you win ")


elif(user == 1 and computer == 0):
    print("you lose")

elif(user == 0 and computer == -1):
    print("you lose")

elif(user == -1 and computer == 1):
    print("you lose")

else:
    print("something went wrong")
