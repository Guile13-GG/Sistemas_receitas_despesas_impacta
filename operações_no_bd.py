#importando SQLlite3
import sqlite3 as sqllite3

#Criando a conexão com o banco de dados
con = sqllite3.connect('banco.db')

#função de inserção de dados---------------------------------

#inserir Categorias
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Categorias (nome) VALUES (?)'
        cur.execute(query, i,)

#inserir Receitas
def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Receitas (categoria, adicionada_em, valor) VALUES (?, ?, ?)'
        cur.execute(query, i)

#inserir Gastos
def inserir_despesa(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?, ?, ?)'
        cur.execute(query, i)

#função de exclusão de dados---------------------------------

#excluir Receitas
def excluir_receita(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Receitas WHERE id = ?'
        cur.execute(query, i,)

#excluir Gastos
def excluir_despesa(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Gastos WHERE id = ?'
        cur.execute(query, i,)

#função de visualização de dados---------------------------------

#visualizar Categorias
def visualizar_categorias():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categorias")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

#visualizar Receitas
def visualizar_receitas():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

#visualizar Gastos
def visualizar_despesa():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

#função para dados da tabela---------------------------------
def tabela_dados():
    gastos = visualizar_despesa()
    receitas = visualizar_receitas()

    tabela_lista = []
    for i in gastos:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista

#função para dados do gráfico bar---------------------------------
def bar_valores():

    #receita total
    receitas = visualizar_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])