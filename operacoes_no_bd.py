#Criando a conexão com o banco de dados
import mysql.connector
from db import conectar  


# Funções de Categorias


def adicionar_categoria(nome):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO Categorias (nome) VALUES (%s)", (nome,))
    con.commit()
    cursor.close()
    con.close()

def listar_categorias():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT id, nome FROM Categorias")
    categorias = cursor.fetchall()
    cursor.close()
    con.close()
    return categorias


# Funções de Receitas

def adicionar_receita(categoria_id, valor, data):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO Receitas (categoria_id, valor, data) VALUES (%s, %s, %s)",
        (categoria_id, valor, data)
    )
    con.commit()
    cursor.close()
    con.close()


def listar_receitas():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
        SELECT r.id, c.nome, r.valor, r.data
        FROM Receitas r
        JOIN Categorias c ON r.categoria_id = c.id
    """)
    receitas = cursor.fetchall()
    cursor.close()
    con.close()
    return receitas


# Funções de Gastos


def adicionar_gasto(categoria_id, valor, data):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO Gastos (categoria_id, valor, data) VALUES (%s, %s, %s)",
        (categoria_id, valor, data)
    )
    con.commit()
    cursor.close()
    con.close()


def listar_gastos():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
        SELECT g.id, c.nome, g.valor, g.data
        FROM Gastos g
        JOIN Categorias c ON g.categoria_id = c.id
    """)
    gastos = cursor.fetchall()
    cursor.close()
    con.close()
    return gastos


# Funções para Gráficos e Resumos


def pie_valores():
    """Retorna categorias e soma dos gastos para gráfico de pizza"""
    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
        SELECT c.nome AS categoria, COALESCE(SUM(g.valor),0) AS total
        FROM Gastos g
        JOIN Categorias c ON g.categoria_id = c.id
        GROUP BY c.nome
        ORDER BY total DESC
    """)
    resultados = cursor.fetchall()
    cursor.close()
    con.close()

    lista_categorias = [r[0] for r in resultados]
    lista_valores = [float(r[1]) for r in resultados]
    return lista_categorias, lista_valores


def pie_valores_receitas():
    """Retorna categorias e soma das receitas para gráfico de pizza"""
    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
        SELECT c.nome AS categoria, COALESCE(SUM(r.valor),0) AS total
        FROM Receitas r
        JOIN Categorias c ON r.categoria_id = c.id
        GROUP BY c.nome
        ORDER BY total DESC
    """)
    resultados = cursor.fetchall()
    cursor.close()
    con.close()

    lista_categorias = [r[0] for r in resultados]
    lista_valores = [float(r[1]) for r in resultados]
    return lista_categorias, lista_valores


def bar_valores():
    """Retorna total de receitas, gastos e saldo"""
    con = conectar()
    cursor = con.cursor()

    # Receitas
    cursor.execute("SELECT COALESCE(SUM(valor),0) FROM Receitas")
    total_receitas = float(cursor.fetchone()[0])

    # Gastos
    cursor.execute("SELECT COALESCE(SUM(valor),0) FROM Gastos")
    total_gastos = float(cursor.fetchone()[0])

    con.close()

    saldo = total_receitas - total_gastos
    return total_receitas, total_gastos, saldo

def porcentagem_valor():
    total_receitas, total_gastos, saldo = bar_valores()

    if total_receitas == 0:  # evita divisão por zero
        return 0, saldo

    porcentagem = (saldo / total_receitas) * 100
    return porcentagem, saldo


def excluir_receita(id_receita):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM Receitas WHERE id = %s", (id_receita,))
    con.commit()
    cursor.close()
    con.close()

def excluir_gasto(id_gasto):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM Gastos WHERE id = %s", (id_gasto,))
    con.commit()
    cursor.close()
    con.close()
