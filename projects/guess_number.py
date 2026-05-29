import random
num = random.randint(1, 100)
user = -1
guess = 1
while (num != user):
    user = int(input(" enter the number: "))

    if(num > user):
        print("large number")
        guess +=1

    elif(num < user ):
        print("small number ")
        guess += 1
    
    else:
        print("correct guess")

print(f"you guesses {num} in {guess} attempts")