import sqlite3

MEMBER_TABLE = "membro_universidade"
OLD_TABLE = "membro_univerisade"

def init_db():
    conn = sqlite3.connect("universidade.db")
    cursor = conn.cursor()
    try:
        cursor.execute(f"ALTER TABLE {OLD_TABLE} RENAME TO {MEMBER_TABLE}")
        conn.commit()
    except sqlite3.OperationalError:
        pass
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
    conn.close()

def criar_membro(nome, email, matricula):
    conn = sqlite3.connect("universidade.db")
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO {MEMBER_TABLE} (nome, email, matricula) VALUES (?, ?, ?)",
        (nome, email, matricula),
    )
    conn.commit()
    conn.close()

def buscar_membro(matricula):
    conn = sqlite3.connect("universidade.db")
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT nome, email, matricula FROM {MEMBER_TABLE} WHERE matricula = ?",
        (matricula,),
    )
    result = cursor.fetchone()
    conn.close()
    return result

def atualizar_membro(nome, email, matricula):
    conn = sqlite3.connect("universidade.db")
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE {MEMBER_TABLE} SET nome = ?, email = ? WHERE matricula = ?",
        (nome, email, matricula),
    )
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount

def deletar_membro(matricula):
    conn = sqlite3.connect("universidade.db")
    cursor = conn.cursor()
    cursor.execute(
        f"DELETE FROM {MEMBER_TABLE} WHERE matricula = ?",
        (matricula,),
    )
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount