import sqlite3


def _conn():
    c = sqlite3.connect("universidade.db")
    c.execute("PRAGMA foreign_keys = ON")
    return c


def init_db():
    c = _conn()
    c.execute("CREATE TABLE IF NOT EXISTS membro_universidade (nome TEXT, email TEXT, matricula TEXT PRIMARY KEY)")
    c.execute("CREATE TABLE IF NOT EXISTS aluno (matricula TEXT PRIMARY KEY, coeficiente_rendimento REAL, FOREIGN KEY(matricula) REFERENCES membro_universidade(matricula) ON DELETE CASCADE)")
    c.execute("CREATE TABLE IF NOT EXISTS professor (matricula TEXT PRIMARY KEY, departamento TEXT, titulacao TEXT, salario REAL, FOREIGN KEY(matricula) REFERENCES membro_universidade(matricula) ON DELETE CASCADE)")
    c.execute("CREATE TABLE IF NOT EXISTS disciplina (codigo TEXT PRIMARY KEY, descricao TEXT, periodo TEXT, carga_horaria INTEGER, nome TEXT)")
    c.commit()
    c.close()


def criar_membro(nome, email, matricula):
    c = _conn()
    c.execute(
        "INSERT INTO membro_universidade (nome, email, matricula) VALUES (?, ?, ?)",
        (nome, email, matricula),
    )
    c.commit()
    c.close()


def buscar_membro(matricula):
    c = _conn()
    r = c.execute(
        "SELECT nome, email, matricula FROM membro_universidade WHERE matricula = ?",
        (matricula,),
    ).fetchone()
    c.close()
    return r


def atualizar_membro(nome, email, matricula):
    c = _conn()
    c.execute(
        "UPDATE membro_universidade SET nome = ?, email = ? WHERE matricula = ?",
        (nome, email, matricula),
    )
    c.commit()
    c.close()


def deletar_membro(matricula):
    c = _conn()
    c.execute("DELETE FROM aluno WHERE matricula = ?", (matricula,))
    c.execute("DELETE FROM professor WHERE matricula = ?", (matricula,))
    c.execute("DELETE FROM membro_universidade WHERE matricula = ?", (matricula,))
    c.commit()
    c.close()


def criar_aluno(matricula, coeficiente_rendimento):
    c = _conn()
    c.execute(
        "INSERT INTO aluno (matricula, coeficiente_rendimento) VALUES (?, ?)",
        (matricula, coeficiente_rendimento),
    )
    c.commit()
    c.close()


def buscar_aluno(matricula):
    c = _conn()
    r = c.execute(
        "SELECT m.nome, m.email, m.matricula, a.coeficiente_rendimento FROM aluno a JOIN membro_universidade m ON m.matricula = a.matricula WHERE a.matricula = ?",
        (matricula,),
    ).fetchone()
    c.close()
    return r


def atualizar_aluno(nome, email, coeficiente_rendimento, matricula):
    c = _conn()
    c.execute(
        "UPDATE membro_universidade SET nome = ?, email = ? WHERE matricula = ?",
        (nome, email, matricula),
    )
    c.execute(
        "UPDATE aluno SET coeficiente_rendimento = ? WHERE matricula = ?",
        (coeficiente_rendimento, matricula),
    )
    c.commit()
    c.close()


def deletar_aluno(matricula):
    c = _conn()
    c.execute("DELETE FROM aluno WHERE matricula = ?", (matricula,))
    c.commit()
    c.close()


def criar_professor(matricula, departamento, titulacao, salario):
    c = _conn()
    c.execute("INSERT INTO professor (matricula, departamento, titulacao, salario) VALUES (?, ?, ?, ?)",
        (matricula, departamento, titulacao, salario))
    c.commit()
    c.close()


def buscar_professor(matricula):
    c = _conn()
    r = c.execute(
        "SELECT m.nome, m.email, m.matricula, p.departamento, p.titulacao, p.salario FROM professor p JOIN membro_universidade m ON m.matricula = p.matricula WHERE p.matricula = ?",
        (matricula,),
    ).fetchone()
    c.close()
    return r


def atualizar_professor(nome, email, departamento, titulacao, salario, matricula):
    c = _conn()
    c.execute("UPDATE membro_universidade SET nome = ?, email = ? WHERE matricula = ?", (nome, email, matricula))
    c.execute("UPDATE professor SET departamento = ?, titulacao = ?, salario = ? WHERE matricula = ?",
        (departamento, titulacao, salario, matricula))
    c.commit()
    c.close()


def deletar_professor(matricula):
    c = _conn()
    c.execute("DELETE FROM professor WHERE matricula = ?", (matricula,))
    c.commit()
    c.close()


def criar_disciplina(codigo, descricao, periodo, carga_horaria, nome):
    c = _conn()
    c.execute("INSERT INTO disciplina (codigo, descricao, periodo, carga_horaria, nome) VALUES (?, ?, ?, ?, ?)",
        (codigo, descricao, periodo, carga_horaria, nome))
    c.commit()
    c.close()


def buscar_disciplina(codigo):
    c = _conn()
    r = c.execute("SELECT codigo, descricao, periodo, carga_horaria, nome FROM disciplina WHERE codigo = ?", (codigo,)).fetchone()
    c.close()
    return r


def atualizar_disciplina(codigo, descricao, periodo, carga_horaria, nome):
    c = _conn()
    c.execute("UPDATE disciplina SET descricao = ?, periodo = ?, carga_horaria = ?, nome = ? WHERE codigo = ?",
        (descricao, periodo, carga_horaria, nome, codigo))
    c.commit()
    c.close()


def deletar_disciplina(codigo):
    c = _conn()
    c.execute("DELETE FROM disciplina WHERE codigo = ?", (codigo,))
    c.commit()
    c.close()
