'''
Dupla: Heitor Moreira Costa
       Luiz Vinícius Márdelle Costa Silva
'''
# Questão 4

comidas = ["Cachorro quente", "Bauru simples", "Bauru com ovo", "Hambúrger", "Cheeseburguer", "Refrigerante"]
codigos = [100, 101, 102, 103, 104, 105]
precos = [1.2, 1.3, 1.5, 1.2, 1.3, 1.0]
pedido = []

while True:
    print("[ 1 ] Cardápio")
    print("[ 2 ] Pagamento")
    print("[ 3 ] Sair")
    opt = int(input("Sua opção: "))
    print()
    if opt == 1:
        print("Especificação".ljust(20), end="")
        print("Código".center(20), end="")
        print("Preço".center(20), end="")
        print()

        for comida, codigo, preco in zip(comidas, codigos, precos):
            print(comida.ljust(20), end="")
            print(str(codigo).center(20), end="")
            print(str(preco).center(20), end="")
            print()

        while True:
            while True:
                codigo = int(input("Digite o código do produto: "))
                quantidade = int(input("Quantidade do produto: "))
                if codigo in codigos:
                    break
                print("Código inválido.\n")
                continue

            for k in range(quantidade):
                codigo = codigo % 100
                pedido.append(comidas[codigo])
                pedido.append(precos[codigo])

            deseja = input(
                ("Deseja mais alguma coisa? [S/N] ")).strip()[0].upper()
            if deseja == "S":
                continue
            break
    if opt == 2:
        total = 0
        for i in pedido:
            if isinstance(i, float):
                total += i
        print(f"Total da conta R${total :.2f}")

    if opt == 3:
        break
