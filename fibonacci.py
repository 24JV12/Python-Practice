import os

def clear(): os.system("cls" if os.name == "nt" else "clear")

clear()

while True:
    fib, cmd, exe = [0, 1], input(r".\Fibonacci> "), False
    if cmd.isdigit():
        rng = int(cmd)
        for _ in range(rng): fib.append(fib[-1] + fib[-2])
        exe = True
    elif cmd.lower() in ["cls", "clean", "clear"]: clear()
    elif cmd.lower() == "exit": exit()   
    if exe:
        try: print(fib[rng] if len(fib) > 2 else fib[rng])
        except IndexError and ValueError: print("Error!")
