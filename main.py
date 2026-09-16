# Aprendendo a conectar com banco de dados + CRUD
import os # Importa o (CLS) para limpar o terminal
import time # Importa um tempo de tela no terminal

#----------------------------------------------------------------------------------------------# Conexão com o banco
import sqlite3 # Biblioteca python para usar o banco de dados SQLite

conexao = sqlite3.connect("clientes.db") # Variável que guardará a conexão com o banco 
# Conecta o python ao Banco SQLite chamado (clientes.db)

cursor = conexao.cursor() # Cria o cursor para executar comandos SQL
# Exemplo de uso: cursor.execute("SELECT * FROM clientes") ou cursor.execute("INSERT INTO clientes ...")

print("Banco Conectado!") # Mensagem de que obteve êxito.
#----------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------# Cria tabela no Banco
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    idade INTEGER
 )""")

conexao.commit() # Confirma e salva as informações no banco de dados as alterações que eu fiz
# É como se apertassemos o botão SALVAR

print("Tabela criada com sucesso!")
#----------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------# Cadastrar clientes
def cadastrar_cliente():
    os.system("cls")
    print("\n################## Tela: Cadastrar ##################")
    nome = input("Informe seu nome: ")
    email = input("Informe seu e-mail: ")
    idade = int(input("Informe sua idade: "))

    cursor.execute("""
        INSERT INTO clientes (nome, email, idade)
        VALUES (?,?,?)
    """, (nome, email, idade))

    conexao.commit() # Confirma e salva as informações no banco de dados as alterações que eu fiz
    # É como se apertassemos o botão SALVAR

    print("-> Cliente cadastrado com sucesso!")
    print("#######################################################")
    time.sleep(3)

#----------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------# Consultar clientes
def consultar_todos_cliente():   
    os.system("cls")
    cursor.execute("""Select * From clientes""")
    clientes = cursor.fetchall() # Pega todos os registros encontrados pela consulta e põe em uma variável para ser exibidos

    print("\n#################### Tela: Consultar ####################")
    for id, nome, email, idade in clientes:
        print(f"ID: {id}") # Printa id todos os clientes cadastrados
        print(f"Nome: {nome}") # Printa nome todos os clientes cadastrados
        print(f"E-mail: {email}") # Printa e-mail todos os clientes cadastrados
        print(f"Idade: {idade}\n") # Printa idade todos os clientes cadastrados

    input("\nPressione ENTER para continuar...")
    print("############################################################")

def consultar_por_id():
    os.system("cls")
    print("\n#################### Tela: Consultar por ID ####################")    
    id_cliente = int(input("-> Informe o ID do cliente: "))
    cursor.execute(""" 
        Select * From clientes
        Where id = ?
        """, (id_cliente,))
    cliente = cursor.fetchone() # Pega 1 registro pela consulta e põe em uma variável para ser exibidos

    if cliente: # Condicional para validar se cliente está cadastrado ou não
    #   print(cliente): Imprime os dados cadastrados em uma única linha
        print(f"ID: {cliente[0]}")
        print(f"Nome: {cliente[1]}")
        print(f"Email: {cliente[2]}")
        print(f"Idade: {cliente[3]}")
        time.sleep(3)
        
    else:
        print("Cliente não existe!")
        time.sleep(3)

    clientes2 = cursor.fetchmany()# Pega alguns registros encontrados pela consulta e põe em uma variável para ser exibidos
    print("############################################################")
#----------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------# Atualizar clientes
def atualizar_cliente():
    os.system("cls")
    id_cliente = int(input("Informe o ID do cliente que deseja alterar: "))
    nova_idade = int(input("Informe nova idade: "))

    cursor.execute(""" 
        UPDATE clientes 
        SET idade = ?
        Where id = ?
        """, (nova_idade, id_cliente))

    if cursor.rowcount > 0:
        conexao.commit() # Confirma e salva as informações no banco de dados as alterações que eu fiz
        # É como se apertassemos o botão SALVAR
        print("Atulizado com sucesso!")

        # Consultar cliente com idade atualizada
        cursor.execute(""" 
            Select * From clientes
            Where id = ?
            """, (id_cliente,))
        cliente = cursor.fetchone()
        print(f"Clinte {cliente[1]}teve sua idade atualizada para {cliente[3]}")
        time.sleep(3)

    else:
        print("Cliente não encontrado!")
        time.sleep(3)
#----------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------# Deletar clientes
def deletar_cliente():
    os.system("cls")
    id_cliente = int(input("Informe o ID do cliente que deseja deletar: "))

    cursor.execute(""" 
        DELETE FROM clientes
        Where id = ?
    """, (id_cliente,))

    if cursor.rowcount > 0:
        conexao.commit() # Estamos atualizando no banco
        print("Deletado com sucesso!")
        time.sleep(3)

    else:
        print("Cliente não encontrado!")
        time.sleep(3)
#----------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------# Menu 
while True:
        try:
            os.system("cls") # Limpa terminal
            print("\n===== MENU =====")
            print("1 - Cadastrar")
            print("2 - Consultar")
            print("3 - Atualizar")
            print("4 - Deletar")
            print("0 - Sair")
            menu = int(input("Informe uma opção: "))

        except ValueError:
            print("Informe números!")
            time.sleep(3)
            os.system("cls")
            

        match menu:
            case 1: 
                cadastrar_cliente()

            case 2:
                os.system("cls")
                while True:
                        try:
                            os.system("cls")
                            print("1 - Consultar todos")
                            print("2 - Consultar por ID")
                            print("0 - Voltar menu")
                            menu = int(input("Informe uma opção: "))

                            if menu == 1:
                                consultar_todos_cliente()
                            elif menu == 2:
                                consultar_por_id()
                            elif menu == 0:
                                break
                            else:
                                print("Opção Inválida!")
                                time.sleep(3)
                                os.system("cls")   

                        except ValueError:
                            print("\n[ERRO]Informe números!")
                            time.sleep(3)
                            os.system("cls")             

            case 3:    
                atualizar_cliente() 
                
            case 4:    
                deletar_cliente()

            case 0:
                os.system("cls")
                break

            case _:
                print("Não tem essa opção no Menu!")
                time.sleep(3)

#----------------------------------------------------------------------------------------------# Fecha conexão como banco
conexao.close() # Fecha a conexão com o banco de dados
#----------------------------------------------------------------------------------------------#