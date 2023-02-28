import random

while True:
    try:
        n = int(input("Level : "))
    except ValueError:
        continue
    else:
        break

computer_guess = random.randint(1,n)

while True:
    guess = int(input("Guess : "))
    if guess == computer_guess:
        print("Just right!")
        break
    if guess > computer_guess:
        print("Too Large!")
    if guess < computer_guess:
        print("Too Small!")
