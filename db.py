import mysql.connector

def conectar():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",          #seu usuário MySQL
            password="senha_senha", #sua senha MySQL
            database="sistema_financeiro"
        )
        return con
    except mysql.connector.Error as err:
        print(f"Erro ao conectar no banco: {err}")
        return None
