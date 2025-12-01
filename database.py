import sqlite3
conn = sqlite3.connect('universidade.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS membro_universidade (nome VARCHAR(100), email VARCHAR(100), matricula VARCHAR(20) PRIMARY KEY)")
cursor.execute("CREATE TABLE IF NOT EXISTS aluno (nome VARCHAR(100), email VARCHAR(100), matricula VARCHAR(20) PRIMARY KEY, coeficiente_rendimento FLOAT, FOREIGN KEY(matricula) REFERENCES membro_universidade(matricula))")
cursor.execute("CREATE TABLE IF NOT EXISTS professor (nome VARCHAR(100), email VARCHAR(100), matricula VARCHAR(20) PRIMARY KEY, departamento VARCHAR(100), titulacao VARCHAR(50), salario FLOAT, FOREIGN KEY(matricula) REFERENCES membro_universidade(matricula))")
cursor.execute("CREATE TABLE IF NOT EXISTS disciplina (codigo VARCHAR(20) PRIMARY KEY, descricao TEXT, periodo VARCHAR(20), carga_horaria INTEGER, nome VARCHAR(100))")

conn.commit()
conn.close()