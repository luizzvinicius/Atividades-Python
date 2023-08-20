# Questão 1º (Igual a figura)
# for i in range(1, 10):
#     for j in range(1, 11):
#         print(f"{j} x {i} = {i * j}".ljust(10), end="    ")
#         j += 1
#     print()

# Questão 2
# qtd_alunos = int(input("Quantos alunos há na turma? "))
# medias = []
# aprovados = 0
# for r in range(qtd_alunos):
#     soma_media = 0
#     print(f"Aluno {r+1}")
#     for m in range(1, 5):
#         nota = float(input(f"Digite sua nota no {m}º Bimestre: "))
#         soma_media += nota

#     if soma_media >= 6:
#         aprovados += 1
#     medias.append(soma_media / 4)
#     print()

# print(f"Maior média: {max(medias)}")
# print(f"Menor média: {min(medias)}")
# print(f"Alunos aprovados: {aprovados}\nAlunos reprovados: {qtd_alunos - aprovados}")

# Questão 3
# while True:
#     num = int(input("Digite um número (negativo para parar): "))
#     if num < 0:
#         break

#     divided = 0
#     if num == 1:
#         divided += 1

#     for i in range(2, num): # Não funciona se o número digitado for 1, por isso o IF anterior
#         if num % i == 0:
#             divided += 1
#             break

#     print("Primo" if divided == 0 else "Não primo")

# Questão 5
apartamentos = set()
elevadorA = elevadorB = elevadorC = 0
periodoM = periodoV = periodoN = 0
while len(apartamentos) < 17:
    num_apto = int(input("Digite o número do seu apartamento (1 a 16): "))
    if num_apto in apartamentos or num_apto not in range(1, 17):
        print("Apartamento inválido ou já respondeu a pesquisa.\n")
        continue
    apartamentos.add(num_apto)

    while True:
        elevador = input('Qual elevador você utiliza com mais frequência: ("A", "B", "C")? ').strip()[0].upper()
        if elevador in ("A", "B", "C"):
            break
        print("Elevador inválido.\n")

    while True:
        periodo = input('Qual período você utiliza o elevador com mais frequência: ("M", "V", "N")? ').strip()[0].upper()
        if periodo in ("M", "V", "N"):
            break
        print("Período inválido.\n")

    if elevador == "A":
        elevadorA += 1
    elif elevador == "B":
        elevadorB += 1
    elif elevador == "C":
        elevadorC += 1

    if periodo == "M":
        periodoM += 1
    elif periodo == "V":
        periodoV += 1
    elif periodo == "N":
        periodoN += 1
    print()

max_elevador = max(elevadorA, elevadorB, elevadorC)
elevador_movimentado = ""
if elevadorA == max_elevador:
    elevador_movimentado += "A "
if elevadorB == max_elevador:
    elevador_movimentado += "B "
if elevadorC == max_elevador:
    elevador_movimentado += "C"

max_periodo = max(periodoM, periodoV, periodoN)
periodo_movimentado = ""
if periodoM == max_periodo:
    periodo_movimentado += "Matutino "
if periodoV == max_periodo:
    periodo_movimentado += "Vespertino "
if periodoN == max_periodo:
    periodo_movimentado += "Noturno"

print(f"Elevador mais movimentado: {elevador_movimentado}")
print(f"Período mais movimentado: {periodo_movimentado}")
percentual_mais_usado = max_elevador / (elevadorA + elevadorB + elevadorC) * 100
percentual_menos_usado = min(elevadorA, elevadorB,elevadorC) / (elevadorA + elevadorB + elevadorC) * 100
print(f"Diferença % do elevador mais usado para o menos usado: {percentual_mais_usado - percentual_menos_usado :.2f}%")
