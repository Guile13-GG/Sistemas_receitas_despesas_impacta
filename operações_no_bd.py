#importando SQLlite3
import sqlite3 as sqllite3
import pandas as pd

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

#inserir despesas
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

    #receita total--------------------------------------- 
    receitas = visualizar_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)
    #desepesa total--------------------------------------- 
    despesas = visualizar_despesa()
    despesas_lista = []

    for i in despesas:
        despesas_lista.append(i[3])

    despesa_total = sum(despesas_lista)

    #saldo total--------------------------------------- 
    saldo_total = receita_total - despesa_total
    valores = [receita_total, despesa_total, saldo_total]
    return valores

#função grafico pie---------------------------------
def pie_valores():
    despesas = visualizar_despesa()
    tabela_lista = []

    for i in despesas:
        tabela_lista.append(i)

    dataframe = pd.DataFrame(tabela_lista, columns=['id', 'categoria', 'retirado_em', 'valor'])
    dataframe = dataframe.groupby('categoria')['valor'].sum()

    lista_quantias = dataframe.values.tolist()
    lista_categorias = []

    for i in dataframe.index:
        lista_categorias.append(i)

    return ([lista_categorias, lista_quantias])

#função gráfico porcentagem---------------------------------
def porcentagem_valor():

    #receita total--------------------------------------- 
    receitas = visualizar_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)
    #desepesa total--------------------------------------- 
    despesas = visualizar_despesa()
    despesas_lista = []

    for i in despesas:
        despesas_lista.append(i[3])

    despesa_total = sum(despesas_lista)

    #porcentagem total--------------------------------------- 
    porcentagem_total = (receita_total - despesa_total) / receita_total * 100
    valores = [porcentagem_total]
    return valores