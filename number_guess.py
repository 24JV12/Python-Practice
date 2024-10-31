from random import randint

number = randint(int(input("Initial: ")), int(input("Final: ")))

while True:
    total_guesses = int(input("How many chances? [1, 25]: "))
    if 1 < total_guesses < 25: break
    print("Error Detected!")

for guesses in range(1, total_guesses + 1):
    guess = int(input(f"Guess {guesses}: "))
    if guess == 0: print(f"Number: {number}"); break
    elif guess == number: print("You Won!"); break
    elif guess > number: print("Try something less than that")
    else: print("Try with something more than that")

else: print("You Lost!")
