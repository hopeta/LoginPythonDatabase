import sqlite3

#comecanco com uma variavel conn de "conexao" com o arquivo, q o proprio python cria pra nois (usersdata.db)
conn = sqlite3.connect('UsersData.db')

#variavel q vai pegar o 'cursor' ou 'cur' da conexao
cursor = conn.cursor()

#pra rodar um comando SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL

);
""")

print("Conectado com o banco de Dados")
