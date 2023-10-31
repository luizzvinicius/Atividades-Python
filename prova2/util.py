'''Módulo com funções de leitura do teclado'''


def read_string(msg, exept_msg="Inválido"):
    '''Função que lê uma string e a retorna já sem os espaços em branco.'''
    while True:
        palavra = input(msg).strip().lower()
        if palavra.isidentifier():
            return palavra
        print(f"{exept_msg}\n")


def read_int(msg, exept_msg="Inválido"):
    '''Função que lê um inteiro e o retorna.'''
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print(f"{exept_msg}\n")


def read_option(msg, min_opt, max_opt, exept_msg="Opção inválida."):
    '''Função que lê opções, dado o parâmetro min_opt e max_opt, e a retorna.'''
    while True:
        opt = read_int(msg, "Digite números")
        if min_opt <= opt <= max_opt:
            return opt
        print(f"{exept_msg}\n")


def show_options(array):
    for i, funcao in enumerate(array, start=1):
        print(f"[ {i} ] {funcao}")
