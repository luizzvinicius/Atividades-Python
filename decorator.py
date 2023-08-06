'''Exemplo 1'''


# def validar(f):
#     def valida(x, y):
#         if x < 0 or y < 0:
#             raise ValueError("Valores negativos são bloqueados")
#         return f(x, y)
#     return valida


# @validar
# def soma(x, y):
#     return x + y


# s = soma(8, -7)
# print(s)


'''Exemplo 2'''
# import timeit

# def time_execution(f):
#     def wrapper(array):
#         st = timeit.default_timer()
#         soma = f(array)
#         end = timeit.default_timer() - st
#         print(f"time spent: {end}")
#         return soma
#     return wrapper

# @time_execution
# def sum_array(array):
#     return sum(array)

# a = [i for i in range(1, 11)]
# salary = sum_array(a)
# print(salary)

'''Exemplo 3'''
# import re
# def val_placa(f):
#     '''Valida se a placa do carro obedece o padrão normal ou mercosul'''
#     def valida():
#         while True:
#             p = f()
#             if re.match(r"^[A-Za-z]{3}\d{1}[A-Za-z0-9]{1}\d{2}$", p):
#                 return p
#             print("Placa inválida.\n")
#     return valida


# @val_placa
# def read_placa():
#     placa = input("Qual a placa do(a) veículo: ").strip().upper()
#     return placa


# car = read_placa()
# print(car)
