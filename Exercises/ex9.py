import random

aim = random.randint(1,9)
guess = 0
counter = 0

def check_guess(aim, guess):
    if guess < aim:
        print("Guess too low")
    elif guess > aim:
        print("Guess too high")
    else:
        print("Congratulations. You guessed right in",counter,"tries")

while aim != guess:
    guess = input("Enter your guess: ")
    if guess == "exit":
        break
    guess = int(guess)
    counter += 1
    check_guess(aim, guess)




