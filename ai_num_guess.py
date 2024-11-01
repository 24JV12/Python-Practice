from random import randint
import time, os

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    try: number, total_guesses = randint(-100, 100), int(input(r".\totalGuesses> ") or 5)
    except ValueError: print("Non Integer Value Detected!"); break
    low, high = -500, 500

    for guess_num in range(1, total_guesses + 1):
        guess = randint(low, high); print(f"Guess {guess_num}: {guess} {'Won!' if guess == number else ''}")
        if guess == number: break
        elif guess > number: high = guess - 1; print("less than that\n")
        else: low = guess + 1; print("more than that\n")
        time.sleep(1)
    else: print("Lost!")
    
    if input("Again? (Y/n) ").lower() == 'n': break
