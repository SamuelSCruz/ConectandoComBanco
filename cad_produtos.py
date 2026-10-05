# Sistema de cadastro de produtos CRUD + cadastro no bd.
# Funcionalidade do sistema: Cadastrar, atulizar, deletar e listar os produtos

import os
import time

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
        quantidade INTEGER NOT NULL
)""") 
conexao.commit() # Salva as informações, funciona com um SAVE
print("Tabela criada!")
time.sleep(3)
os.system("cls")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Funções
#----------------------------------------------------------------------- CADASTRAR
def cadastrar_produto():
  print("+---------------------------+")  
  print("|   CADASTRO DE PRODUTOS    |")  
  print("+---------------------------+")
  
  nome = input("Infome nome do produto: ")  
  preco = float(input("Infome preço do produto: "))  
  qtd = int(input("Infome quantidade do produto: "))  

  cursor.execute(""" 
        INSERT INTO produtos (nome, preco, quantidade)
        VALUES (?,?,?)       
  """, (nome, preco, qtd))
  conexao.commit()

  print("\nProduto cadastrado com sucesso!")
  time.sleep(3)
  os.system("cls")
#----------------------------------------------------------------------- LISTAR
def listar_produto():
  print("+---------------------------+")  
  print("|   CONSULTA DE PRODUTOS    |")  
  print("+---------------------------+")

  cursor.execute(""" Select * from produtos """)
  produtos = cursor.fetchall()

  for id, nome, preco, qtd in produtos:
    print(f"ID: {id} | Produto: {nome} | Preco: {preco} | Quantidade: {qtd}")
  input("\nPress [ENTER] para retornar!")
  os.system("cls")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Mostra as funções
while True:
  try:  
      print("+---------------------------+")  
      print("|           MENU            |")  
      print("+---------------------------+")  
      print("|1 - Cadastrar              |")  
      print("|2 - Listar                 |")    
      print("|0 - Sair                   |")    
      print("+---------------------------+")
      menu = int(input("Iforme opção: "))
  
  except ValueError:
    print("[ERRO] Informe apenas números!")

  match menu:
      case 1:
        os.system("cls")
        cadastrar_produto()
  
      case 2:
        os.system("cls")
        listar_produto()

      case 0:
       os.system("cls")
       break

      case _:
       os.system("cls")
       print("Não tem essa opção!")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- Fecha conexão com banco de dados
conexao.close() # Fecha a conexão com o banco
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
