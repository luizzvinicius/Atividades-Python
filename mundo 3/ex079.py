a = []

for i in range(3):
    n = int(input("Digite um número: "))
    a.append(n)

u = list(set(a))

print(sorted(u))
