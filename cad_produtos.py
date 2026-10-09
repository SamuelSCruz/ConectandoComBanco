# Sistema de cadastro de produtos CRUD + cadastro no bd.
# Funcionalidade do sistema: Cadastrar, atulizar, deletar e listar os produtos

import os
import time

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Conexão com banco de dados
import sqlite3  # Bilblioteca para usar o banco de dados

conexao = sqlite3.connect(
    "produtos.db"
)  # Conecta o python ao banco 'sqlite3' chamado 'produtos.db', essa conexão é inserida na variável 'conexao'
cursor = conexao.cursor()  # O '.cursor' usado para executar os comandos SQL
print("Banco conectado!")  # Informa da execução no banco
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Tabela: produtos
# Comando SQL: Cria a tabela 'produtos' caso ela não exita, com os seguintes campos: id, nome, preco e quantidade
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL
)""")
conexao.commit()  # Salva as informações, funciona com um SAVE
print("Tabela criada!")
time.sleep(1)
os.system("cls")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Funções
# =============================================================================== CADASTRAR
def cadastrar_produto():
    print("+---------------------------+")
    print("|    CADASTRAR PRODUTOS     |")
    print("+---------------------------+")

    nome = input("Infome nome do produto: ")
    preco = float(input("Infome preço do produto: "))
    qtd = int(input("Infome quantidade do produto: "))

    cursor.execute(
        """ 
        INSERT INTO produtos (nome, preco, quantidade)
        VALUES (?,?,?)       
  """,
        (nome, preco, qtd),
    )
    conexao.commit()

    print("\nProduto cadastrado com sucesso!")
    time.sleep(3)
    os.system("cls")


# ===============================================================================


# =============================================================================== LISTAR
def listar_todos_produto():
    print("+---------------------------+")
    print("|    CONSULTAR PRODUTOS     |")
    print("+---------------------------+")

    cursor.execute(""" Select * from produtos """)
    produtos = cursor.fetchall()

    for id, nome, preco, qtd in produtos:
        print(f"ID: {id} | Produto: {nome} | Preco: {preco} | Quantidade: {qtd}")
    input("\nPress [ENTER] para retornar!")
    os.system("cls")


# ===============================================================================


# =============================================================================== ATUALIZAR
def atualizar_produto():
    while True:
        try:
            print("+----------------------------+")
            print("|     ATUALIZAR PRODUTOS     |")
            print("+----------------------------+")
            id_produto = int(input("Informe ID que deseja alterar: "))

        except ValueError:
            print("[ERRO] Informe apenas números!")
            time.sleep(3)
            os.system("cls")
            continue

        cursor.execute(
            """ Select * from produtos
        where ID = ?
        """,
            (id_produto,),
        )
        produto = cursor.fetchone()

        if produto:
            print(
                f"ID: {produto[0]} NOME: {produto[1]} PRECO: {produto[2]} QUANTIDADE: {produto[3]}"
            )
            condicao = input("ID encontrado! Deseja realmente alterar este ID? (y/n): ")

            match condicao.strip().lower():
                case "y":
                    while True:
                        try:
                            print("+---------------------------+")
                            print("|1 - NOME                   |")
                            print("|2 - PREÇO                  |")
                            print("|3 - QUANTIDADE             |")
                            print("|0 - Sair                   |")
                            print("+---------------------------+")
                            alterar = int(input("\nInforme o que deseja alterar: "))

                        except ValueError:
                            print("[ERRO] Informe apenas números!")
                            time.sleep(3)
                            os.system("cls")
                            continue

                        match alterar:
                            case 1:
                                novo_nome = input("Informe o novo nome: ")
                                cursor.execute(
                                    """ Update produtos 
                                            SET nome = ?
                                            Where id = ?""",
                                    (novo_nome, id_produto),
                                )

                                if cursor.rowcount > 0:
                                    conexao.commit()
                                    print("Atualizado com sucesso!")

                                else:
                                    print("Produto não encontrado!")

                            case 2:
                                novo_preco = input("Informe o novo preço: ")
                                cursor.execute(
                                    """ Update produtos 
                                            SET preco = ?
                                            Where id = ?""",
                                    (novo_preco, id_produto),
                                )

                                if cursor.rowcount > 0:
                                    conexao.commit()
                                    print("Atualizado com sucesso!")

                                else:
                                    print("Produto não encontrado!")

                            case 3:
                                novo_qtd = input("Informe o nova quantidade: ")
                                cursor.execute(
                                    """ Update produtos 
                                            SET quantidade = ?
                                            Where id = ?""",
                                    (novo_qtd, id_produto),
                                )

                                if cursor.rowcount > 0:
                                    conexao.commit()
                                    print("Atualizado com sucesso!")

                                else:
                                    print("Produto não encontrado!")
                case "n":

                    condicao2 = input("\nDeseja informar outro ID? (y/n): ")

                    if condicao2.strip().lower() == "y":
                        print("Voltando...")
                        time.sleep(3)
                        os.system("cls")

                    elif condicao2.strip().lower() == "n":
                        print("Saindo...")
                        time.sleep(3)
                        os.system("cls")
                        break

                    else:
                        print("\nInforme uma opção válida!")
                        time.sleep(3)
                        os.system("cls")

                case _:
                    print("Não tem essa opção no Menu!")
                    time.sleep(3)

        else:
            print("Produto não exite!")
            time.sleep(3)
            os.system("cls")


# ===============================================================================


# =============================================================================== DELETAR
def deletar_produto():
    while True:  # Loop para o menu
        try:  # Tratamento de exceções
            print("+----------------------------+")
            print("|      DELETAR PRODUTOS      |")
            print("+----------------------------+")
            id_produto = int(input("Informe ID que deseja deletar: "))

        except (
            ValueError
        ):  # Trata erros, neste caso, usário deverá informar apenas números
            print("[ERRO] Informe apenas números!")  # Imprime o erro
            time.sleep(3)
            os.system("cls")
            continue  # Avança todo o restante do código e retorna para o loop, sem ele o código avançaria para a o primeiro if e não seria tratado

        cursor.execute(
            """ 
          Select * From produtos
          Where id = ?
          """,
            (id_produto,),
        )  # A vírgula (id_cliente, <--) é chamada de TUPLA, é uma forma de guardar vários valores.
        produto = (
            cursor.fetchone()
        )  # Pega 1 registro pela consulta e põe em uma variável para ser exibidos

        if produto:  # Condicional que valida o produto cadastrado
            print(
                f"ID: {produto[0]} | Produto: {produto[1]} | Preco: {produto[2]} | Quantidade: {produto[3]}"
            )  # Impressão do produto informado
            condicao = input("ID encontrado! Deseja realmente deletar este ID? (y/n): ")

            match condicao.strip().lower():  # Escolhas para cada caso
                case "y":  # Caso escolha (y), produto será deletado.
                    cursor.execute(
                        """
                  DELETE FROM produtos
                  WHERE id = ?
                  """,
                        (id_produto,),
                    )

                    print("\nProduto deletado!")
                    conexao.commit()  # Salva as informações
                    time.sleep(3)
                    os.system("cls")
                    break

                case (
                    "n"
                ):  # Caso escolha (n), imprime ao usuário se ele deseja informar outro ID, se não voltará ao menu principal
                    condicao2 = input("\nDeseja informar outro ID? (y/n): ")

                    if condicao2.strip().lower() == "y":
                        print("Voltando...")
                        time.sleep(3)
                        os.system("cls")

                    elif condicao2.strip().lower() == "n":
                        print("Saindo...")
                        time.sleep(3)
                        os.system("cls")
                        break

                    else:
                        print("\nInforme uma opção válida!")
                        time.sleep(3)
                        os.system("cls")

                case _:
                    print("Não tem essa opção no Menu!")
                    time.sleep(3)

        else:  # Condicial que imprime que produto não estar cadastrado.
            print("\nProduto não encontrado!")
            time.sleep(1)
            os.system("cls")


# ===============================================================================

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Mostra as funções
while True:  # Loop para permanecer no MENU até que o usuário queira sair (0)
    try:  # Tratamento de exceção: Permite apenas que o usuário informe números, tratando este erro.
        print("+---------------------------+")
        print("|           MENU            |")
        print("+---------------------------+")
        print("|1 - Cadastrar              |")
        print("|2 - Listar                 |")
        print("|3 - Atualizar              |")
        print("|4 - Deletar                |")
        print("|0 - Sair                   |")
        print("+---------------------------+")
        menu = int(input("Iforme opção: "))

    except (
        ValueError
    ):  # Retorno um aviso ao usuário informando que só é permitido números
        print("[ERRO] Informe apenas números!")
        time.sleep(3)
        os.system("cls")
        continue  # Avança todo o restante do código e retorna para o loop, sem ele o código avançaria para a o primeiro if e não seria tratado

    match menu:
        case 1:
            os.system("cls")
            cadastrar_produto()

        case 2:
            os.system("cls")
            listar_todos_produto()

        case 3:
            os.system("cls")
            atualizar_produto()

        case 4:
            os.system("cls")
            deletar_produto()

        case 0:
            os.system("cls")
            break

        case _:
            os.system("cls")
            print("Não tem essa opção!")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Fecha conexão com banco de dados
conexao.close()  # Fecha a conexão com o banco
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
