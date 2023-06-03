import uteis

jogadores = []

continuar = "S"
while continuar == "S":
    nome = uteis.lerString("Nome do jogador: ")
    qtdPartidas = uteis.lerInteiro(f"Quantas partidas {nome} jogou? ")

    gols = []
    for i in range(qtdPartidas):
        gol = uteis.lerInteiro(f"\tQuantos gols na {i+1}º partida? ")
        gols.append(gol)

    jogadores.append({"nome": nome, "gols": gols})

    continuar = uteis.lerString("Quer continuar (S/N): ")
    print()
print("-=" * 30)

print(f"{'Cod' :<4}", end="")
print(f"{'Nome' :<25}", end="")
print(f"{'Gols' :<25}", end="")
print(f"{'Total' :<5}")

print("-" * 60)
for i, v in enumerate(jogadores, start=1):
    print(f"{i :<4}", end="")
    print(str(v['nome']).ljust(25), end="")
    print(str(v['gols']).ljust(25), end="")
    print(str(sum(v['gols'])))
print("-" * 60)

while True:
    opt = uteis.lerOption(f"Mostrar dados de qual jogador? ({len(jogadores) + 1} para parar) ", max=len(jogadores)+1)-1
    if opt+1 == len(jogadores)+1:
        break
    print(f"--Levantamento do jogador {jogadores[opt]['nome']}")
    c = 1
    for i in jogadores[opt]['gols']:
        print(f"\tNo jogo {c} fez {i} gols")
        c += 1
    print("-" * 60)
