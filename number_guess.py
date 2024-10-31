from random import randint

try: number = randint(int(input("Initial: ")), int(input("Final: ")))
except ValueError: print("Error!"); exit()

while True:
    try: 
        total_guesses = int(input("How many chances? [1, 25]: "))
        if 1 <= total_guesses <= 25: break
    except ValueError: print("Error!")

for guesses in range(1, total_guesses + 1):
    try: guess = int(input(f"Guess {guesses}: "))
    except: print("Error!"); exit()
    if guess == 0: print(f"Number: {number}"); break
    elif guess == number: print("You Won!"); break
    elif guess > number: print("Try something less than that")
    else: print("Try with something more than that")

else: print("You Lost!")
