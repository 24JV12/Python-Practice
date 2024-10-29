import os, random, time
def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def randomize(jar, interval, cls):
    clear()
    removals = len(jar) - 1
    for _ in range(removals):
        unfaithful = random.choice(jar)
        jar.remove(unfaithful)
        if not cls: print(f"'{unfaithful}' is out of the game!"), time.sleep(interval)
    if cls: clear()
    if jar: print(f"And the random choice is '{jar[0]}'")

clear()
while True:
    jar = []
    while True:
        cmd = input(f"Choice {len(jar) + 1}: ").strip()
        if cmd.lower().startswith("done"):
            parts = cmd.split()
            if len(parts) == 2 and parts[-1].isdigit(): interval, cls = int(parts[1]), False
            else: interval, cls = 0, True
            randomize(jar, interval, cls)
            break
        elif cmd in ["cls", "clean", "clear"]: clear()
        elif cmd == "exit": exit()
        else: jar.append(cmd)
