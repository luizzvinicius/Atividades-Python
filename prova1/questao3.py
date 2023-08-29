'''
Dupla: Heitor Moreira Costa
       Luiz Vinícius Márdelle Costa Silva
'''
# Questão 3
primos = []
nPrimos = []

while True:
    num = int(input("Digite o número: "))
    if num < 0:
        break

    divided = 0
    if num in (0, 1):
        divided += 1

    for i in range(2, num):
        if num % i == 0:
            divided += 1
            break

    if divided == 0:
        primos.append(num)
    else:
        nPrimos.append(num)

print(f"Total de números digitados: {len(primos) + len(nPrimos)}")
for i, value in enumerate(primos):
    if value in (0, 1):
        primos.pop(i)

print(f"Total de primos: {len(primos)}")
print(f"Números primos: {primos}")
print(f"Números não primos: {nPrimos}")
