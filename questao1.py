'''
Dupla: Heitor Moreira Costa
       Luiz Vinícius Márdelle Costa Silva
'''
# Questão 1

qtd_pessoas = int(input("Quantas pessoas para calcular o IMC? "))
imcs = []
abaixo = ideal = acima = muitoAcima = obeso = 0

for i in range(1, qtd_pessoas+1):
    sexo = input(f"Qual o sexo da pessoa {i} [M/F]: ").strip()[0].upper()
    altura = float(input(f"Qual a altura da pessoa {i} [Em m]? "))
    peso = float(input(f"Qual o peso da pessoa {i}? "))
    print()

    imc = peso / (altura ** 2)
    imcs.append(imc)
    
    # Não é necessário usar dois operadores lógicos
    if sexo == 'F':
        if imc < 19.1:
            abaixo += 1
        elif imc < 25.8:
            ideal += 1
        elif imc < 27.3:
            acima += 1
        elif imc < 31.1:
            muitoAcima += 1
        elif imc >= 31.1:
            obeso += 1
    if sexo == 'M':
        if imc < 20.7:
            abaixo += 1
        elif imc < 26.4:
            ideal += 1
        elif imc < 27.8:
            acima += 1
        elif imc < 32.3:
            muitoAcima += 1
        elif imc >= 32.3:
            obeso += 1

print(imcs)
print(f"Abaixo do peso: {abaixo}")
print(f"Peso ideal: {ideal}")
print(f"Um pouco acima do peso: {acima}")
print(f"Acima do peso ideal: {muitoAcima}")
print(f"Obeso: {obeso}")