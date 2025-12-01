import sqlite3

# Conexao unica e simples
conn = sqlite3.connect("universidade.db")
cursor = conn.cursor()

MEMBER_TABLE = "membro_universidade"
OLD_TABLE = "membro_univerisade"

# Renomeia a tabela antiga (com typo) se ela existir
try:
    cursor.execute(f"ALTER TABLE {OLD_TABLE} RENAME TO {MEMBER_TABLE}")
    conn.commit()
except sqlite3.OperationalError:
    pass

# Garante que a tabela exista com o nome correto
cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {MEMBER_TABLE} (
        nome TEXT,
        email TEXT,
        matricula TEXT PRIMARY KEY
    )
    """
)
conn.commit()


def criar_membro(nome, email, matricula):
    cursor.execute(
        f"INSERT INTO {MEMBER_TABLE} (nome, email, matricula) VALUES (?, ?, ?)",
        (nome, email, matricula),
    )
    conn.commit()


def buscar_membro(matricula):
    cursor.execute(
        f"SELECT nome, email, matricula FROM {MEMBER_TABLE} WHERE matricula = ?",
        (matricula,),
    )
    return cursor.fetchone()


def atualizar_membro(nome, email, matricula):
    cursor.execute(
        f"UPDATE {MEMBER_TABLE} SET nome = ?, email = ? WHERE matricula = ?",
        (nome, email, matricula),
    )
    conn.commit()
    return cursor.rowcount


def deletar_membro(matricula):
    cursor.execute(
        f"DELETE FROM {MEMBER_TABLE} WHERE matricula = ?",
        (matricula,),
    )
    conn.commit()
    return cursor.rowcount
