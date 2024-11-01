import os, random, time

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def randomize(jar, parts, interval, cls, remaining_choices):
    if not jar: print("No choices to pick from!"); return
    removals, executed = len(jar) - remaining_choices, False; clear()
    if removals > 0 and remaining_choices != 0:
        for _ in range(removals):
            unfaithful = random.choice(jar); jar.remove(unfaithful)
            if not cls: print(f"'{unfaithful}' is out of the game!"); time.sleep(interval)
        executed = True
    if cls: clear()
    if jar and executed: print(f"Final choices are: {', '.join(jar)}" if len(parts) == 3 else f"Final choice is: {jar[0]}")
    if not executed: print("Error!")

def coin_flip(): time.sleep(1.5); print(random.choice(["Heads", "Tails"]))

clear()
while True:
    jar = []
    while True:
        cmd = input(f"Choice {len(jar) + 1}: ").strip()
        if cmd.lower().startswith("done"):
            parts = cmd.split()
            randomize(jar, parts, float(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0,
            len(parts) == 1, int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 1); break
        elif cmd.lower() in ["coin", "flip", "toss"]: coin_flip()
        elif cmd.lower() in ["cls", "clean", "clear"]: clear()
        elif cmd.lower() == "exit": exit()
        else: jar.append(cmd)
