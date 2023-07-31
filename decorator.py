def validar(f):
    def valida(x, y):
        if x < 0 or y < 0:
            raise ValueError("Valores negativos são bloqueados")
        return f(x, y)
    return valida


@validar
def soma(x, y):
    return x + y

print(soma(9, 1))

dobro = validar(soma(8, 7))
