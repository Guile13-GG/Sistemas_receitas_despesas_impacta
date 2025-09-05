#importando MySQL Connector
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # coloque aqui seu usuário do MySQL
        password="senha_senha"  # coloque aqui a senha do MySQL
    )

# Conecta ao servidor MySQL
con = conectar()
cur = con.cursor()

# 1. Cria o banco de dados se não existir
cur.execute("CREATE DATABASE IF NOT EXISTS sistema_financeiro")
cur.execute("USE sistema_financeiro")

# 2. Cria as tabelas
cur.execute("""
CREATE TABLE IF NOT EXISTS Categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Receitas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    categoria_id INT,
    valor DECIMAL(10,2) NOT NULL,
    data DATE,
    FOREIGN KEY (categoria_id) REFERENCES Categorias(id)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Gastos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    categoria_id INT,
    valor DECIMAL(10,2) NOT NULL,
    data DATE,
    FOREIGN KEY (categoria_id) REFERENCES Categorias(id)
)
""")

con.commit()
con.close()

print("Banco e tabelas criados com sucesso! 🚀")
