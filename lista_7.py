from random import randint
from utils import reader

# questão 1
def celsiusKelvin(temp):
    print(f"Temperatura em Kelvin é: {temp + 273.15 :.2f}\n")


def kelvincelsius(temp):
    while temp < 273.15:
        print("Temperatura inválida")
        temp = reader.read_float("Digite a nova temperatura: ")
    print(f"Temperatura em Celsius é: {temp - 273.15 :.2f}\n")


def celsiusFahrenheit(temp):
    print(f"Temperatura em Celsius é: {(temp * 9/5) + 32 :.2f}\n")


def fahrenheitcelsius(temp):
    print(f"Temperatura em Celsius é: {(temp - 32) * 5/9 :.2f}\n")


print("Conversor de temperaturas")
funcoes = ["Celsius para Kelvin", "Kelvin para Celsius", "Celsius para Fahrenheit", "Fahrenheit para Celsius", "Sair"]
while True:
    for i, msg in enumerate(funcoes, start=1):
        print(f"[ {i} ] {msg}")
    opt = reader.read_option("Sua opção: ", 5, "Opção inválida") - 1
    if opt == 4: break

    temp = reader.read_float(f"Digite a temperatura em {funcoes[opt].split(' ')[0]}: ")
    if opt == 0:
        celsiusKelvin(temp)
    elif opt == 1:
        kelvincelsius(temp)
    elif opt == 2:
        celsiusFahrenheit(temp)
    elif opt == 3:
        fahrenheitcelsius(temp)
print("Programa encerrado")

# questão 2
print("Terminal bancário")
saldo = 0
transacoes = []

def ver_saldo():
    print(f"Seu saldo é: {saldo}")

def depositar(valor):
    while valor <= 0:
        print("Quantia inválida para depósito")
        valor = reader.read_float("Digite a quantia a ser depositada: ", "Quantia inválida")
    global saldo
    saldo += valor
    print(f"Quantia de {valor} foi depositada com sucesso")
    transacoes.append(valor)

def sacar(valor):
    global saldo
    while valor <= 0 or valor > saldo:
        if saldo == 0:
            print("Conta sem saldo")
            return
        print("Quantia inválida para saque")
        valor = reader.read_float("Digite a quantia a ser sacada: ", "Quantia inválida")
    saldo -= valor
    print(f"Quantia de {valor} foi sacada com sucesso")
    transacoes.append(-valor)

def extrato():
    for i, valores in enumerate(transacoes, start=1):
        operacao = "depósito" if valores > 0 else "saque"
        print(f"{i}. Ocorreu um {operacao} no valor de {valores}")

funcoes = ["Ver saldo", "Depositar", "Sacar", "Ver extrato", "Sair"]
while True:
    for i, msg in enumerate(funcoes, start=1):
        print(f"[ {i} ] {msg}")
    opt = reader.read_option("Sua opção: ", 5, "Opção inválida") - 1

    if opt == 0:
        ver_saldo()
    elif opt == 1:
        valor = reader.read_float("Digite o valor de depósito: ")
        depositar(valor)
    elif opt == 2:
        valor = reader.read_float("Digite o valor do saque: ")
        sacar(valor)
    elif opt == 3:
        extrato()
    elif opt == 4:
        break
print("Programa encerrado")

# questão 3
def valida_chute(num, qtd_chutes):
    chutes = []
    tentativas = 1
    while tentativas <= qtd_chutes:
        chute = reader.read_int("Digite seu chute: ", "Digite um número")
        if not (0 < chute <= 100):
            print("Chute fora do intervalo de 1 a 100")
            continue
        if chute in chutes:
            print("Chute já informado")
        elif chute < num:
            print("Chute menor que o número")
            tentativas += 1
        elif chute > num:
            print("Chute maior que o número")
            tentativas += 1
        elif chute == num:
            print(f"Você acertou em {tentativas} tentativas")
            return
        chutes.append(chute)
    print("Você não acertou o número secreto")

funcoes = ["Sete chutes", "Cinco chutes", "Três chutes", "Sair"]
while True:
    for i, msg in enumerate(funcoes, start=1):
        print(f"[ {i} ] {msg}")

    opt = reader.read_option("Sua opção: ", len(funcoes), "Opção inválida") - 1
    if opt == 3: break

    num_gerado = randint(1, 100)
    print(num_gerado)
    if opt == 0:
        valida_chute(num_gerado, 7)
    elif opt == 1:
        valida_chute(num_gerado, 5)
    elif opt == 2:
        valida_chute(num_gerado, 3)
print("Programa encerrado")
