import uteis

matriz = []
for i in range(0, 3):
    linha = []
    for j in range(0, 3):
        n = uteis.lerInteiro(f"Digite o valor da posição [{i}][{j}]: ")
        linha.append(n)
    matriz.append(linha)
print()

soma, sum3Column, max2Line = 0, 0, 0
for j, m in enumerate(matriz):
    if j == 1:
        max2Line = max(m)
    for i, v in enumerate(m):
        if v % 2 == 0:
            soma += v
        if i == 2:
            sum3Column += v
        print(f"{str(v) :^3}", end=" ")
    print()

print(f"Soma dos pares: {soma}")
print(f"Soma da 3 coluna: {sum3Column}")
print(f"Maior valor da segunda linha: {max2Line}")
