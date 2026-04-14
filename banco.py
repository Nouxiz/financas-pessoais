import sqlite3

def criar_banco():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS transacoes (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo      TEXT NOT NULL,
    valor     REAL NOT NULL,
    categoria TEXT NOT NULL,
    data      DATE NOT NULL,
    descricao TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS limites (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria  TEXT NOT NULL,
    valor_max  REAL NOT NULL,
    mes        TEXT NOT NULL
    )""")

    conexao.commit()
    conexao.close()

def conectar():
    return sqlite3.connect('banco.db')

criar_banco()