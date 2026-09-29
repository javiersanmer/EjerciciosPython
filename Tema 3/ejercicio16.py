import random
lanza = []

for _ in range(10):
    n = random.randint(0,1)
    if n == 0:
        lanza.append("Cara")
    else:
        lanza.append("Cruz")
print(lanza)