import uteis

dados = []

continuar = "S"
while continuar == "S":
    pessoa = {
        "nome": uteis.lerString("Digite seu nome: ", "Nome inválido"),
        "idade": uteis.lerInteiro("Idade: "),
        "sexo": uteis.lerString("Digite seu sexo: ")
    }
    dados.append(pessoa)
    continuar = uteis.lerString("\nQuer continuar? ")
    print()


def media(lista):
    return sum(i["idade"] for i in lista) / len(lista)


def women(lista):
    l2 = []
    for i in lista:
        if i["sexo"] == "F":
            l2.append(i["nome"])
    return l2


def greaterMean(lista):
    l2 = []
    media2 = media(lista)
    for i in lista:
        if i["idade"] > media2:
            l2.append(i)
    return l2


print(f"Pessoas cadastradas: {len(dados)}")
print(f"Média de idade: {media(dados) :.1f}")
print(f"Mulheres na lista: {women(dados)}")
print(f"Pessoas acima da média: {greaterMean(dados)}")
