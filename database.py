import sqlite3
conn = sqlite3.connect("universidade.db")

def init_db():
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS membro_universidade (
            nome TEXT,
            email TEXT,
            matricula TEXT PRIMARY KEY
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS aluno (
            matricula TEXT PRIMARY KEY,
            coeficiente_rendimento REAL,
            FOREIGN KEY(matricula) REFERENCES membro_universidade(matricula) ON DELETE CASCADE
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS professor (
            matricula TEXT PRIMARY KEY,
            departamento TEXT,
            titulacao TEXT,
            salario REAL,
            FOREIGN KEY(matricula) REFERENCES membro_universidade(matricula) ON DELETE CASCADE
        )
        """
    )
    conn.execute(
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
    conn.commit()


def criar_membro(nome, email, matricula):
    conn.execute(
        f"INSERT INTO membro_universidade (nome, email, matricula) VALUES ('{nome}', '{email}', '{matricula}')"
    )
    conn.commit()


def buscar_membro(matricula):
    return conn.execute(
        f"SELECT nome, email, matricula FROM membro_universidade WHERE matricula = '{matricula}'"
    ).fetchone()


def atualizar_membro(nome, email, matricula):
    conn.execute(
        f"UPDATE membro_universidade SET nome = '{nome}', email = '{email}' WHERE matricula = '{matricula}'"
    )
    conn.commit()


def deletar_membro(matricula):
    conn.execute(f"DELETE FROM aluno WHERE matricula = '{matricula}'")
    conn.execute(f"DELETE FROM professor WHERE matricula = '{matricula}'")
    conn.execute(f"DELETE FROM membro_universidade WHERE matricula = '{matricula}'")
    conn.commit()


def criar_aluno(matricula, coeficiente_rendimento):
    conn.execute(
        f"INSERT INTO aluno (matricula, coeficiente_rendimento) VALUES ('{matricula}', {coeficiente_rendimento})"
    )
    conn.commit()


def buscar_aluno(matricula):
    return conn.execute(
        f"SELECT membro_universidade.nome, membro_universidade.email, membro_universidade.matricula, aluno.coeficiente_rendimento "
        f"FROM aluno JOIN membro_universidade ON membro_universidade.matricula = aluno.matricula "
        f"WHERE aluno.matricula = '{matricula}'"
    ).fetchone()


def atualizar_aluno(nome, email, coeficiente_rendimento, matricula):
    conn.execute(
        f"UPDATE membro_universidade SET nome = '{nome}', email = '{email}' WHERE matricula = '{matricula}'"
    )
    conn.execute(
        f"UPDATE aluno SET coeficiente_rendimento = {coeficiente_rendimento} WHERE matricula = '{matricula}'"
    )
    conn.commit()


def deletar_aluno(matricula):
    conn.execute(f"DELETE FROM aluno WHERE matricula = '{matricula}'")
    conn.commit()


def criar_professor(matricula, departamento, titulacao, salario):
    conn.execute("INSERT INTO professor (matricula, departamento, titulacao, salario) VALUES "
                 f"('{matricula}', '{departamento}', '{titulacao}', {salario})")
    conn.commit()


def buscar_professor(matricula):
    return conn.execute(
        f"SELECT membro_universidade.nome, membro_universidade.email, membro_universidade.matricula, professor.departamento, professor.titulacao, professor.salario "
        f"FROM professor JOIN membro_universidade ON membro_universidade.matricula = professor.matricula "
        f"WHERE professor.matricula = '{matricula}'"
    ).fetchone()


def atualizar_professor(nome, email, departamento, titulacao, salario, matricula):
    conn.execute(
        f"UPDATE membro_universidade SET nome = '{nome}', email = '{email}' WHERE matricula = '{matricula}'"
    )
    conn.execute(
        f"UPDATE professor SET departamento = '{departamento}', titulacao = '{titulacao}', salario = {salario} "
        f"WHERE matricula = '{matricula}'"
    )
    conn.commit()


def deletar_professor(matricula):
    conn.execute(f"DELETE FROM professor WHERE matricula = '{matricula}'")
    conn.commit()


def criar_disciplina(codigo, descricao, periodo, carga_horaria, nome):
    conn.execute("INSERT INTO disciplina (codigo, descricao, periodo, carga_horaria, nome) VALUES "
                 f"('{codigo}', '{descricao}', '{periodo}', {carga_horaria}, '{nome}')")
    conn.commit()


def buscar_disciplina(codigo):
    return conn.execute(f"SELECT codigo, descricao, periodo, carga_horaria, nome FROM disciplina WHERE codigo = '{codigo}'").fetchone()


def atualizar_disciplina(codigo, descricao, periodo, carga_horaria, nome):
    conn.execute(
        f"UPDATE disciplina SET descricao = '{descricao}', periodo = '{periodo}', carga_horaria = {carga_horaria}, "
        f"nome = '{nome}' WHERE codigo = '{codigo}'"
    )
    conn.commit()


def deletar_disciplina(codigo):
    conn.execute(f"DELETE FROM disciplina WHERE codigo = '{codigo}'")
    conn.commit()
