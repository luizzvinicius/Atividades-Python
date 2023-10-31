# Nome: Luiz Vinícius Márdelle Costa Silva
from datetime import date
import util

funcoes = ["Adicionar livro", "Consultar livro", "Adicionar leitura do momento", "Remover leitura momento", "Sair"]
livros, livros_momento = [], []
generos = ["Autobiografia", "Biografia", "Conto", "Poesia", "Romance", "Autoajuda"]

def adicionar_livro(titulo, ano_lancamento, autor, genero):
    global livros
    livros.append([titulo, ano_lancamento, autor, genero])
    print(f"{titulo} adicionado com sucesso\n")


def consultar_por_titulo(titulo):
    global livros
    livro_mesmo_titulo = []
    for livro in livros:
        if titulo in livro[0]:
            livro_mesmo_titulo.append(livro)
    return livro_mesmo_titulo


def consultar_por_genero(genero):
    global livros
    livro_mesmo_genero = []
    for livro in livros:
        if livro[3] == genero:
            livro_mesmo_genero.append(livro)
    return livro_mesmo_genero


def adicionar_livro_para_leitura(titulo):
    global livros_momento
    livros_momento.append(titulo)
    print(f"{titulo} adicionado em leitura do momento\n")


def livro_ja_cadastrado(titulo, momento=False):
    global livros, livros_momento
    if momento:
        for v in livros_momento:
            if v == titulo:
                print("Livro já adicionado\n")
                return True
    else:
        for i, v in enumerate(livros):
            if livros[i][0] == titulo:
                print("Livro já adicionado\n")
                return True


def possui_livros(biblioteca):
    if len(biblioteca) == 0:
        print("Nenhum livro cadastrado\n")
    return len(biblioteca) > 0


def remover_livro(titulo):
    global livros_momento
    try:
        livros_momento.remove(titulo)
        print(f"{titulo} removido\n")
    except ValueError:
        print(f"{titulo} não encontrado\n")


while True:
    util.show_options(funcoes)
    opt = util.read_option("Digite a opção: ", 1, len(funcoes)) - 1
    if opt == len(funcoes) - 1:
        print("Programa encerrado.")
        break
    if opt == 0:
        titulo = util.read_string("Digite o título do livro: ", "Digite apenas letras (sem espaços) para o título do livro")
        if livro_ja_cadastrado(titulo): continue
        ano_lancamento = util.read_option("Digite o ano de lançamento: ", 1900, date.today().year, f"Ano deve ser após 1900 e antes de {date.today().year}")
        autor = util.read_string(f"Digite o nome do autor de {titulo}: ", "Digite apenas letras (sem espaços) para o autor do livro")
        util.show_options(generos)
        opt_genero = util.read_option(f"Selecione o gênero de {titulo}: ", 1, len(generos), "Gênero inválido") - 1
        adicionar_livro(titulo, ano_lancamento, autor, generos[opt_genero])
    elif opt == 1:
        if not possui_livros(livros): continue
        forma_consulta = util.read_option("[ 1 ] Por título\n[ 2 ] Por gênero\nQual a forma de consulta? ", 1, 2, "Consulta inválida") - 1
        if forma_consulta == 0:
            titulo = util.read_string("Digite o título do livro: ", "Digite apenas letras (sem espaços) para o título do livro")
            resultado = consultar_por_titulo(titulo)
        elif forma_consulta == 1:
            util.show_options(generos)
            opt_genero = util.read_option("Selecione o gênero: ", 1, len(generos), "Gênero inválido") - 1
            resultado = consultar_por_genero(generos[opt_genero])
        if not possui_livros(resultado): continue
        for livro in resultado:
            print(f"Título: {livro[0]}")
            print(f"Ano lançamento: {livro[1]}")
            print(f"Autor: {livro[2]}")
            print(f"Gênero: {livro[3]}")
            print()
    elif opt == 2:
        if not possui_livros(livros): continue
        if len(livros_momento) == 3:
            print("Quantidade máxima de livros atingida (3)\n")
            continue
        for i, livro in enumerate(livros, start=1):
            print(f"[ {i} ] {livro[0]}")
        livro_escolhido = util.read_option("Selecione o livro que você está lendo atualmente: ", 1, len(livros)) - 1
        if livro_ja_cadastrado(livros[livro_escolhido][0], True): continue
        adicionar_livro_para_leitura(livros[livro_escolhido][0])
    elif opt == 3:
        if not possui_livros(livros_momento): continue
        util.show_options(livros_momento)
        livro_removido = util.read_option("Selecione o livro a ser removido: ", 1, len(livros_momento), "Digite apenas letras (sem espaços) para o título do livro") - 1
        remover_livro(livros_momento[livro_removido])
