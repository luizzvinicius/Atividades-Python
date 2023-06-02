import random

info = {}
for i in range(1, 5):
    info.setdefault(f"jogador{i}", random.randint(1, 6))

for i in sorted(info, key=info.get, reverse=True):
    print(i, info[i])
