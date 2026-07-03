import random

def roll_dice(num_dice, sides):
    rolls = []
    for _ in range(num_dice):
        rolls.append(random.randint(1, sides))
    return rolls

while True:
    try:
        num_dice = int(input("How many dice do you want to roll? "))
        sides = int(input("How many sides per die? "))
        if num_dice <= 0 or sides <= 1:
            print("Enter positive values (sides must be at least 2).")
            continue

        results = roll_dice(num_dice, sides)

        print("\nRolls:", results)
        print("Total:", sum(results))
        print("Highest:", max(results))
        print("Lowest:", min(results))

        again = input("\nRoll again? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break

    except ValueError:
        print("please enter the value ")