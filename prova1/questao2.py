'''
Dupla: Heitor Moreira Costa
       Luiz Vinícius Márdelle Costa Silva
'''
# Questão 2

nomes = []
notas = []

while len(nomes) < 10:
    nome = input("Nome do aluno: ")
    if nome in nomes:
        print("Nome já está na lista\n")
        continue

    nota = int(input("Nota do aluno: "))
    if nota < 0 or nota > 10:
        print("Nota inválida\n")
        continue

    nomes.append(nome)
    notas.append(nota)
    print()

while True:
    print("1. Informar o aluno que teve a maior nota, e o aluno com a menor nota.")
    print("2. Informar a média geral da turma.")
    print("3. Sair.")
    opt = int(input("Sua opção: "))
    if opt == 1:
        menor = notas[0]
        maior = notas[0]
        nome_menor_aluno = nomes[0]
        nome_maior_aluno = nomes[0]
        for nota, nome in zip(notas, nomes):
            if nota < menor:
                menor = nota
                nome_menor_aluno = nome
            if nota > maior:
                maior = nota
                nome_maior_aluno = nome
        print(f"Nome e nota do aluno com a maior média: {nome_maior_aluno} {maior}")
        print(f"Nome e nota do aluno com a menor média: {nome_menor_aluno} {menor}")
    if opt == 2:
        soma = 0
        for i in notas:
            soma += i
        media = soma / len(notas)
        print(f"A média da turma é: {media}")

        if media < 6:
            print("Situação ruim.")
        elif media <= 7:
            print("Situação regular.")
        elif media < 8.9:
            print('Situação boa.')
        elif media >= 9:
            print("Situação exelente.")
    if opt == 3:
        break
