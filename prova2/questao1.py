# Nome: Luiz Vinícius Márdelle Costa Silva
import reader
from datetime import date

livros = []
livros_momento = []
generos = ["Autobiografia", "Biografia", "Conto", "Poesia", "Romance", "Autoajuda"]

def adicionar_livro(titulo, ano_lancamento, autor, genero):
    global livros
    livros.append([titulo, ano_lancamento, autor, genero])

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

def remover_livro(titulo):
    global livros_momento
    try:
        livros_momento.remove(titulo)
        print(f"{titulo} removido")
    except ValueError:
        print(f"{titulo} não encontrado\n")

funcoes = ["Adicionar livro", "Consultar livro", "Adicionar leitura do momento", "Remover leitura momento", "Sair"]

while True:
    for i, funcao in enumerate(funcoes, start=1):
        print(f"[ {i} ] {funcao}")

    opt = reader.read_option("Digite a opção: ", 1, len(funcoes)) - 1
    if opt == len(funcoes) - 1:
        print("Programa encerrado.")
        break

    if opt == 0:
        titulo = reader.read_string("Digite o título do livro: ", "Digite apenas letras (sem espaços) para o título do livro").lower()
        for livro in livros:
            if titulo == livro[0]:
                print("Livro já cadastrado")
                continue
        ano_lancamento = reader.read_option("Digite o ano de lançamento do livro: ", 1900, date.today().year, f"Ano deve ser após 1900 e antes de {date.today().year}")
        autor = reader.read_string(f"Digite o nome do autor de {titulo}: ", "Digite apenas letras (sem espaços) para o autor do livro")
        for i, genero in enumerate(generos, start=1):
            print(f"[ {i} ] {genero}")
        opt_genero = reader.read_option(f"Selecione o gênero de {titulo}: ", 1, len(generos), "Gênero inválido") - 1
        adicionar_livro(titulo, ano_lancamento, autor, generos[opt_genero])
        print(f"{titulo} adicionado com sucesso\n")
    elif opt == 1:
        if len(livros) == 0:
            print("Nenhum livro cadastrado\n")
            continue
        
        print("[ 1 ] Por título\n[ 2 ] Por gênero")
        forma_consulta = reader.read_option("Qual a forma de consulta? ", 1, 2, "Forma de consulta inválida") - 1
        if forma_consulta == 0:
            titulo = reader.read_string("Digite o título do livro: ", "Digite apenas letras (sem espaços) para o título do livro")
            resultado = consultar_por_titulo(titulo)
            if len(resultado) == 0:
                print("Livro(s) não encontrado(s)\n")
                continue
            
            for livro in resultado:
                print(f"Título: {livro[0]}")
                print(f"Ano lançamento: {livro[1]}")
                print(f"Autor: {livro[2]}")
                print(f"Gênero: {livro[3]}")
                print()
        elif forma_consulta == 1:
            for i, genero in enumerate(generos, start=1):
                print(f"[ {i} ] {genero}")
            opt_genero = reader.read_option(f"Selecione o gênero de {titulo}: ", 1, len(generos), "Gênero inválido") - 1
            
            resultado = consultar_por_genero(generos[opt_genero])
            if len(resultado) == 0:
                print("Nenhum livro com esse gênero foi encontrado\n")
                continue
            
            for livro in resultado:
                print(f"Título: {livro[0]}")
                print(f"Ano lançamento: {livro[1]}")
                print(f"Autor: {livro[2]}")
                print(f"Gênero: {livro[3]}")
                print()
    elif opt == 2:
        if len(livros) == 0:
            print("Nenhum livro sendo lido atualmente.")
            continue
        if len(livros_momento) == 3:
            print("Quantidade máxima de livros atingida (3)")
            continue

        for i, livro in enumerate(livros, start=1):
            print(f"[ {i} ] {livro[0]}")
        livro_escolhido = reader.read_option("Selecione o livro que você está lendo atualmente: ", 1, len(livros)) - 1
        ja_adicionado = False
        for i, titulo in enumerate(livros_momento):
            if livros[livro_escolhido][0] == titulo:
                ja_adicionado = True
                print("Livro já adicionado")
        if ja_adicionado: continue
        print(f"{livros[livro_escolhido][0]} adicionado a leitura do momento\n")
        adicionar_livro_para_leitura(livros[livro_escolhido][0])
    elif opt == 3:
        if len(livros_momento) == 0:
            print("Nenhum livro sendo lido atualmente\n")
            continue

        for i, titulo in enumerate(livros_momento, start=1):
            print(f"{i} {titulo}")
        livro_removido = reader.read_option("Selecione o livro a ser removido: ", 1, len(livros_momento), "Digite apenas letras (sem espaços) para o título do livro") - 1
        remover_livro(livros_momento[livro_removido])
