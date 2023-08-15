# Questão 1º (Igual a figura)
for i in range(1, 10):
    for j in range(1, 11):
        print(f"{j} x {i} = {i * j}".ljust(10), end="    ")
        j += 1
    print()

# Questão 2
qtd_alunos = int(input("Quantos alunos há na turma? "))
medias = []
aprovados = 0
for r in range(qtd_alunos):
    soma_media = 0
    print(f"Aluno {r+1}")
    for m in range(1, 5):
        nota = float(input(f"Digite sua nota no {m}º Bimestre: "))
        soma_media += nota

    if soma_media >= 6:
        aprovados += 1
    medias.append(soma_media / 4)
    print()

print(f"Maior média: {max(medias)}")
print(f"Menor média: {min(medias)}")
print(f"Alunos aprovados: {aprovados}\nAlunos reprovados: {qtd_alunos - aprovados}")

# Questão 3
while True:
    num = int(input("Digite um número (negativo para parar): "))
    if num < 0:
        break

    divided = 0
    if num == 1:
        divided += 1

    for i in range(2, num): # Não funciona se o número digitado for 1, por isso o IF anterior
        if num % i == 0:
            divided += 1
            break

    print("Primo" if divided == 0 else "Não primo")
