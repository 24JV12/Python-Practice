import os, random, time

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def randomize(jar, interval, cls):
    if not jar: print("No choices to pick from!"); return
    clear(); removals = len(jar) - 1
    for _ in range(removals):
        unfaithful = random.choice(jar); jar.remove(unfaithful)
        if not cls: print(f"'{unfaithful}' is out of the game!"),time.sleep(interval)
    if cls: clear()
    if jar: print(f"And the random choice is '{jar[0]}'")

def coin_flip(): time.sleep(1.5), print(random.choice(["Heads", "Tails"]))
clear()
while True:
    jar = []
    while True:
        cmd = input(f"Choice {len(jar) + 1}: ").strip()
        if cmd.lower().startswith("done"):
            parts = cmd.split()
            interval, cls = int(parts[1]) if len(parts) == 2 and parts[-1].isdigit() else 0, len(parts) == 1
            randomize(jar, interval, cls); break
        elif cmd.lower() in ["coin", "flip", "toss"]: coin_flip()
        elif cmd.lower() in ["cls", "clean", "clear"]: clear()
        elif cmd.lower() == "exit": exit()
        else: jar.append(cmd)
