# Sistema de cadastro de produtos CRUD + cadastro no bd.
# Funcionalidade do sistema: Cadastrar, atulizar, deletar e listar os produtos

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Conexão com banco de dados
import sqlite3 # Bilblioteca para usar o banco de dados
conexao = sqlite3.connect("produtos.db") # Conecta o python ao banco 'sqlite3' chamado 'produtos.db', essa conexão é inserida na variável 'conexao'
cursor = conexao.cursor() # O '.cursor' usado para executar os comandos SQL
print("Banco conectado!") # Informa da execução no banco
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Tabela: produtos
# Comando SQL: Cria a tabela 'produtos' caso ela não exita, com os seguintes campos: id, nome, preco e quantidade
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTERGER NOT NULL
)""") 
conexao.commit() # Salva as informações, funciona com um SAVE
print("Tabela criada!")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Funções
def cad_produto():
  print("+---------------------------+")  
  print("|   CADASTRO DE PRODUTOS    |")  
  print("+---------------------------+")
  nome = input("Infome nome do produto: ")  
  preco = float(input("Infome preço do produto: "))  
  qtd = int(input("Infome quantidade do produto: "))  
  print(f"\nPronduto: {nome} Preço: {preco} Quantidade: {qtd}")



cad_produto()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Fecha conexão com banco de dados
conexao.close() # Fecha a conexão com o banco
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
