import time, random
fibonacci = [0,1]
print(f"{fibonacci[0]}\n{fibonacci[1]}")

while True:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    time.sleep(random.uniform(0.01, 1.0)), print(number)
