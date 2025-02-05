import random
def number_guessing_game():
    number = random.randint(1, 100)
    guess = None
    tries = 0

    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        tries += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! It took you {tries} tries.")

number_guessing_game()