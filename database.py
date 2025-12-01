import sqlite3


MEMBER_TABLE = "membro_universidade"
OLD_TABLE = "membro_univerisade"


def _get_connection():
    """Abre conexao habilitando chaves estrangeiras para manter as tabelas em sincronia."""
    conn = sqlite3.connect("universidade.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = _get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(f"ALTER TABLE {OLD_TABLE} RENAME TO {MEMBER_TABLE}")
        conn.commit()
    except sqlite3.OperationalError:
        # tabela antiga nao existe, segue o fluxo normal
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
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS disciplina (
            codigo TEXT PRIMARY KEY,
            descricao TEXT,
            periodo TEXT,
            carga_horaria INTEGER,
            nome TEXT
        )
        """
    )
    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS aluno (
            matricula TEXT PRIMARY KEY,
            coeficiente_rendimento REAL,
            FOREIGN KEY(matricula) REFERENCES {MEMBER_TABLE}(matricula) ON DELETE CASCADE
        )
        """
    )
    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS professor (
            matricula TEXT PRIMARY KEY,
            departamento TEXT,
            titulacao TEXT,
            salario REAL,
            FOREIGN KEY(matricula) REFERENCES {MEMBER_TABLE}(matricula) ON DELETE CASCADE
        )
        """
    )
    conn.commit()
    conn.close()


def criar_membro(nome, email, matricula):
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO {MEMBER_TABLE} (nome, email, matricula) VALUES (?, ?, ?)",
        (nome, email, matricula),
    )
    conn.commit()
    conn.close()


def buscar_membro(matricula):
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT nome, email, matricula FROM {MEMBER_TABLE} WHERE matricula = ?",
        (matricula,),
    )
    result = cursor.fetchone()
    conn.close()
    return result


def atualizar_membro(nome, email, matricula):
    conn = _get_connection()
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
    conn = _get_connection()
    cursor = conn.cursor()
    # remove filhos antes para manter integridade mesmo sem ON DELETE
    cursor.execute("DELETE FROM aluno WHERE matricula = ?", (matricula,))
    cursor.execute("DELETE FROM professor WHERE matricula = ?", (matricula,))
    cursor.execute(
        f"DELETE FROM {MEMBER_TABLE} WHERE matricula = ?",
        (matricula,),
    )
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount


def criar_aluno(matricula, coeficiente_rendimento):
    """Cria registro de aluno somente se o membro base existir."""
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT 1 FROM {MEMBER_TABLE} WHERE matricula = ?",
        (matricula,),
    )
    if cursor.fetchone() is None:
        conn.close()
        raise sqlite3.IntegrityError("Membro nao cadastrado")
    cursor.execute(
        """
        INSERT INTO aluno (matricula, coeficiente_rendimento)
        VALUES (?, ?)
        """,
        (matricula, coeficiente_rendimento),
    )
    conn.commit()
    conn.close()


def buscar_aluno(matricula):
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"""
        SELECT m.nome, m.email, m.matricula, a.coeficiente_rendimento
        FROM aluno a
        JOIN {MEMBER_TABLE} m ON m.matricula = a.matricula
        WHERE a.matricula = ?
        """,
        (matricula,),
    )
    result = cursor.fetchone()
    conn.close()
    return result


def atualizar_aluno(nome, email, coeficiente_rendimento, matricula):
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE {MEMBER_TABLE} SET nome = ?, email = ? WHERE matricula = ?",
        (nome, email, matricula),
    )
    cursor.execute(
        """
        UPDATE aluno
        SET coeficiente_rendimento = ?
        WHERE matricula = ?
        """,
        (coeficiente_rendimento, matricula),
    )
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount


def deletar_aluno(matricula):
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM aluno WHERE matricula = ?", (matricula,))
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount


def criar_professor(matricula, departamento, titulacao, salario):
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT 1 FROM {MEMBER_TABLE} WHERE matricula = ?",
        (matricula,),
    )
    if cursor.fetchone() is None:
        conn.close()
        raise sqlite3.IntegrityError("Membro nao cadastrado")
    cursor.execute(
        """
        INSERT INTO professor (matricula, departamento, titulacao, salario)
        VALUES (?, ?, ?, ?)
        """,
        (matricula, departamento, titulacao, salario),
    )
    conn.commit()
    conn.close()


def buscar_professor(matricula):
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"""
        SELECT m.nome, m.email, m.matricula, p.departamento, p.titulacao, p.salario
        FROM professor p
        JOIN {MEMBER_TABLE} m ON m.matricula = p.matricula
        WHERE p.matricula = ?
        """,
        (matricula,),
    )
    result = cursor.fetchone()
    conn.close()
    return result


def atualizar_professor(nome, email, departamento, titulacao, salario, matricula):
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE {MEMBER_TABLE} SET nome = ?, email = ? WHERE matricula = ?",
        (nome, email, matricula),
    )
    cursor.execute(
        """
        UPDATE professor
        SET departamento = ?, titulacao = ?, salario = ?
        WHERE matricula = ?
        """,
        (departamento, titulacao, salario, matricula),
    )
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount


def deletar_professor(matricula):
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM professor WHERE matricula = ?", (matricula,))
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount


def criar_disciplina(codigo, descricao, periodo, carga_horaria, nome):
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO disciplina (codigo, descricao, periodo, carga_horaria, nome)
        VALUES (?, ?, ?, ?, ?)
        """,
        (codigo, descricao, periodo, carga_horaria, nome),
    )
    conn.commit()
    conn.close()


def buscar_disciplina(codigo):
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT codigo, descricao, periodo, carga_horaria, nome
        FROM disciplina
        WHERE codigo = ?
        """,
        (codigo,),
    )
    result = cursor.fetchone()
    conn.close()
    return result


def atualizar_disciplina(codigo, descricao, periodo, carga_horaria, nome):
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE disciplina
        SET descricao = ?, periodo = ?, carga_horaria = ?, nome = ?
        WHERE codigo = ?
        """,
        (descricao, periodo, carga_horaria, nome, codigo),
    )
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount


def deletar_disciplina(codigo):
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM disciplina WHERE codigo = ?", (codigo,))
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount
