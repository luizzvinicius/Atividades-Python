'''Módulo com funções de leitura do teclado'''


def read_string(msg, exept_msg="Inválido"):
    '''Função que lê uma string e a retorna já sem os espaços em branco.'''
    while True:
        palavra = input(msg).strip()
        if palavra.isidentifier():
            return palavra
        print(exept_msg + "\n")


def read_int(msg, exept_msg="Inválido"):
    '''Função que lê um inteiro e o retorna.'''
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print(exept_msg + "\n")


def read_float(msg, exept_msg="Inválido"):
    '''Função que lê um inteiro e o retorna.'''
    while True:
        try:
            num = float(input(msg))
            return num
        except ValueError:
            print(exept_msg + "\n")


def read_option(msg, max_opt, exept_msg="Opção inválida."):
    '''Função que lê opções, dado o parâmetro max_opt, e a retorna.'''
    while True:
        opt = read_int(msg, "Digite números")
        if 0 < opt <= max_opt:
            return opt
        print(f"\033[31m{exept_msg}\033[m\n")


def fileExists(name):
    try:
        with open(name, "r", encoding="utf-8"):
            return True
    except (FileNotFoundError, IOError):
        return False
    
"""
Archives Manipulations Modes
'r' open for reading (default)
'w' open for writing, truncating the file first
'x' open for exclusive creation, failing if the file already exists
'a' open for writing, appending to the end of file if it exists
'b' binary mode
't' text mode (default)
'+' open for updating (reading and writing)
"""