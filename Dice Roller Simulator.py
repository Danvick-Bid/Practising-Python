import random
def roll_dice():
    sides = int(input("Enter the number of sides on your dice: "))
    print(f"You rolled a {random.randint(1, sides)}")

roll_dice()