import random
num = random.randint(1, 10)# select random between 1 and 10 inclusive


guess = int(input("Guess an integer between 1 and 10: "))
if guess == num:
    print("you guessed right")
else:
    print("you guessed wrong")
print(num)