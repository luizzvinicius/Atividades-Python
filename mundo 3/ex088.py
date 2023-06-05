import uteis; import random

palpites = uteis.lerInteiro("Quantos palpites? ")
jogos = []
for k in range(palpites):
    jogo = []
    while len(jogo) < 6:
        n = random.randint(1, 60)
        if n not in jogo:
            jogo.append(n)
    jogos.append(jogo)

for j, v in enumerate(jogos, start=1):
    print(f"{j}º jogo é: {sorted(v)}")
