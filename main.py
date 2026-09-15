# Aprendendo a conectar com banco de dados + CRUD

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


#----------------------------------------------------------------------------------------------# Cadastro clientes
nome = input("\nInforme seu nome: ")
email = input("Informe seu e-mail: ")
idade = int(input("Informe sua idade: "))

cursor.execute("""
    INSERT INTO clientes (nome, email, idade)
    VALUES (?,?,?)
 """, (nome, email, idade))

conexao.commit() # Confirma e salva as informações no banco de dados as alterações que eu fiz
# É como se apertassemos o botão SALVAR

print("-> Cliente cadastrado com sucesso!\n")
#----------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------# Consultar clientes
cursor.execute("Select * From clientes")
clientes = cursor.fetchall() # Pega todos os registros encontrados pela consulta e põe em uma variável para ser exibidos
clientes1 = cursor.fetchone() # Pega 1 registro pela consulta e põe em uma variável para ser exibidos
clientes2 = cursor.fetchmany()# Pega alguns registros encontrados pela consulta e põe em uma variável para ser exibidos

for id, nome, email, idade in clientes:
    print(f"\nID: {id}") # Printa id todos os clientes cadastrados
    print(f"Nome: {nome}") # Printa nome todos os clientes cadastrados
    print(f"E-mail: {email}") # Printa e-mail todos os clientes cadastrados
    print(f"Idade: {idade}") # Printa idade todos os clientes cadastrados
#----------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------# Fecha conexão como banco
conexao.close() # Fecha a conexão com o banco de dados
#----------------------------------------------------------------------------------------------#