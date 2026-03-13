# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least on one of them."
test_score1 = int(input("what is your test score?"))
test_score2 = int(input("what is your test score?"))
if test_score1 >50 and test_score2 >50:
    print("you passed both!")
else:
    print("you at least failed one of them.")
# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
brought_lunch = input("did you bring lunch?yes/no")
brought_water = input("did you bring water?yes/no")
if brought_lunch == "yes" or brought_water == "yes":
    print("you are somewhat ready.")
if brought_water == "yes" and brought_lunch == "yes":
    print("you're fully ready!")
if brought_water == "no" and brought_lunch == "no":
    print("you're not ready.")
# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
user_input = int(input("give me a number"))
if user_input > 10 or user_input < 1:
    print("out of range.")
else:
    print("in range.")
# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
user_input = int(input("guess a random number between 1 and 10."))
import random
num = random.randint(1, 10)# select random between 1 and 10 inclusive
if user_input == num and num % 2 == 0:
    print("even match")
elif user_input == num or num == 5:
    print("nice try.")
else:
    print("nope")
# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
user_input = int(input("give me a number."))
user_inputs = int(input("give me a number."))
if user_input % 5 == 0 and user_inputs % 2 != 0:
    print("intresting pair!")
else:
    print("plain pair.")