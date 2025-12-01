import sqlite3

# Conexao unica e simples
conn = sqlite3.connect("universidade.db")
cursor = conn.cursor()

# Garante que a tabela exista
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS membro_univerisade (
        nome TEXT,
        email TEXT,
        matricula TEXT PRIMARY KEY
    )
    """
)
conn.commit()


def criar_membro(nome, email, matricula):
    cursor.execute(
        "INSERT INTO membro_univerisade (nome, email, matricula) VALUES (?, ?, ?)",
        (nome, email, matricula),
    )
    conn.commit()


def buscar_membro(matricula):
    cursor.execute(
        "SELECT nome, email, matricula FROM membro_univerisade WHERE matricula = ?",
        (matricula,),
    )
    return cursor.fetchone()


def atualizar_membro(nome, email, matricula):
    cursor.execute(
        "UPDATE membro_univerisade SET nome = ?, email = ? WHERE matricula = ?",
        (nome, email, matricula),
    )
    conn.commit()
    return cursor.rowcount


def deletar_membro(matricula):
    cursor.execute(
        "DELETE FROM membro_univerisade WHERE matricula = ?",
        (matricula,),
    )
    conn.commit()
    return cursor.rowcount
