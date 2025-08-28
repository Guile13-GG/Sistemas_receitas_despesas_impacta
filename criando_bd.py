#importando SQLlite3
import sqlite3 as sqllite3

#Criando a conexão com o banco de dados
con = sqllite3.connect('banco.db')

#Criando o tabela de categorias
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categorias (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

#Criando o tabela de receitas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Receitas (id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionada_em DATE, valor DECIMAL)")

    #Criando o tabela de gastos
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Gastos (id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")